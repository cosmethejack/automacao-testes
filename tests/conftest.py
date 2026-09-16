import pytest
from selenium import webdriver


def create_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    return options


def driver_func():
    options = create_chrome_options()
    return webdriver.Chrome(options=options)


@pytest.fixture
def driver():
    browser = driver_func()
    yield browser
    browser.quit()