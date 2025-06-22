# scraper.py
import asyncio
from playwright.async_api import async_playwright 

async def main():
    # Usamos 'async with' para asegurar que los recursos se cierren correctamente.
    async with async_playwright() as p:
        # Lanzar una nueva instancia del navegador Chromium.
        # La opción 'headless=True' (por defecto) ejecuta el navegador sin interfaz gráfica,
        # lo cual es ideal para entornos de producción debido a su eficiencia.
        # La opción 'headless=False' abre una ventana visible del navegador,
        # lo que es extremadamente útil para la depuración y para observar
        # el comportamiento del script en tiempo real.
        browser = await p.chromium.launch(headless=False) 

        # Abrir una nueva página (equivalente a una nueva pestaña) en el navegador.
        page = await browser.new_page() 

        # Navegar a una URL de ejemplo.
        await page.goto('https://www.scrapingcourse.com/javascript-rendering') 

        # Imprimir el título de la página en la consola para verificar que la navegación fue exitosa.
        print(f"Título de la página: {await page.title()}") 

        # Cerrar el navegador para liberar recursos.
        await browser.close() 

if __name__ == "__main__":
    asyncio.run(main())