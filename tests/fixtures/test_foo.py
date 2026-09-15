from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def test_navegacao():
    # Inicializa o ChromeDriver automaticamente - Browser
    driver = webdriver.Chrome() 

    try:
        # 1. Abre a URL inicial
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        time.sleep(2)  # Pausa apenas para você visualizar a ação

        driver.find_element(By.ID, "my-text-id").send_keys("foo")

        #botao_submit = driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[2]/button[@type='submit']")
        #botao_submit.click()
        
        driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[2]/button").click()
        time.sleep(80)


    finally:
        # Fecha o navegador e encerra o processo
        driver.quit()
