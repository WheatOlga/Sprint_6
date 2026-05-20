
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException

class OrderPage(BasePage):
    @allure.step("Клик по кнопке Заказать")
    def click_order_button(self, entry_point):
        
        self.close_cookie_popup()
        
        if entry_point == "header":
            locator = MainPageLocators.HEADER_ORDER_BUTTON
        else:
            locator = MainPageLocators.BOTTOM_ORDER_BUTTON
        
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(OrderPageLocators.HEADER_NAME_FIRST_STEP)
        )

    @allure.step("Заполнить первый шаг формы заказа (поля: Имя, Фамиля, Адрес, Метро, Телефон)")
    def fill_step_1(self, data):

        self.find_element(OrderPageLocators.INPUT_FIRST_NAME).send_keys(data["first_name"])
        self.find_element(OrderPageLocators.INPUT_LAST_NAME).send_keys(data["last_name"])
        self.find_element(OrderPageLocators.INPUT_ADDRESS).send_keys(data["address"])

        subway_input = self.find_element(OrderPageLocators.INPUT_SUBWAY)
        subway_input.click()
        subway_input.clear()
        subway_input.send_keys(data["subway"])
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".select-search.has-focus"))
        )
        
        option_xpath = f"//div[contains(@class, 'select-search') and .//text()[contains(., '{data['subway']}')]]"
        
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//*[contains(@class, 'select-search')]//*[contains(text(), '{data['subway']}')]")
            )
        )
        option.click()

        self.find_element(OrderPageLocators.INPUT_PHONE).send_keys(data["phone"])

    @allure.step("Нажать кнопку Далее")
    def click_next(self):

        self.find_element(OrderPageLocators.BUTTON_NEXT).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.HEADER_NAME_SECOND_STEP)
        )

    @allure.step("Заполнить второй шаг формы заказа (поля: Когда привезти самокат, Срок аренды, Цвет самоката, Комментарий курьеру)")
    def fill_step_2(self, data):

        date_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.INPUT_DATE)
        )
        date_input.click()
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".react-datepicker"))
        )
        
        day, month, year = data["date"].split(".")
        day = int(day) 
        
        day_locator = (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and @aria-disabled='false' and contains(@aria-label, '{day}-е')]")
        
        day_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(day_locator)
        )
        day_element.click()

        dropdown = self.find_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD)
        dropdown.click()
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{data['rental_period']}']"))
        )
        option.click()

        self.find_element((By.XPATH, f"//label[contains(text(), '{data['color']}')]")).click()

        self.find_element(OrderPageLocators.TEXTAREA_COMMENT).send_keys(data["comment"])

    @allure.step("Нажать на кнопку Заказать")
    def click_submit(self):

        self.find_element(OrderPageLocators.BUTTON_SUBMIT).click()

    @allure.step("В попапе подтверждения нажать кнопку Да")
    def confirm_order(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.CONFIRM_MODAL_CONTAINER)
        )
        self.find_element(OrderPageLocators.BUTTON_MODAL_YES).click()

    @allure.step("Открывает попап успешного оформления заказа")
    def is_success_popup_visible(self):

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL)
            )
            return True
        except Exception:
            return False
    @allure.step("Выводятся текст Заказ оформлен")
    def get_success_text(self):

        return self.find_element(OrderPageLocators.SUCCESS_HEADER).text
    
    @allure.step("Проверить отображение попапа успеха")
    def is_success_popup_visible(self) -> bool:
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL)
            )
            return element.is_displayed()
        except TimeoutException:
            return False
    