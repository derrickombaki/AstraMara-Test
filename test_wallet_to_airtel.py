import pytest
from pages.send_money_page import SendMoneyPage
from config.utility import UtilityMethods
from pages.home_page import HomePage

# Load test data
data = UtilityMethods.get_data_by_keys("airtel_money")

@pytest.mark.usefixtures("app_driver")
class TestWalletToAirtel:

    def test_send_to_airtel_money(self, app_driver):
        home_page = HomePage(app_driver)
        send_page = SendMoneyPage(app_driver)

        home_page.click_send_button()
        send_page.select_mobile_money()
        send_page.select_other_number()

        send_page.enter_mobile_number(data["airtel_number"])
        send_page.enter_mobile_amount(data["amount"])
        send_page.continue_mobile_transfer()
        send_page.enter_purpose(data["purpose"])
        send_page.click_send_money()
        send_page.enter_passcode(data["passcode"])
        send_page.click_verify()
        send_page.click_done()

    def test_send_to_airtel_money_different_amount(self, app_driver):
        home_page = HomePage(app_driver)
        send_page = SendMoneyPage(app_driver)

        home_page.click_send_button()
        send_page.select_mobile_money()
        send_page.select_other_number()

        send_page.enter_mobile_number(data["airtel_number"])
        send_page.enter_mobile_amount("amount1")  # Different amount
        send_page.continue_mobile_transfer()
        send_page.enter_purpose(data["purpose"])
        send_page.click_send_money()
        send_page.enter_passcode(data["passcode"])
        send_page.click_verify()
        send_page.click_done()
