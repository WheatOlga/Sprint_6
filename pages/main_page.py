
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage): 
    def __init__(self, driver):
        super().__init__(driver) 

    @allure.step("Скроллить до последнего вопроса")
    def scroll_to_last_question(self):
        try:
            last_question = self.find_element(MainPageLocators.QUESTION_LOCATORS[8])
            self.execute_script("arguments[0].scrollIntoView(true);", last_question)
        except Exception:
            pass

    @allure.step("Клик по вопросу")
    def click_question(self, question_number: int):
        question_locator = MainPageLocators.QUESTION_LOCATORS[question_number]
        
        question = self.wait_for_clickable(question_locator)
        
        self.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", 
            question
        )
        self.execute_script("arguments[0].click();", question)

    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text(self, question_number: int) -> str:
        answer_locator = MainPageLocators.ANSWERS_LOCATORS[question_number]
        answer = self.wait_for_visible(answer_locator)
        return answer.text
    
    @allure.step("Клик по логотипу Самоката")
    def click_samokat_logo(self):
        self.find_element(MainPageLocators.LOGO_SAMOKAT).click()
    
    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.find_element(MainPageLocators.LOGO_YANDEX).click()
    
    @allure.step("Проверить загрузку главной страницы")
    def is_main_page_loaded(self):
        try:
            self.wait_for_visible(MainPageLocators.HOME_HEADER)
            return True
        except Exception:
            return False
        
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Ожидание появления нового окна")
    def wait_for_new_window(self, expected_count: int):
        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(expected_count)
        )

    def switch_to_window(self, handle: str):
        self.driver.switch_to.window(handle)

    @allure.step("Проверка видимости модального окна на ya.ru")
    def is_ya_modal_visible(self) -> bool:
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(MainPageLocators.YA_MODAL_WINDOW)
        )
        return True