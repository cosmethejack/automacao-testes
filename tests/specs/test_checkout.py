import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    botao_mochila = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
    driver.execute_script("arguments[0].click();", botao_mochila)

    # 3. IR PARA CARRINHO E CHECKOUT
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart.html"))
    
    # [CORREÇÃO AQUI] Clique JS que já havia funcionado antes para sair do carrinho
    botao_checkout = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
    driver.execute_script("arguments[0].click();", botao_checkout)
    
    wait.until(EC.url_contains("checkout-step-one.html"))

    # 4. PREENCHER DADOS E CONTINUAR COM ENTER
    campo_nome = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    campo_nome.send_keys("Damião")
    driver.find_element(By.ID, "last-name").send_keys("Barbosa")
    
    campo_cep = driver.find_element(By.ID, "postal-code")
    campo_cep.send_keys("30642-290")
    campo_cep.send_keys(Keys.RETURN)
    
    wait.until(EC.url_contains("checkout-step-two.html"))
    
    # 5. FINALIZAR COMPRA
    botao_finish = wait.until(EC.presence_of_element_located((By.ID, "finish")))
    driver.execute_script("arguments[0].click();", botao_finish)

    # 6. VALIDAÇÃO FINAL
    mensagem = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert mensagem.is_displayed()
    assert "Thank you" in mensagem.text