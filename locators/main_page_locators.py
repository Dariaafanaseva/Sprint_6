from selenium.webdriver.common.by import By


class MainPageLocators:
    MAKE_ORDER_BUTTON_ON_HEADER = By.XPATH, '//div[2]/button[contains(text(),"Заказать")]'
    MAKE_ORDER_BUTTON_ON_DOWN = By.XPATH, '//div[5]/button[contains(text(),"Заказать")]'
