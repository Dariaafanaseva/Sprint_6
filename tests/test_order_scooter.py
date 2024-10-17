import pytest
from selenium import webdriver
from pages.make_order_page import OrderPage


class TestOrderScooter:
    def test_make_order_button_on_header(self, driver):
        order_page = OrderPage(driver)
        order_page.get(("https://qa-scooter.praktikum-services.ru/"))
        order_page.make_order_button_on_header(name='Дарья', surname='Петрова', address='Ленина 1', telephone='89998887744')
        expected_result = 'Посмотреть статус'
        actual_result = order_page.check_order()
        assert actual_result == expected_result, f"Ожидаемый результат: '{expected_result}', но получен: '{actual_result}'"

    def test_make_order_button_on_down(self, driver):
        order_page = OrderPage(driver)
        order_page.get(("https://qa-scooter.praktikum-services.ru/"))
        order_page.make_order_button_on_down(name='Дарья', surname='Петрова', address='Ленина 1', telephone='89998887744')
        expected_result = 'Посмотреть статус'
        actual_result = order_page.check_order()
        assert actual_result == expected_result, f"Ожидаемый результат: '{expected_result}', но получен: '{actual_result}'"