# main.py
from core.scraper import FacebookScraper
import warnings

warnings.filterwarnings("ignore", category=ResourceWarning, module="asyncio")  # Ignora todos los warnings [[1]]

async def main():
    # Inicializa el scraper con PostgreSQL
    scraper = FacebookScraper(
        email="rafael.padron773@proton.me",
        password="@Rp230594.Facebook@",
        db_type="sqlite"  # Cambia a "sqlite" para pruebas locales
    )
    
    # Ejecuta la búsqueda y guarda resultados automáticamente
    await scraper.search("corolla 2018")

# Ejecución principal
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())