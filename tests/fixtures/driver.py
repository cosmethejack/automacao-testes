import tempfile
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():
    driver = driver_func()

    yield driver

    driver.quit()


def driver_func():

    chrome_options = Options()

    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }

    chrome_options.add_experimental_option("prefs", prefs)

    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    chrome_options.add_argument("--safebrowsing-disable-leak-detection")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.maximize_window()

    return driver