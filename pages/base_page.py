from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):

        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def close_cookie_popup(self):

        try:
            cookie_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            self.driver.execute_script("arguments[0].click();", cookie_button)
        except:
            pass
        