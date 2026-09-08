import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions import interaction

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def click(self,locator,timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator)).click()

    def  wait_and_click(self,locator,timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def wait_and_send_keys  (self,locator,text,timeout=10):
        element =WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        element.send_keys(text)

    def wait_for_element(self,locator,timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def sleep(self,seconds):
        time.sleep(seconds)