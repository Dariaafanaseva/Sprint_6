from selenium.webdriver.common.by import By


class SwitchToPageLocators:
    HEADER_LOGO_SCOOTER = By.XPATH, '//img[@alt="Scooter"]/parent::a'
    HEADER_LOGO_YANDEX = By.XPATH, '// img[ @ alt = "Yandex"]/parent::a'