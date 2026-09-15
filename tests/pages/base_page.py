from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def find_all(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        self.find(by, value).click()

    def type(self, by, value, text):
        elemento = self.find(by, value)
        elemento.clear()
        elemento.send_keys(text)

    def get_text(self, by, value):
        return self.find(by, value).text

    def is_visible(self, by, value):
        try:
            return self.find(by, value).is_displayed()
        except Exception:
            return False

    def wait_element_visible(self, by, value):
        return self.wait.until(
            EC.visibility_of_element_located((by, value))
        )

    def wait_element_clickable(self, by, value):
        return self.wait.until(
            EC.element_to_be_clickable((by, value))
        )

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url