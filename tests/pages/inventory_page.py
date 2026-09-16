from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def is_loaded(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_CONTAINER)
        ).is_displayed()

    def add_product(self):
        self.click(*self.ADD_BACKPACK)

    def go_to_cart(self):
        self.click(*self.CART)
        self.wait.until(EC.url_contains("cart.html"))
