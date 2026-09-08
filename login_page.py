from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    # Locators
    DENY_BTN = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")
    LETS_DO_THIS_BTN = (AppiumBy.XPATH, '//android.widget.TextView[@text="Let’s Do This"]')
    PHONE_FIELD = (AppiumBy.XPATH, "//*[@resource-id='btn-phoneNumberInput']")
    CONTINUE_BTN = (AppiumBy.XPATH, '//android.widget.TextView[@text="Continue"]/..')
    PIN_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='input-login-pin']")
    LOGIN_BTN = (AppiumBy.XPATH, '//android.view.ViewGroup[@index="11"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Actions
    def deny_permission(self):
        self.click(self.DENY_BTN, timeout=5)

    def click_lets_do_this(self):
        self.click(self.LETS_DO_THIS_BTN, timeout=15)

    def enter_phone(self, phone_number):
        phone_field = self.driver.find_element(*self.PHONE_FIELD)
        phone_field.send_keys(phone_number)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def enter_pin(self, pin):
        self.wait_and_send_keys(self.PIN_FIELD, pin)


    def click_login(self):
        self.wait_and_click(self.LOGIN_BTN, timeout=5)
