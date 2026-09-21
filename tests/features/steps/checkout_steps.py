from behave import given, when, then
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage


@given("que o usuário está logado na aplicação")
def step_user_logged_in(context):
    context.login_page = LoginPage(context.driver)
    context.inventory_page = InventoryPage(context.driver)
    context.login_page.open("https://www.saucedemo.com/")
    context.login_page.login("standard_user", "secret_sauce")
    assert context.inventory_page.is_loaded()


@given("que o usuário adiciona um produto ao carrinho")
def step_add_product_to_cart(context):
    if not hasattr(context, "inventory_page"):
        context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.add_product()


@given("que o usuário acessa o carrinho de compras")
def step_access_cart(context):
    if not hasattr(context, "inventory_page"):
        context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.driver)


@when("ele inicia o processo de checkout")
def step_start_checkout(context):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    context.cart_page.start_checkout()
    context.checkout_page = CheckoutPage(context.driver)


@when('ele preenche os dados de entrega com nome "{name}", sobrenome "{last_name}" e CEP "{postal_code}"')
def step_fill_checkout_form(context, name, last_name, postal_code):
    if not hasattr(context, "checkout_page"):
        context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.fill_form(name, last_name, postal_code)
    context.checkout_page.continue_checkout()


@when("ele confirma e finaliza o pedido")
def step_finish_order(context):
    if not hasattr(context, "checkout_page"):
        context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.finish()


@then('a mensagem de sucesso "{expected_message}" deve ser exibida')
def step_verify_order_success(context, expected_message):
    if not hasattr(context, "checkout_page"):
        context.checkout_page = CheckoutPage(context.driver)
    success_msg = context.checkout_page.get_success_message()
    assert expected_message.upper() in success_msg.upper(), (
        f"Esperado '{expected_message}', mas obteve '{success_msg}'"
    )
