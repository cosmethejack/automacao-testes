def test_compra_produto_com_sucesso(driver):
    wait = WebDriverWait(driver, 10)

    # 1. LOGIN
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. ADICIONAR PRODUTO
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # 3. IR PARA CARRINHO E CHECKOUT
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # CORREÇÃO: Em vez de checar a URL, esperamos o botão de checkout ficar clicável
    botao_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    botao_checkout.click()

    # 4. PREENCHER DADOS
    # Esperamos o campo de nome ficar visível
    campo_nome = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    campo_nome.send_keys("Damião")
    
    driver.find_element(By.ID, "last-name").send_keys("Barbosa")
    driver.find_element(By.ID, "postal-code").send_keys("30642-290")
    driver.find_element(By.ID, "continue").click()
    
    # 5. FINALIZAR COMPRA
    # Esperamos o botão finish ficar clicável
    botao_finish = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    botao_finish.click()

    # 6. VALIDAÇÃO FINAL
    mensagem = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert mensagem.is_displayed()
    assert "Thank you" in mensagem.text