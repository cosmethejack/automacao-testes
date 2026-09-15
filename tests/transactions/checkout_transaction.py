from guara.transaction import AbstractTransaction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTransaction(AbstractTransaction):
    
    def do(self, **kwargs):
        driver = self._driver 
        wait = WebDriverWait(driver, 10)
        
        botao_checkout = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        driver.execute_script("arguments[0].click();", botao_checkout)
        
        wait.until(EC.url_contains("checkout-step-one.html"))
        
        first_name_field = wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys(kwargs.get("name"))
        driver.find_element(By.ID, "last-name").send_keys(kwargs.get("last"))
        driver.find_element(By.ID, "postal-code").send_keys(kwargs.get("zip_code"))
        
        botao_continue = driver.find_element(By.ID, "continue")
        driver.execute_script("arguments[0].click();", botao_continue)
        
        # A MÁGICA PARA O GUARA FUNCIONAR: Esperar a tela mudar antes de retornar
        wait.until(EC.url_contains("checkout-step-two.html"))
        
        return driver.current_url