import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class TestMainPageLogos:
    
    def test_samokat_logo_redirect(self, main_page):

        main_page.click_samokat_logo()

        assert main_page.is_main_page_loaded()

    def test_yandex_logo_redirect(self, main_page):
   
        initial_window = main_page.driver.current_window_handle
        all_windows_before = len(main_page.driver.window_handles)
        
        main_page.click_yandex_logo()

        WebDriverWait(main_page.driver, 10).until(
            EC.number_of_windows_to_be(all_windows_before + 1)
        )
        
        new_window_handle = [
            w for w in main_page.driver.window_handles 
            if w != initial_window
        ][0]
        main_page.driver.switch_to.window(new_window_handle)
        
        try:
            WebDriverWait(main_page.driver, 15).until(
                EC.visibility_of_element_located(MainPageLocators.YA_MODAL_WINDOW)
            )
            modal_visible = True
        except:
            modal_visible = False
        
        assert modal_visible
        