
import pytest
from data import ORDER_DATA_SETS
from pages.order_page import OrderPage

@pytest.mark.parametrize("order_data", ORDER_DATA_SETS)
def test_positive_order_flow(main_page, order_data):
    main_page.close_cookie_popup()
    
    order_page = OrderPage(main_page.driver)
    
    order_page.click_order_button(order_data["entry_point"])
    
    order_page.fill_step_1(order_data)
    order_page.click_next()
    order_page.fill_step_2(order_data)
    
    order_page.click_submit()
    order_page.confirm_order()
    
    assert order_page.is_success_popup_visible()
    