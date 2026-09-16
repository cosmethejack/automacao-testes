from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_all(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        elemento = self.wait.until(EC.element_to_be_clickable((by, value)))
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)
        except Exception:
            pass
        self.driver.execute_script("arguments[0].click();", elemento)

    def type(self, by, value, text):
        elemento = self.wait.until(EC.visibility_of_element_located((by, value)))
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)
            self.driver.execute_script("arguments[0].focus();", elemento)
        except Exception:
            pass

        try:
            self.driver.execute_script("""
                const elem = arguments[0];
                const val = arguments[1];
                const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                if (nativeSetter) {
                    nativeSetter.call(elem, val);
                } else {
                    elem.value = val;
                }
                elem.dispatchEvent(new Event('input', { bubbles: true }));
                elem.dispatchEvent(new Event('change', { bubbles: true }));
            """, elemento, str(text))
        except Exception:
            elemento.clear()
            elemento.send_keys(str(text))

    def get_text(self, by, value):
        elemento = self.wait.until(EC.visibility_of_element_located((by, value)))
        return elemento.text

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