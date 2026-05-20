from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATORS = {
        1: (By.ID, "accordion__heading-0"),
        2: (By.ID, "accordion__heading-1"),
        3: (By.ID, "accordion__heading-2"),
        4: (By.ID, "accordion__heading-3"),
        5: (By.ID, "accordion__heading-4"),
        6: (By.ID, "accordion__heading-5"),
        7: (By.ID, "accordion__heading-6"),
        8: (By.ID, "accordion__heading-7"),
    }
    
    ANSWERS_LOCATORS = {
        1: (By.ID, "accordion__panel-0"),
        2: (By.ID, "accordion__panel-1"),
        3: (By.ID, "accordion__panel-2"),
        4: (By.ID, "accordion__panel-3"),
        5: (By.ID, "accordion__panel-4"),
        6: (By.ID, "accordion__panel-5"),
        7: (By.ID, "accordion__panel-6"),
        8: (By.ID, "accordion__panel-7"),
    }
    
    HEADER_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]//button[text()='Заказать']")

    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SAMOKAT = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    HOME_HEADER = (By.CLASS_NAME, "Home_Header__iJKdX")
    YA_MODAL_WINDOW = (By.CLASS_NAME, "DistributionSplashScreenModalContent")
