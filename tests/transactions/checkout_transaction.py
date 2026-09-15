from guara.transaction import AbstractTransaction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTransaction(AbstractTransaction):
    
    def do(self, **kwargs):
        driver = self._driver 
        wait = WebDriverWait(driver, 10)
        
        botao_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        botao_checkout.click()
        
        wait.until(EC.url_contains("checkout-step-one.html"))
        
        first_name_field = wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys(kwargs.get("name"))
        driver.find_element(By.ID, "last-name").send_keys(kwargs.get("last"))
        
        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys(kwargs.get("zip_code"))
        postal_code_field.send_keys(Keys.RETURN) # O pulo do gato!
        
        wait.until(EC.url_contains("checkout-step-two.html"))
        
        return driver.current_url