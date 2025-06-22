from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.webkit.launch(headless=False)
    page = browser.new_page()

    # Paso 1: Navegar a la página principal de Playwright
    page.goto("https://playwright.dev/")
    page.wait_for_selector("h1") # Espera que el H1 de la página principal aparezca
    print("Page title (main):", page.title())

    # Paso 2: Navegar a la página de documentación de introducción
    # page.goto() ya espera la carga principal de la página.
    page.goto("https://playwright.dev/python/docs/intro")

    # En lugar de esperar una respuesta de red específica,
    # espera por un elemento que confirme que la página de docs/intro se cargó.
    # Por ejemplo, el título de la documentación o el primer encabezado.
    # Puedes inspeccionar la página para encontrar un selector adecuado.
    # Por ejemplo, un <h1> dentro de la sección de contenido de la documentación
    page.wait_for_selector("article h1") # Espera el H1 dentro de la sección de artículo
    print("Page title (docs intro):", page.title())
    print("Data loaded (confirmed by element on docs page)")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)