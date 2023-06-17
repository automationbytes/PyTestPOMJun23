# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
# from Util.generateLogs import LogGenerator
# from Util.readConfig import readConfig
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# from PageObjects.loginPage import loginPage
# from PageObjects.homePage import homePage
#
# class TestDemo:
#     logger = LogGenerator.loggen()
#     @pytest.fixture()
#     def prestep(self):
#         self.logger.info("------------PreStep------------")
#         if readConfig.getConfig("commoninfo","browser")=="chrome":
#             options = webdriver.ChromeOptions()
#             options.add_experimental_option("detach", True)
#             options.add_argument("--start-maximized")
#             self.driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
#         elif readConfig.getConfig("commoninfo","browser")=="firefox":
#             self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.driver.get(readConfig.getConfig("commoninfo","baseURL"))
#         self.logger.info("-------------Login---------------")
#         lp = loginPage(self.driver)
#         lp.enterUsername("standard_user")
#         lp.enterPassword("secret_sauce")
#         lp.clickLoginButton()
#
#     def test_homePage(self,prestep):
#         self.logger.info("-------------verify homepage -------------------")
#         hp = homePage(self.driver)
#         if hp.verifyHomePageLogo() == True:
#             assert True
#         else:
#             assert False
#
#     def test_sortDropdown(self,prestep):
#         self.logger.info("------------- Sorting -------------------")
#         hp = homePage(self.driver)
#         hp.selectSortFilter("Price (high to low)")
