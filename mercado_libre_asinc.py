import asyncio
from playwright.async_api import async_playwright
import polars as pl

queries = ["Sonos move 2", "JBL Charge 5", "Bose SoundLink", "Sony XB33"]

async def scrap_site(playwright, query):
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()

    url = f"https://listado.mercadolibre.com.ve/{query.replace(' ', '-')}"
    await page.goto(url)

    try:
        await page.wait_for_selector('text="Agregar ubicación"', timeout=1000)
        await page.click('text="Más tarde"')
    except:
        pass

    await page.wait_for_selector("#shipping_highlighted_fulfillment", timeout=2000)
    await page.click("#shipping_highlighted_fulfillment")
    await page.wait_for_selector("li.ui-search-layout__item", timeout=5000)
    items = await page.query_selector_all("li.ui-search-layout__item")

    results = []

    for item in items:

        title = await item.query_selector("h3")
        price = await item.query_selector("span.andes-money-amount__fraction")
        link = await item.query_selector("a")

        title_val = await title.inner_text() if title else ""
        price_val = await price.inner_text() if price else ""
        link_val = await link.get_attribute("href") if link else ""

        results.append((query, title_val.strip(), price_val.strip(), link_val))


    await browser.close()
    return results

async def main():
    async with async_playwright() as p:
        tasks = [scrap_site(p, q) for q in queries]
        all_results = await asyncio.gather(*tasks)

    flat = [item for sublist in all_results for item in sublist]
    df = pl.DataFrame(flat, schema=["Query", "Title", "Price", "Link"])
    df.write_csv("productos.csv")

asyncio.run(main())