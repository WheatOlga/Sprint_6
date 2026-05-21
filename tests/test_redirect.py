
import pytest
import allure

class TestMainPageLogos:
    
    @allure.title("Редирект на главную страницу по клику на лого Самоката")
    def test_samokat_logo_redirect(self, main_page):
        
        with allure.step("Кликнуть по логотипу Самоката"):
            main_page.click_samokat_logo()
            
        with allure.step("Проверить, что главная страница загрузилась"):
            assert main_page.is_main_page_loaded()

    @allure.title("Открытие ya.ru в новой вкладке по клику на лого Яндекса")
    def test_yandex_logo_redirect(self, main_page):
        
        with allure.step("Запомнить дескриптор текущей вкладки"):
            initial_window = main_page.get_current_window_handle()
            windows_before = len(main_page.get_window_handles())
            
        with allure.step("Кликнуть по логотипу Яндекса"):
            main_page.click_yandex_logo()
            
        with allure.step("Дождаться появления новой вкладки"):
            main_page.wait_for_new_window(windows_before + 1)
            
        with allure.step("Переключиться на новую вкладку"):
            new_window = [w for w in main_page.get_window_handles() if w != initial_window][0]
            main_page.switch_to_window(new_window)
            
        with allure.step("Проверить видимость модального окна"):
            assert main_page.is_ya_modal_visible()
        