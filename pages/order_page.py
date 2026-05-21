import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    
    @allure.step("Клик по кнопке Заказать")
    def click_order_button(self, entry_point):
        self.close_cookie_popup()
        
        if entry_point == "header":
            locator = MainPageLocators.HEADER_ORDER_BUTTON
        else:
            locator = MainPageLocators.BOTTOM_ORDER_BUTTON
        
        element = self.wait_for_clickable(locator)
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.execute_script("arguments[0].click();", element)
        
        self.wait_for_visible(OrderPageLocators.HEADER_NAME_FIRST_STEP, timeout=15)

    @allure.step("Заполнить первый шаг формы заказа")
    def fill_step_1(self, data):
        self.find_element(OrderPageLocators.INPUT_FIRST_NAME).send_keys(data["first_name"])
        self.find_element(OrderPageLocators.INPUT_LAST_NAME).send_keys(data["last_name"])
        self.find_element(OrderPageLocators.INPUT_ADDRESS).send_keys(data["address"])

        subway_input = self.find_element(OrderPageLocators.INPUT_SUBWAY)
        subway_input.click()
        subway_input.clear()
        subway_input.send_keys(data["subway"])
        
        self.wait_for_visible(OrderPageLocators.SUBWAY_OPTIONS_CONTAINER)
        
        subway_option_locator = (
            By.XPATH, 
            OrderPageLocators.SUBWAY_OPTION_TEMPLATE.format(value=data["subway"])
        )
        option = self.wait_for_clickable(subway_option_locator)
        option.click()

        self.find_element(OrderPageLocators.INPUT_PHONE).send_keys(data["phone"])

    @allure.step("Нажать кнопку Далее")
    def click_next(self):
        self.find_element(OrderPageLocators.BUTTON_NEXT).click()
        self.wait_for_visible(OrderPageLocators.HEADER_NAME_SECOND_STEP)

    @allure.step("Заполнить второй шаг формы заказа")
    def fill_step_2(self, data):

        date_input = self.wait_for_clickable(OrderPageLocators.INPUT_DATE)
        date_input.click()
        
        self.wait_for_present(OrderPageLocators.DATEPICKER_CONTAINER)
        
        day, month, year = data["date"].split(".")
        day = int(day)
        
        day_locator = (
            By.XPATH, 
            OrderPageLocators.DATE_DAY_TEMPLATE.format(value=f"{day}-е")
        )
        day_element = self.wait_for_clickable(day_locator)
        day_element.click()

        dropdown = self.find_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD)
        dropdown.click()
        
        option_locator = (
            By.XPATH, 
            OrderPageLocators.RENTAL_OPTION_TEMPLATE.format(value=data["rental_period"])
        )
        option = self.wait_for_clickable(option_locator)
        option.click()

        color_locator = (
            By.XPATH, 
            OrderPageLocators.COLOR_LABEL_TEMPLATE.format(value=data["color"])
        )
        self.find_element(color_locator).click()

        self.find_element(OrderPageLocators.TEXTAREA_COMMENT).send_keys(data["comment"])

    @allure.step("Нажать на финальную кнопку Заказать")
    def click_submit(self):
        self.find_element(OrderPageLocators.BUTTON_SUBMIT).click()

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        self.wait_for_visible(OrderPageLocators.CONFIRM_MODAL_CONTAINER)
        self.find_element(OrderPageLocators.BUTTON_MODAL_YES).click()

    @allure.step("Проверить появление попапа успеха")
    def is_success_popup_visible(self) -> bool:
        try:
            self.wait_for_visible(OrderPageLocators.SUCCESS_MODAL)
            return True
        except Exception:
            return False
    
    @allure.step("Получить текст заголовка успеха")
    def get_success_text(self) -> str:
        return self.get_text(OrderPageLocators.SUCCESS_HEADER)