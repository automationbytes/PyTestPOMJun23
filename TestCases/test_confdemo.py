import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from Util.generateLogs import LogGenerator
from Util.readConfig import readConfig
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from PageObjects.loginPage import loginPage
from PageObjects.homePage import homePage
from pytest_html_reporter import attach

class TestDemo:
    logger = LogGenerator.loggen()
    driver = None

    @pytest.fixture()
    def prestep(self, setup):
        self.logger.info("------------PreStep------------")
        TestDemo.driver = setup
        TestDemo.driver.maximize_window()
        TestDemo.driver.implicitly_wait(10)
        TestDemo.driver.get(readConfig.getConfig("commoninfo", "baseURL"))
        self.logger.info("-------------Login---------------")
        lp = loginPage(TestDemo.driver)
        lp.enterUsername("standard_user")
        lp.enterPassword("secret_sauce")
        lp.clickLoginButton()

    def test_homePage(self, prestep):
        self.logger.info("-------------verify homepage -------------------")
        hp = homePage(TestDemo.driver)
        if hp.verifyHomePageLogo():
            assert True
        else:
            assert False, "Homepage logo verification failed"

    def test_sortDropdown(self, prestep):
        self.logger.info("------------- Sorting -------------------")
        hp = homePage(TestDemo.driver)
        hp.selectSortFilter("Price (high to low)")

