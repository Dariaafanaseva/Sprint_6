from pages.switch_to_page import SwitchToPage

class TestSwitchTo:
    def test_to_scooter_main_page(self, driver):
        order_page = OrderPage(driver)
        order_page.get(("https://qa-scooter.praktikum-services.ru/"))
        order_page.switch_to_scooter_main_page()
        order_button_text = order_page.find_element_main_page()
        assert order_button_text