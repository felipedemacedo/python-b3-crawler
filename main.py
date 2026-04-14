from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    return driver


def normalize_label(text):
    normalized = " ".join(text.upper().replace("\n", " ").split())
    return normalized.replace("HELP_OUTLINE", "").strip()


def clean_value(text):
    return " ".join(text.split()).replace("help_outline", "").strip()


def extract_indicator_map(driver):
    indicators = {}

    for info in driver.find_elements(By.CSS_SELECTOR, ".top-info .info"):
        titles = [
            normalize_label(el.text)
            for el in info.find_elements(By.CSS_SELECTOR, ".title, .sub-title")
            if el.text.strip()
        ]
        values = [
            clean_value(el.text)
            for el in info.find_elements(By.CSS_SELECTOR, ".value, .sub-value")
            if el.text.strip() and "arrow_" not in el.text
        ]

        for title, value in zip(titles, values):
            indicators[title] = value

    return indicators


def get_fii_data(ticker):
    driver = create_driver()
    data = {"ticker": ticker}
    url = f"https://statusinvest.com.br/fundos-imobiliarios/{ticker.lower()}"

    try:
        driver.get(url)

        WebDriverWait(driver, 15).until(
            lambda d: "cloudflare" not in d.title.lower()
            and len(d.find_elements(By.CSS_SELECTOR, ".top-info .info")) > 0
        )

        indicators = extract_indicator_map(driver)
        data["preco"] = indicators.get("VALOR ATUAL")
        data["pvp"] = indicators.get("P/VP")
        data["dy"] = indicators.get("DIVIDEND YIELD")

        if not any([data.get("preco"), data.get("pvp"), data.get("dy")]):
            data["erro"] = "Indicadores nao encontrados na pagina."
    except TimeoutException:
        data["erro"] = (
            "A pagina nao carregou os indicadores a tempo ou o acesso foi bloqueado."
        )
    except Exception as e:
        data["erro"] = f"Erro ao buscar dados: {e}"
    finally:
        driver.quit()

    return data


for fii in ["BRCO11","BTHF11","CACR11","HSML11","MFII11","MXRF11","RBRX11","RZAT11","XPLG11","XPML11","HGLG11"]:
    print(get_fii_data(fii))
