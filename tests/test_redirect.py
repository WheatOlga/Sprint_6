
import pytest
from locators.main_page_locators import MainPageLocators


class TestMainPageLogos:
    
    def test_samokat_logo_redirect(self, main_page):
        main_page.click_samokat_logo()
        assert main_page.is_main_page_loaded()

    def test_yandex_logo_redirect(self, main_page):
        initial_window = main_page.get_current_window_handle()
        windows_before = len(main_page.get_window_handles())
        
        main_page.click_yandex_logo()
        main_page.wait_for_new_window(windows_before + 1)
        
        new_window = [w for w in main_page.get_window_handles() if w != initial_window][0]
        main_page.switch_to_window(new_window)
        
        assert main_page.is_ya_modal_visible()
        