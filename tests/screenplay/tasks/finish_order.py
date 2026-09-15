# tests/screenplay/tasks/finish_order.py

from screenpy import Performable
from tests.pages.checkout_page import CheckoutPage


class FinishOrder(Performable):

    def perform_as(self, actor):

        page = CheckoutPage(actor.driver)

        page.finish()

    @staticmethod
    def now():
        return FinishOrder()