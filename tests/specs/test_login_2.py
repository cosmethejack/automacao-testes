from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_continuar_comprando_apos_adicionar_item(driver):
    wait = WebDriverWait(driver, 10)

    # 1. LOGIN
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. ADICIONAR ITEM AO CARRINHO
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    # 3. IR AO CARRINHO
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart.html"))

    # 4. CLICAR EM CONTINUAR COMPRANDO
    wait.until(EC.element_to_be_clickable((By.ID, "continue-shopping"))).click()

    # 5. VALIDAR RETORNO À TELA DE INVENTÁRIO
    wait.until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url