from guara.transaction import AbstractTransaction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTransaction(AbstractTransaction):
    
    def do(self, driver, kwargs):
        wait = WebDriverWait(driver, 10)
        
        # 1. Clicar no botão de Checkout que está na página do carrinho
        driver.find_element(By.ID, "checkout").click()
        
        # 2. Esperar a página do formulário carregar buscando o first-name
        first_name_field = wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        
        # 3. Preencher os dados
        first_name_field.send_keys(kwargs.get("name"))
        driver.find_element(By.ID, "last-name").send_keys(kwargs.get("last"))
        driver.find_element(By.ID, "postal-code").send_keys(kwargs.get("zip_code"))
        
        # 4. Clicar em continuar
        driver.find_element(By.ID, "continue").click()
        
        # Retorna a URL atual para as asserções (.asserts) no Guara
        return driver.current_url