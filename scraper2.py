# Ejemplo: Extracción del título de un producto utilizando su clase CSS
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://scrapeme.live/shop/') # URL de ejemplo para demostración

        # Seleccionar todos los elementos que coincidan con la clase '.woocommerce-loop-product__title'
        product_elements = await page.query_selector_all('.woocommerce-loop-product__title') 

        # Obtener el contenido de texto del tercer producto (índice 2 en un array basado en cero).
        if len(product_elements) > 2:
            third_product_title = await product_elements[2].text_content() 
            print(f"Título del 3er producto: {third_product_title}")
        else:
            print("No se encontraron suficientes productos.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())