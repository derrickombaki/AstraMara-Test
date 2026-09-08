# tests/test_send_money.py
from pages.home_page import HomePage
from tests.conftest import driver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("driver")
def test_click_send_button(driver):

    home_page = HomePage(driver)
    home_page.click_send_button()

