from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def acessar(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, usuario, senha):
        self.driver.find_element(By.ID, "user-name").send_keys(usuario)
        self.driver.find_element(By.ID, "password").send_keys(senha)
        self.driver.find_element(By.ID, "login-button").click()