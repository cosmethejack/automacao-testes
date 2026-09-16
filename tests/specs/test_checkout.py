from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage


def test_compra_produto_com_sucesso(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. LOGIN
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_loaded()

    # 2. ADICIONAR PRODUTO E IR AO CARRINHO
    inventory_page.add_product()
    inventory_page.go_to_cart()

    # 3. INICIAR CHECKOUT
    cart_page.start_checkout()

    # 4. PREENCHER DADOS
    checkout_page.fill_form("Damiao", "Barbosa", "30642")
    checkout_page.continue_checkout()

    # 5. FINALIZAR COMPRA
    checkout_page.finish()

    # 6. VALIDAR MENSAGEM DE SUCESSO
    assert checkout_page.is_order_completed()