
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

    @allure.step("Найти элементы")
    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
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

    @allure.step("Ожидать количество окон")
    def wait_for_windows_count(self, expected_count, timeout=None):
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(expected_count)
        )
    
    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить дескриптор текущего окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Получить список дескрипторов окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключиться на окно")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step("Закрыть текущее окно")
    def close_window(self):
        self.driver.close()
    
    @allure.step("Скроллить к элементу")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    @allure.step("Закрыть попап с куки")
    def close_cookie_popup(self):
        try:
            cookie_button = self.wait_for_clickable((By.ID, "rcc-confirm-button"), timeout=3)
            self.execute_script("arguments[0].click();", cookie_button)
        except TimeoutException:
            pass
        except Exception:
            pass
