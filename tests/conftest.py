import os
from datetime import datetime
import pytest
import allure
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver_instance = item.funcargs.get("driver", None)
        if driver_instance:
            try:
                os.makedirs("reports/screenshots", exist_ok=True)
                screenshot_bytes = driver_instance.get_screenshot_as_png()
                allure.attach(
                    screenshot_bytes,
                    name=f"Evidencia_Falha_Pytest_{item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"failed_pytest_{timestamp}_{item.name[:30]}.png"
                file_path = os.path.join("reports", "screenshots", file_name)
                with open(file_path, "wb") as f:
                    f.write(screenshot_bytes)
            except Exception as e:
                print(f"Erro ao capturar screenshot no Pytest: {e}")