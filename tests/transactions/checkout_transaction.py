# 1. Estas são as importações que estavam faltando!
from guara.transaction import AbstractTransaction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 2. A sua classe agora vai reconhecer o AbstractTransaction
class CheckoutTransaction(AbstractTransaction):
    
    def do(self, **kwargs):
        driver = self._driver
        wait = WebDriverWait(driver, 10)
        
        driver.find_element(By.ID, "checkout").click()
        
        # Clicar no botão de Checkout
        driver.find_element(By.ID, "checkout").click()
        
        # Esperar a página carregar buscando o first-name
        first_name_field = wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        
        # Preencher os dados
        first_name_field.send_keys(kwargs.get("name"))
        driver.find_element(By.ID, "last-name").send_keys(kwargs.get("last"))
        driver.find_element(By.ID, "postal-code").send_keys(kwargs.get("zip_code"))
        
        driver.find_element(By.ID, "continue").click()
        
        return driver.current_url