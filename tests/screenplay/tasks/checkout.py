from screenpy import Performable

from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage


class ProceedToCheckout(Performable):

    def __init__(self, first_name, last_name, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.postal_code = postal_code

    def perform_as(self, actor):

        cart_page = CartPage(actor.driver)
        checkout_page = CheckoutPage(actor.driver)

        cart_page.start_checkout()

        checkout_page.fill_form(
            self.first_name,
            self.last_name,
            self.postal_code,
        )

        checkout_page.continue_checkout()

    @staticmethod
    def with_customer_data(first_name, last_name, postal_code):
        return ProceedToCheckout(
            first_name,
            last_name,
            postal_code,
        )