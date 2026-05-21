
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage
from urls import Urls
from pages.order_page import OrderPage

@pytest.fixture(scope="session")
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1240")
    firefox_options.add_argument("--height=756")

    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    driver.get(Urls.URL_MAIN_PAGE)
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)
