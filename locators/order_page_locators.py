from selenium.webdriver.common.by import By

class OrderPageLocators:
    
    # Шаг 1
    HEADER_NAME_FIRST_STEP = (By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and text()='Для кого самокат']")
    INPUT_FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_SUBWAY = (By.CSS_SELECTOR, "input.select-search__input")
    INPUT_PHONE = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    # Шаг 2
    HEADER_NAME_SECOND_STEP = (By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and text()='Про аренду']")
    INPUT_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    DROPDOWN_RENTAL_PERIOD = (By.CSS_SELECTOR, ".Dropdown-control")
    RENTAL_OPTION = (By.CSS_SELECTOR, ".Dropdown-option")
    
    RADIO_COLOR_BLACK = (By.XPATH, "//label[contains(text(), 'чёрный жемчуг')]")
    RADIO_COLOR_GREY = (By.XPATH, "//label[contains(text(), 'серая безысходность')]")
    TEXTAREA_COMMENT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    
    BUTTON_SUBMIT = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    
    # Попап Хотите оформить заказ?
    CONFIRM_MODAL_CONTAINER = (By.CSS_SELECTOR, ".Order_Modal__YZ-d3")
    CONFIRM_MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Хотите оформить заказ?']")
    
    BUTTON_MODAL_NO = (By.XPATH, "//button[text()='Нет']")
    BUTTON_MODAL_YES = (By.XPATH, "//button[text()='Да']")
        
    # Попап успеха
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3') and contains(., 'Заказ оформлен')]")
    SUCCESS_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".Order_Text__2broi")

    BUTTON_CHECK_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")
    