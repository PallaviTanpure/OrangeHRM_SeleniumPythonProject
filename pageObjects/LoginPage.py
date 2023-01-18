from selenium.webdriver.common.by import By
from selenium import webdriver

#Page Object Login
class LoginPage:
    textbox_username = (By.XPATH,"//input[@name='username']")
    textbox_password = (By.XPATH,"//input[@name='password']")
    button_login = (By.XPATH,"//button[normalize-space()='Login']")
    profile_icon = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
    button_logout = (By.LINK_TEXT,"Logout")

    def __init__(self,driver):
        self.driver = driver

    #set username
    def setUserName(self, username):
        self.driver.find_element(*LoginPage.textbox_username).clear()
        self.driver.find_element(*LoginPage.textbox_username).send_keys(username)

    #set password
    def setPassword(self,password):
        self.driver.find_element(*LoginPage.textbox_password).clear()
        self.driver.find_element(*LoginPage.textbox_password).send_keys(password)

    #click login
    def clickLogin(self):
         self.driver.find_element(*LoginPage.button_login).click()

    # click logout
    def clickLogOut(self):
        self.driver.find_element(*LoginPage.profile_icon).click()
        self.driver.find_element(*LoginPage.button_logout).click()