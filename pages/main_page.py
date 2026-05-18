
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
    
    @allure.step("Звкрыть попап с куки")
    def close_cookie_popup(self):
        try:
            cookie_button = self.driver.find_element(By.ID, "rcc-confirm-button")
            cookie_button.click()
        except:
            pass
    
    @allure.step("Проскроллить до последнего вопроса")
    def scroll_to_last_question(self):
        try:
            last_question = self.driver.find_element(*MainPageLocators.QUESTION_LOCATORS[8])
            self.driver.execute_script("arguments[0].scrollIntoView(true);", last_question)
        except:
            pass

    @allure.step("Клик на вопрос")
    def click_question(self, question_number: int):
        question_locator = MainPageLocators.QUESTION_LOCATORS[question_number]
        
        question = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(question_locator)
        )
        
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", 
            question
        )
        
        self.driver.execute_script("arguments[0].click();", question)

    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text(self, question_number: int) -> str:
        answer_locator = MainPageLocators.ANSWERS_LOCATORS[question_number]
        
        answer = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(answer_locator)
        )
        return answer.text
    
    @allure.step("Кликнуть на логотип Самоката")
    def click_samokat_logo(self):
        self.find_element(MainPageLocators.LOGO_SAMOKAT).click()
    
    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.find_element(MainPageLocators.LOGO_YANDEX).click()
    
    @allure.step("Проверить загрузку главной страницы")
    def is_main_page_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.HOME_HEADER)
            )
            return True
        except:
            return False
        