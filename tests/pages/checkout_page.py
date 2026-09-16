from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def fill_form(self, name, last, zip_code):
        self.type(*self.FIRST_NAME, name)
        self.type(*self.LAST_NAME, last)
        self.type(*self.POSTAL_CODE, zip_code)

    def continue_checkout(self):
        self.click(*self.CONTINUE_BTN)
        self.wait.until(EC.url_contains("checkout-step-two.html"))

    def finish(self):
        self.click(*self.FINISH_BTN)
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG))

    def get_success_message(self):
        return self.get_text(*self.SUCCESS_MSG)

    def is_order_completed(self):
        return "THANK YOU FOR YOUR ORDER" in self.get_success_message().upper()