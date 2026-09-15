from screenpy import Resolvable

from tests.pages.checkout_page import CheckoutPage


class OrderCompleted(Resolvable):

    def resolve(self, actor):

        page = CheckoutPage(actor.driver)

        return page.is_order_completed()