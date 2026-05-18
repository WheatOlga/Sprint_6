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
    
    EXPECTED_ANSWERS = {
        1: "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        2: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        3: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        4: "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        5: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        6: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        7: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        8: "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
    }

    HEADER_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]//button[text()='Заказать']")

    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SAMOKAT = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    HOME_HEADER = (By.CLASS_NAME, "Home_Header__iJKdX")
    YA_MODAL_WINDOW = (By.CLASS_NAME, "DistributionSplashScreenModalContent")
