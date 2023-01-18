import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def get_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def get_element_text(self, locator):
        return self.get_element(locator).text

    def get_elements(self, locator):
        return self.driver.find_elements(By.XPATH, locator)

    def click(self,locator):
        self.get_element(locator).click()

    def clearText(self,locator):
        self.get_element(locator).clear()

    def get_elements_text(self,locator):
        list_of_element = self.get_elements(locator)
        list_text_value = []
        for each_element in list_of_element:
            list_text_value.append(each_element.text)
        return  list_text_value

    def safe_click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, locator))).click()


    def getActions(self):
        action = ActionChains(self.driver)
        return action

    def move_to_element(self, locator):
        ele = self.get_element(locator)
        self.getActions().move_to_element(ele)

    def double_click(self, locator):
        ele = self.get_element(locator)
        self.getActions().double_click(ele)

    def enter_text(self,locator,value):
        self.get_element(locator).send_keys(value)

    def get_page_title(self):
        return self.driver.title

    def scroll_into_view(self,locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",self.get_element(locator))

    def actions_click(self,locator):
        self.getActions().move_to_element(self.get_element(locator)).click().perform()

    def is_element_visible(self,locator):
        return self.get_element(locator).is_displayed()

    def wait_for_element(self,locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def get_driver(self):
        return self.driver

    def wait_for_element_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    def clear(self, locator):
        self.wait_for_element_clickable(locator)
        ele = self.get_element(locator)
        time.sleep(2)
        self.getActions().move_to_element(ele).double_click(ele).send_keys(Keys.DELETE).perform()