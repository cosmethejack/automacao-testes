from guara.transaction import AbstractTransaction
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage


class CheckoutTransaction(AbstractTransaction):

    def do(self, **kwargs):
        cart_page = CartPage(self._driver)
        cart_page.start_checkout()

        checkout_page = CheckoutPage(self._driver)
        checkout_page.fill_form(
            name=kwargs.get("name"),
            last=kwargs.get("last"),
            zip_code=kwargs.get("zip_code")
        )
        checkout_page.continue_checkout()

        return self._driver.current_url