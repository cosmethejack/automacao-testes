from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    def start_checkout(self):
        self.click(*self.CHECKOUT_BTN)
        self.wait.until(EC.url_contains("checkout-step-one.html"))

    def continue_shopping(self):
        self.click(*self.CONTINUE_SHOPPING_BTN)
        self.wait.until(EC.url_contains("inventory.html"))