import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Ejemplo de uso en el scraper
logging.info("Iniciando scraping de productos")  [[10]]