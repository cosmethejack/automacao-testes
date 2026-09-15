import time
 
from tests.fixtures.driver import driver
from selenium.webdriver.common.by import By
 
 
# =========================================================
# CENÁRIO - CONTINUAR COMPRANDO APÓS ADICIONAR ITEM
# =========================================================
 
def test_continuar_comprando_apos_adicionar_item(driver):
 
    # =========================
    # 1. LOGIN
    # =========================
    driver.get("https://www.saucedemo.com")
    time.sleep(2)
 
    driver.find_element(
        By.ID,
        "user-name"
    ).send_keys("standard_user")
    time.sleep(1)
 
    driver.find_element(
        By.ID,
        "password"
    ).send_keys("secret_sauce")
    time.sleep(1)