import pytest
from pages.home_page import HomePage
from pages.send_money_page import SendMoneyPage
from config.utility import UtilityMethods

@pytest.mark.usefixtures("driver")
def test_send_money_flow(driver):
    # Identify the correct data block by required keys
    required_keys = ["account_number", "amount", "purpose", "passcode"]
    data = UtilityMethods.get_data_by_keys(required_keys)
    assert data is not None, "Send money test data not found"

    home_page = HomePage(driver)
    home_page.click_send_button()
    send_money_page = SendMoneyPage(driver)
    send_money_page.enter_wallet_account(data["account_number"])
    send_money_page.enter_wallet_amount(data["amount"])
    send_money_page.click_continue_wallet_transfer()
    send_money_page.enter_purpose(data["purpose"])
    send_money_page.click_send_money()
    send_money_page.enter_passcode(data["passcode"])
    send_money_page.click_verify()
