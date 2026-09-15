import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver

def test_compra_produto_com_sucesso(driver):
    wait = WebDriverWait(driver, 10)

    # 1. LOGIN
    driver.get("https://www.saucedemo.com/")
    campo_usuario = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    campo_usuario.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. ADICIONAR PRODUTO
    botao_mochila = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    driver.execute_script("arguments[0].click();", botao_mochila)

    # 3. IR PARA CARRINHO E CHECKOUT
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart.html"))
    
    botao_checkout = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
    driver.execute_script("arguments[0].click();", botao_checkout)

    # 4. PREENCHER DADOS E CONTINUAR
    campo_nome = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    campo_nome.send_keys("Damião")
    driver.find_element(By.ID, "last-name").send_keys("Barbosa")
    driver.find_element(By.ID, "postal-code").send_keys("30642-290")
    
    # Clique JS no Continue e espera a tela mudar
    botao_continue = driver.find_element(By.ID, "continue")
    driver.execute_script("arguments[0].click();", botao_continue)
    wait.until(EC.url_contains("checkout-step-two.html"))
    
    # 5. FINALIZAR COMPRA
    botao_finish = wait.until(EC.presence_of_element_located((By.ID, "finish")))
    driver.execute_script("arguments[0].click();", botao_finish)

    # 6. VALIDAÇÃO FINAL
    mensagem = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert mensagem.is_displayed()
    assert "Thank you" in mensagem.text