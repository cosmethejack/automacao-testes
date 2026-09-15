from screenpy import Resolvable
from tests.pages.inventory_page import InventoryPage


class InventoryPageIsLoaded(Resolvable):

    def resolve(self, actor):
        page = InventoryPage(actor.driver)
        return page.is_loaded()