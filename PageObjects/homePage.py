from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver

class homePage():

    #homepage
    sort_select_xpath = "//select[@data-test='product_sort_container']"
    open_menu_xpath = "//button[text()='Open Menu']"
    logout_button_xpath = "//a[text()='Logout']"
    logo_img_class = "app_loo"

    def __init__(self,driver):
        self.driver = driver
       # self.driver = webdriver.Chrome()

    def verifyHomePageLogo(self):
        return self.driver.find_element(By.CLASS_NAME,self.logo_img_class).is_displayed()


    def selectSortFilter(self,option):
        dropdown = Select(self.driver.find_element(By.XPATH,self.sort_select_xpath))
        dropdown.select_by_visible_text(option)

    def logout(self):
        self.driver.find_element(By.XPATH,self.open_menu_xpath).click()
        self.driver.find_element(By.XPATH,self.logout_button_xpath).click()
