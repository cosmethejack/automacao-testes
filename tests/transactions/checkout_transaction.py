class CheckoutTransaction(AbstractTransaction):
    
    # CORREÇÃO: Adicionados os ** antes do kwargs e ajustado o driver
    def do(self, **kwargs):
        # No framework Guara, o driver costuma vir de self.driver
        driver = self.driver 
        wait = WebDriverWait(driver, 10)
        
        # Clicar no botão de Checkout que está na página do carrinho
        driver.find_element(By.ID, "checkout").click()
        
        # Esperar a página do formulário carregar buscando o first-name
        first_name_field = wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        
        # Preencher os dados usando as kwargs
        first_name_field.send_keys(kwargs.get("name"))
        driver.find_element(By.ID, "last-name").send_keys(kwargs.get("last"))
        driver.find_element(By.ID, "postal-code").send_keys(kwargs.get("zip_code"))
        
        driver.find_element(By.ID, "continue").click()
        
        return driver.current_url