# core/scraper.py
from models.product import Product
from config.database import Database
from typing import List
import logging
import asyncio
from random import uniform
from tenacity import retry, stop_after_attempt, wait_exponential
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO)

class FacebookScraper:
    def __init__(self, email: str, password: str, db_type: str = "sqlite"):
        self.email = email
        self.password = password
        self.db = Database(db_type)
        self.db.create_tables()  # Crea tablas automáticamente [[1]]
        self.base_url = "https://www.facebook.com/marketplace/category" 

    @retry(stop=stop_after_attempt(3), wait=wait_exponential())
    async def save_results(self, results: List[Product]):
        """Guarda resultados con manejo de transacciones [[9]]"""
        session = self.db.Session()
        try:
            session.add_all(results)
            session.commit()
        except Exception as e:
            session.rollback()  # Rollback en caso de error [[9]]
            logging.error(f"Error en transacción: {e}")
            raise
        finally:
            session.close()

    async def _init_browser(self):
        """Inicializa navegador con configuración anti-detección [[1]][[8]]"""
        if not hasattr(self, "playwright"):
            raise RuntimeError("Playwright no inicializado")
        self.browser = await self.playwright.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
            #,proxy={"server": "http://user:pass@proxy-ip:port"}  # Proxy rotativo [[8]]
        )
        self.context = await self.browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        self.page = await self.context.new_page()

    async def _handle_login(self):
        """Realiza login con comportamiento humano [[1]]"""
        try:
            await self.page.goto("https://www.facebook.com",  timeout=60000)
            await asyncio.sleep(uniform(1.5, 3.5))  # Delay aleatorio [[1]]
            
            await self.safe_click("#email")
            await self.page.keyboard.type(self.email, delay=uniform(50, 150))
            await asyncio.sleep(uniform(0.5, 1.5))
            
            await self.safe_click("#pass")
            await self.page.keyboard.type(self.password, delay=uniform(50, 150))
            await asyncio.sleep(uniform(0.5, 1.5))
            
            await self.safe_click("button[name='login']")
            await self.page.wait_for_load_state("networkidle")
        except Exception as e:
            logging.error(f"Error en login: {e}")
            raise

    async def _bypass_captcha(self):
        """Detecta y maneja CAPTCHA [[1]]"""
        if await self.page.query_selector("#captcha_container"):
            logging.warning("CAPTCHA detectado. Resuelva manualmente en 30 segundos...")
            await asyncio.sleep(30)

    async def _scroll_and_load(self):
        """Simula scroll humano para cargar resultados """
        for _ in range(5):
            await self.page.mouse.wheel(0, uniform(800, 1200))  # Scroll aleatorio
            await asyncio.sleep(uniform(1.0, 2.5))  # Delay variable

    async def search(self, query: str):
        """Ejecuta scraping completo con manejo de errores """
        try:
            async with async_playwright() as self.playwright:
                await self._init_browser()
                await self._handle_login()
                await asyncio.sleep(uniform(2.0, 5.0))  
                await self._bypass_captcha()
                await self.page.goto(f"{self.base_url}?query={query}")
                await self._scroll_and_load()
                
                # Extracción de datos [[3]]
                items = await self.page.query_selector_all("div[aria-label='Colección de artículos de Marketplace']")
                results = []
                
                for item in items:
                    logging.info(item)
                    title = await item.query_selector("span[dir='auto']")
                    price = await item.query_selector("span[aria-label*='Precio']")
                    location = await item.query_selector("span[aria-label*='Ubicación']")
                    link = await item.query_selector("a")
                    
                    product = Product(
                        title=await title.inner_text() if title else "",
                        price=await price.inner_text() if price else "",
                        location=await location.inner_text() if location else "",
                        url=await link.get_attribute("href") if link else ""
                    )
                    results.append(product)
                
                await self.save_results(results)
        except Exception as e:
            logging.error(f"Error en scraping: {e}")
            raise
        finally:
            if hasattr(self, "browser") and self.browser:
                await self.browser.close()  # Cierra navegador incluso si hay errores
                #await self.playwright.stop()  # Añade esto para liberar recursos [[1]]

    async def safe_click(self, selector: str):
        """Realiza clic con reintentos y logging [[2]][[9]]"""
        try:
            await self.page.click(selector)
        except Exception as e:
            logging.warning(f"Fallo en clic, reintento: {e}")
            await asyncio.sleep(uniform(1.5, 3.5))  # Delay aleatorio [[1]]
            await self.safe_click(selector)