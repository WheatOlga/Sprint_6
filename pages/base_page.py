
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Ожидать кликабельность элемента")
    def wait_for_clickable(self, locator, timeout=None):
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидать видимость элемента")
    def wait_for_visible(self, locator, timeout=None):
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидать присутствие элемента")
    def wait_for_present(self, locator, timeout=None):
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Закрыть попап с куки")
    def close_cookie_popup(self):
        try:
            # Используем наш новый метод wait_for_clickable
            cookie_button = self.wait_for_clickable((By.ID, "rcc-confirm-button"), timeout=3)
            self.execute_script("arguments[0].click();", cookie_button)
        except TimeoutException:
            pass
        except Exception:
            pass
