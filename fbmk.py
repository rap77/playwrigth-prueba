import asyncio
from playwright.async_api import async_playwright
from dataclasses import dataclass
import random
from typing import List
import sqlite3
conn = sqlite3.connect("marketplace.db")


@dataclass
class Listing:
    title: str
    price: str
    location: str
    url: str

class FacebookMarketplaceScraper:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.base_url = "https://www.facebook.com/marketplace/category/vehicles" 
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"
        ]

    async def _init_browser(self):
        """Inicializa navegador con configuración anti-detección"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
            proxy={"server": "http://user:pass@proxy-ip:port"}  # Proxy rotativo [[2]]
        )
        self.context = await self.browser.new_context(
            user_agent=random.choice(self.user_agents),
            viewport={"width": 1280, "height": 800},
            extra_http_headers={"Accept-Language": "es-ES,en;q=0.9"}
        )
        self.page = await self.context.new_page()

    async def _handle_login(self):
        """Realiza login con comportamiento humano"""
        await self.page.goto("https://www.facebook.com") 
        await asyncio.sleep(random.uniform(1.5, 3.5))
        
        # Simulación de tipeo humano
        await self.page.type("#email", self.email, delay=random.randint(100, 200))
        await asyncio.sleep(random.uniform(0.5, 1.5))
        await self.page.type("#pass", self.password, delay=random.randint(100, 200))
        await asyncio.sleep(random.uniform(0.5, 1.5))
        
        await self.page.click("button[name='login']")
        await self.page.wait_for_load_state("networkidle")

    async def _bypass_captcha(self):
        """Detecta y maneja CAPTCHA (requiere intervención humana)"""
        if await self.page.query_selector("#captcha_container"):
            print("CAPTCHA detectado. Resuelva manualmente en 30 segundos...")
            await asyncio.sleep(30)  # Espera para resolución manual

    async def _scroll_and_load(self):
        """Simula scroll humano para cargar todos los resultados"""
        for _ in range(5):  # Ajustar según necesidades
            await self.page.mouse.wheel(0, random.randint(800, 1200))  # Scroll aleatorio
            await asyncio.sleep(random.uniform(1, 2.5)) # Pausa entre scrolls

    async def search(self, query: str) -> List[Listing]:
        """Realiza búsqueda y extrae resultados"""
        await self._init_browser() # Con proxy rotativo [[1]]
        await self._handle_login()
        await self._bypass_captcha() # Manejo de CAPTCHA [[1]]
        
        # Navegar a la búsqueda
        await self.page.goto(f"{self.base_url}?query={query}")
        await self._scroll_and_load() # Scroll humano [[1]]
        
        # Extracción de datos
        listings = []
        items = await self.page.query_selector_all("div[aria-label='Lista de resultados']")
        results = []
        for item in items:
            title = await item.query_selector("span[dir='auto']")
            price = await item.query_selector("span[aria-label*='Precio']")
            location = await item.query_selector("span[aria-label*='Ubicación']")
            
            listings.append(Listing(
                title=await title.inner_text() if title else "",
                price=await price.inner_text() if price else "",
                location=await location.inner_text() if location else "",
                url=await item.query_selector("a").get_attribute("href")
            ))
            results.append(Listing(...))
            
        await self.browser.close()
        return listings
            

    async def safe_click(self, selector):
        try:
            await self.page.click(selector)
        except:
            await asyncio.sleep(2)
            await self.safe_click(selector)  # Retry

# Uso del scraper
async def main():
    scraper = FacebookMarketplaceScraper(
        email="rafael.padron773@proton.me",
        password="@Rp230594.Facebook@"
    )
    results = await scraper.search("corolla 2018")
    print(f"Se encontraron {len(results)} resultados")

asyncio.run(main())