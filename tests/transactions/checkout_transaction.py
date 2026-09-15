import time
from guara.transaction import AbstractTransaction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutTransaction(AbstractTransaction):

    def do(self, **kwargs):
        driver = self._driver
        wait = WebDriverWait(driver, 10)

        checkout_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()

        wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

        driver.find_element(
            By.ID, "first-name"
        ).send_keys(kwargs.get("name"))

        driver.find_element(
            By.ID, "last-name"
        ).send_keys(kwargs.get("last"))

        driver.find_element(
            By.ID, "postal-code"
        ).send_keys(kwargs.get("zip_code"))

        time.sleep(1)

        driver.find_element(By.ID, "continue").click()

        return driver.current_url