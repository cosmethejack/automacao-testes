from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage


def test_continuar_comprando_apos_adicionar_item(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # 1. LOGIN
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_loaded()

    # 2. ADICIONAR ITEM AO CARRINHO E IR AO CARRINHO
    inventory_page.add_product()
    inventory_page.go_to_cart()

    # 3. CLICAR EM CONTINUAR COMPRANDO
    cart_page.continue_shopping()

    # 4. VALIDAR RETORNO À TELA DE INVENTÁRIO
    assert inventory_page.is_loaded()
    assert "inventory.html" in driver.current_url