import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="D:\\AlationProject_2023\\Project_Softwares\\chromedriver.exe")
    driver.maximize_window()
    return driver


############### PyTest HTML Report  ########################

# It is hook for Adding environment info to the HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'OrangeHRM'
    config._metadata['Module Name'] = 'PIM'
    config._metadata['Tester'] = 'Pallavi'

# It is hook for delete/modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


