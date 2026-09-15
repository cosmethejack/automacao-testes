# Certifique-se de ter os imports:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Dentro do método que clica na mochila:
wait = WebDriverWait(self.driver, 10)
botao_mochila = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
botao_mochila.click()

# Se você clica no carrinho na mesma transação, espere ele ficar clicável também:
carrinho = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
carrinho.click()