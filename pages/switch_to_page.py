import allure
from pages.base_page import BasePage
from locators.switch_locators import SwitchToPageLocators
from locators.make_order_locators import MakeOrderLocators
from locators.main_page_locators import MainPageLocators

class SwitchToPage(BasePage):
    @allure.step('Переходим на страницу самоката')
    def get(self, url):
        self.driver.get(url)

    @allure.step('Переходим на страницу самоката, при нажатии на лого самоката')
    def switch_to_scooter_main_page(self):
        self.accept_cookies(MakeOrderLocators.COOKIE_BUTTON)
        self.click_to_element(MainPageLocators.MAKE_ORDER_BUTTON_ON_HEADER)
        self.find_element_with_wait(SwitchToPageLocators.HEADER_LOGO_SCOOTER)
        self.switch_to.window(self.window_handles[-1])


    @allure.step('Проверяем наличие кнопки "заказать" на главной странице')
    def find_element_main_page(self):
        self.find_element_with_wait(MainPageLocators.MAKE_ORDER_BUTTON_ON_HEADER)




