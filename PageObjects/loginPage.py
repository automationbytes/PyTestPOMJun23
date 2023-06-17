from selenium.webdriver.common.by import By
from  selenium import webdriver


class loginPage():
    # loginpage
    username_inputbox_name = "user-name"
    password_inputbox_name = "password"
    login_button_id = 'login-button'


    def __init__(self,driver):
        self.driver = driver
#        self.driver = webdriver.Chrome()


    def enterUsername(self,username):
        self.driver.find_element(By.NAME,self.username_inputbox_name).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.NAME, self.password_inputbox_name).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.ID, self.login_button_id).click()

