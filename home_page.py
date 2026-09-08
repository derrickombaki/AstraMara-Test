from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):
    #Locators
    SEND_BTN= (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='menu-button-send']")
    SEE_MORE = (AppiumBy.XPATH, "//android.widget.TextView[@text='See more']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_see_more(self):
        self.wait_and_click(self.SEE_MORE, timeout=10)

    def click_send_button(self):
        self.wait_and_click(self.SEND_BTN, timeout=5)



