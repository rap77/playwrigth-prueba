# Ejemplo: Extracción del atributo 'href' de un enlace y 'src' de una imagen
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://scrapeme.live/shop/') # URL de ejemplo para demostración

        # Localizar el primer enlace de producto y obtener su atributo 'href'.
        # Usamos.first para obtener el primer elemento que coincida.
        link_element = await page.locator('a.woocommerce-LoopProduct-link').first.get_attribute('href') #
        print(f"Enlace del producto: {link_element}")

        # Localizar la primera imagen de producto y obtener su atributo 'src'.
        image_element = await page.locator('img.attachment-woocommerce_thumbnail').first.get_attribute('src') # [15, 26, 35]
        print(f"URL de la imagen: {image_element}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())