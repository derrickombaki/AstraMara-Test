# pages/send_money_page.py

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from appium.webdriver.extensions.android.nativekey import AndroidKey


class SendMoneyPage(BasePage):
    # Locators

    # Wallet Transfer
    ACCOUNT_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='input-wallet-number']")
    WALLET_AMOUNT_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='input-send-to-wallet-amount']")
    CONTINUE_BTN_WALLET = (AppiumBy.XPATH,"//android.view.ViewGroup[@resource-id='btn-send-to-wallet-recipient-continue']")

    # Mobile Money
    MOBILE_MONEY = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Mobile')]")
    OTHER_NUMBER = (AppiumBy.XPATH, "//android.widget.TextView[@text='To other number']")
    ENTER_PHONE_NUMBER = (AppiumBy.XPATH,
                          "//android.widget.EditText[@resource-id='input-send-to-non-beneficiary-number']")
    MOBILE_AMOUNT_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='input-send-to-mobile-amount']")
    CONTINUE_BTN_MOBILE = (AppiumBy.XPATH, "//*[@text='Continue']")

    # Local Bank
    LOCAL_BANKS = (AppiumBy.XPATH, "//*[contains(@text, 'Local')]")
    USING_ACCOUNT_OPTION = (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='btn-using-account-number-option']")
    SELECT_BANK_DROPDOWN = (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='btn-dropdown-select-bank']")
    BANK_SEARCH_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='input-dropdown-select-bank']")
    BANK_RESULT = lambda self, name: (AppiumBy.XPATH, f"//android.view.ViewGroup[@content-desc='{name}']")
    BANK_ACCOUNT_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='input-send-to-bank-account-number']")
    BANK_AMOUNT_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='input-send-to-bank-amount']")
    CONTINUE_BTN_BANK = (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='btn-send-to-bank-continue']")

    # Shared
    PURPOSE_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='fund-account-input-narration']")
    #CONFIRM_PAYMENT_BTN = (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='confirm-payment-button']")
    SEND_BTN = (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='confirm-payment-button']")
    PASSCODE_INPUT = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='passcode-input']")
    VERIFY_BTN = (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='btn-confirmation-modal-yes']")
    FEE_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='Fee KES 0.00']")
    DONE_BTN = (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='btn-done']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)


    # Wallet Transfer
    def enter_wallet_account(self, account_number):
        print("Attempting to locate wallet account input field...")
        enter_wallet_account= self.wait.until(EC.presence_of_element_located(self.ACCOUNT_INPUT))
        enter_wallet_account.click()
        enter_wallet_account.send_keys(account_number)
        self.driver.hide_keyboard()

    def enter_wallet_amount(self, amount):
        print("Attempting to locate wallet amount input field...")
        enter_wallet_amount = self.wait.until(EC.presence_of_element_located(self.WALLET_AMOUNT_INPUT))
        enter_wallet_amount.click()
        enter_wallet_amount.send_keys(amount)

    def click_continue_wallet_transfer(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN_WALLET)).click()

    # Mobile Money Transfer
    def select_mobile_money(self):
        self.wait.until(EC.element_to_be_clickable(self.MOBILE_MONEY)).click()

    def select_other_number(self):
        self.wait.until(EC.element_to_be_clickable(self.OTHER_NUMBER)).click()

    def enter_mobile_number(self, number):
        self.wait.until(EC.presence_of_element_located(self.ENTER_PHONE_NUMBER)).send_keys(number)
        self.driver.hide_keyboard()

    def enter_mobile_amount(self, amount):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().resourceId("input-send-to-mobile-amount"))'
        )
        self.wait.until(EC.presence_of_element_located(self.MOBILE_AMOUNT_INPUT)).send_keys(amount)

    def continue_mobile_transfer(self):
        self.wait.until(EC.presence_of_element_located(self.CONTINUE_BTN_MOBILE)).click()

    # Local Bank Transfer
    def select_local_bank_option(self):
        self.wait.until(EC.element_to_be_clickable(self.LOCAL_BANKS)).click()

    def choose_account_number_option(self):
        self.wait.until(EC.element_to_be_clickable(self.USING_ACCOUNT_OPTION)).click()

    def open_bank_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_BANK_DROPDOWN)).click()

    def search_and_select_bank(self, bank_name):
        self.wait.until(EC.presence_of_element_located(self.BANK_SEARCH_INPUT)).send_keys(bank_name)
        self.wait.until(EC.element_to_be_clickable(self.BANK_RESULT(bank_name))).click()

    def enter_bank_account(self, account_number):
        self.wait.until(EC.visibility_of_element_located(self.BANK_ACCOUNT_INPUT)).send_keys(account_number)
        self.driver.press_keycode(AndroidKey.ENTER)

    def enter_bank_amount(self, amount):
        self.wait.until(EC.element_to_be_clickable(self.BANK_AMOUNT_INPUT)).send_keys(amount)

    def continue_bank_transfer(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN_BANK)).click()

    # Shared
    def enter_purpose(self, purpose):
        self.wait.until(EC.presence_of_element_located(self.PURPOSE_INPUT)).send_keys(purpose)
        self.driver.press_keycode(AndroidKey.ENTER)

    def click_send_money(self,):
        send_btn = self.wait.until(EC.element_to_be_clickable(self.SEND_BTN))
        send_btn.click()


    def enter_passcode(self, passcode):
        self.wait.until(EC.presence_of_element_located(self.PASSCODE_INPUT)).send_keys(passcode)

    def click_verify(self):
        self.wait.until(EC.element_to_be_clickable(self.VERIFY_BTN)).click()


    def click_done(self):
        self.wait.until(EC.element_to_be_clickable(self.DONE_BTN)).click()
