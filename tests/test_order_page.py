
import pytest
import allure
from data import ORDER_DATA_SETS
from pages.order_page import OrderPage

class TestOrderFlow:
    
    @allure.title("Оформление заказа: точка входа - {order_data[entry_point]}")
    @pytest.mark.parametrize("order_data", ORDER_DATA_SETS)
    def test_positive_order_flow(self, main_page, order_data):
        
        with allure.step("Закрыть попап с куки"):
            main_page.close_cookie_popup()
            
        with allure.step("Инициализировать объект страницы заказа"):
            order_page = OrderPage(main_page.driver)
            
        with allure.step(f"Кликнуть по кнопке 'Заказать' ({order_data['entry_point']})"):
            order_page.click_order_button(order_data["entry_point"])
            
        with allure.step("Заполнить контакты (Шаг 1)"):
            order_page.fill_step_1(order_data)
            
        with allure.step("Нажать кнопку 'Далее'"):
            order_page.click_next()
            
        with allure.step("Заполнить параметры аренды (Шаг 2)"):
            order_page.fill_step_2(order_data)
            
        with allure.step("Нажать финальную кнопку 'Заказать'"):
            order_page.click_submit()
            
        with allure.step("Подтвердить заказ в модальном окне"):
            order_page.confirm_order()
            
        with allure.step("Проверить появление окна успеха"):
            assert order_page.is_success_popup_visible(), "Окно успеха не отобразилось"
    