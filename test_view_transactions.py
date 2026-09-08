import os
from pages.home_page import HomePage
from tests.conftest import driver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("driver")
def test_view_transaction(driver):

    home_page = HomePage(driver)
    home_page.click_see_more()

