import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
# import sys
# sys.path.append('C:\\Users\dombaki\\PycharmProjects\\pytest_html_plus')
import pytest_html_plus

from config.utility import UtilityMethods
from pages.login_page import LoginPage
from pages.home_page import HomePage  #for resetting to homepage


@pytest.fixture(scope="class")
def app_driver(request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.platform_version = "15"
    options.app_package = "com.dbp.astrauat"
    options.app_activity = "com.dbp.astra.MainActivity"
    options.automation_name = "UiAutomator2"

    driver = webdriver.Remote("http://localhost:4723", options=options)
    driver.implicitly_wait(10)

    # Login once per class
    data = UtilityMethods.get_data_by_keys("login_details")
    login_page = LoginPage(driver)
    login_page.deny_permission()
    login_page.click_lets_do_this()
    login_page.enter_phone(data['phone'])
    login_page.click_continue()
    login_page.enter_pin(data['pin'])
    login_page.click_login()

    request.cls.driver = driver  # Optional: for use with self.driver in test classes
    yield driver
    driver.quit()


# @pytest.fixture(scope="function", autouse=True)
# def reset_to_home(app_driver):
#     yield
#     # Optional: reset to homepage after each test
#     home_page = HomePage(app_driver)
#     home_page.navigate_to_home()  # Replace with actual method if available
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call" and report.failed:
#         driver = item.funcargs.get("driver", None)
#         if driver:
#             screenshot_dir = "reports/screenshots"
#             os.makedirs(screenshot_dir, exist_ok=True)
#             timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")
#             driver.save_screenshot(screenshot_path)
#             if hasattr(report, "extra"):
#                 report.extra.append(extras.image(screenshot_path))
