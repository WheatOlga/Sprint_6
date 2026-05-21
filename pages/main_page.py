
import allure
from selenium.webdriver.common.by import By
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
    def is_main_page_loaded(self) -> bool:
        try:
            self.wait_for_visible(MainPageLocators.HOME_HEADER)
            return True
        except Exception:
            return False

    @allure.step("Ожидание появления нового окна")
    def wait_for_new_window(self, expected_count: int):
        self.wait_for_windows_count(expected_count)

    
    @allure.step("Проверка видимости модального окна на ya.ru")
    def is_ya_modal_visible(self) -> bool:
        try:
            self.wait_for_visible(MainPageLocators.YA_MODAL_WINDOW)
            return True
        except Exception:
            return False
    