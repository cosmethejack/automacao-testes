from screenpy import Performable
from tests.pages.inventory_page import InventoryPage


class AddItemToCart(Performable):

    def perform_as(self, actor):
        page = InventoryPage(actor.driver)

        page.add_product()
        page.go_to_cart()

    @staticmethod
    def the_first_item():
        return AddItemToCart()