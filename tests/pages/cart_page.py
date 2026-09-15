from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CartPage(BasePage):

    def start_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one")
        )