import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", help="Choose the browser: chrome or firefox")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    #if report.when == "call" and report.failed:
    if report.when == "call":
        allure.attach(item.parent.cls.driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)
