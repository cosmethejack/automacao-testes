from guara.transaction import AbstractTransaction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTransaction(AbstractTransaction):
    
    def do(self, **kwargs):
        # O self._driver fica AQUI DENTRO, onde o 'self' existe!
        driver = self._driver
        wait = WebDriverWait(driver, 10)
        
        # 1. Aguarda o botão da mochila carregar após o login e clica
        botao_mochila = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        botao_mochila.click()
        
        # 2. Aguarda o ícone do carrinho ficar clicável e clica
        carrinho = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        carrinho.click()
        
        # Retorna a URL atual para a validação do framework Guara
        return driver.current_url