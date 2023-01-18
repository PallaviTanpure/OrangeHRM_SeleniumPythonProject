import pytest
from selenium import webdriver

from Configurations.AutoConfigCostants import AutoConstants
from pageObjects.EmployeePage import EmployeePage
from pageObjects.LoginPage import  LoginPage
from testCases import conftest
from utilities import readProperties
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_001_Login:

    baseURL = readProperties.ReadConfig.getApplicationURL();
    username = readProperties.ReadConfig.getUsername();
    password = readProperties.ReadConfig.getPassword();

    logger = LogGen.test_loggen()

    @pytest.mark.regression
    # verify the title of homepage
    def test_homepagetitle(self, setup):
        self.logger.info("***************** Test_001_Login **********************")
        self.logger.info("***** Verifying Home Page Title *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        # get the title of home page
        act_title = self.driver.title
        # verify the title of page
        if act_title == AutoConstants.homePageTitle:
            assert True
            self.driver.close()
            self.logger.info("Home Page Title Test is PASSED")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Pallavi_Tanpure\\PycharmProjects\\EmployeeSystem\\Screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            self.logger.error("Home Page Title Test is FAILED")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # verify the login is successful
    def test_login(self, setup):
        self.logger.info("***************** Test_001_Login **********************")
        self.logger.info("***** Verifying Login Test *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(10)
        # creating object of LoginPage class
        self.loginpage = LoginPage(self.driver)
        # accessing the methods of LoginPage Class
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassword(self.password)
        self.loginpage.clickLogin()
        # get the title of page
        act_title = self.driver.title
        # verify the title of page after login
        if act_title == AutoConstants.loginPageTitle:
            assert True
            self.driver.close()
            self.logger.info("Verifying Login Test is PASSED")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Pallavi_Tanpure\\PycharmProjects\\EmployeeSystem\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("Verifying Login Test is FAILED")
            assert False



