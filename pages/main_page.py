import allure
import pytest

from page_object.pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.make_order_locators import MakeOrderLocators
from pages.main_page import MainPage


class OrderPage(BasePage):

    @allure.step('Создаем заказ')
    def set_order(self, station_locator, name_locator, name,
                  last_name, address, time, button_locator):
        self.click_to_element(MainPageLocators.MAKE_ORDER_BUTTON_ON_HEADER)
        self.add_text_to_element(MakeOrderLocators.NAME_INPUT_FIELD, 'Дарья')
        self.add_text_to_element(MakeOrderLocators.SURNAME_INPUT_FIELD, 'Афанасьева')
        self.add_text_to_element(MakeOrderLocators.ADDRESS_INPUT_FIELD, 'Ленина 1')
        self.cli
        self.click_to_element(time)
        self.click_to_element(button_locator)

    @allure.step('Проверяем, что заказ создался')
    def check_order(self, locator):
        return self.get_text_from_element(locator)

class TestMainPage:



