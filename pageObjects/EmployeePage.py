import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from pageObjects.BasePage import BasePage
from utilities.customLogger import LogGen



class EmployeePage(BasePage):

    pim_module = "//span[normalize-space()='PIM']"
    addEmployeeButton = "//button[normalize-space()='Add']"
    employeeFirstName = "//input[@name='firstName']"
    employeeMiddleName = "//input[@name='middleName']"
    employeeLastName = "//input[@name='lastName']"
    saveButton = "//button[normalize-space()='Save']"
    cancelButton = "//button[normalize-space()='Cancel']"
    employeeList = "//a[normalize-space()='Employee List']"
    employeeID = "//div[@class='orangehrm-employee-container']//input[@class='oxd-input oxd-input--active']"
    searchEmployeeID = "//div[@class='oxd-table-filter']//input[@class='oxd-input oxd-input--active']"
    searchButton = "//button[normalize-space()='Search']"
    deleteEmployeeIcon = "//div[@class='oxd-table orangehrm-employee-list']//button//i[@class='oxd-icon bi-trash']"
    updateEmployeeIcon  = "//div[@class='oxd-table orangehrm-employee-list']//button//i[@class='oxd-icon bi-pencil-fill']"
    getUpdatedEmpInfo = "//div[@class='oxd-table orangehrm-employee-list']//div[@class='oxd-table-card']//div//div//div[normalize-space()]"
    searchEmployeeName = "//div[@class='oxd-table-filter']//input[@placeholder='Type for hints...']"
    emp_id_field = "//label[text()='Employee Id']/../parent::div//input"
    deleteBtnInPopup = "//button[normalize-space()='Yes, Delete']"
    empStatusMsg = "//div[@class='oxd-toast-content oxd-toast-content--success']//p[contains(@class,'toast-message')]"

    logger = LogGen.test_loggen()

    def __init__(self,driver):
        super().__init__(driver)


    #Click on PIM Module
    def click_on_PIM_module(self):
        self.safe_click(EmployeePage.pim_module)
        time.sleep(5)
        self.logger.info("Clicked on PIM Module")


    #Click on Add Employee Button
    def click_on_AddEmployee_button(self):
        # Click on Add Button
        self.safe_click(EmployeePage.addEmployeeButton)
        time.sleep(5)
        self.logger.info("Clicked on Add Employee Button")


    #Enter the Employee Details
    def add_EmployeeDetails(self,fNameValue,mNameValue,lNameValue):
        self.logger.info("Add Employee Page Opened")
        self.enter_text(EmployeePage.employeeFirstName,fNameValue)
        time.sleep(2)
        self.logger.info("Entered the Employee First name in the textbox")
        self.enter_text(EmployeePage.employeeMiddleName, mNameValue)
        time.sleep(2)
        self.logger.info("Entered the Employee Middle name in the textbox")
        self.enter_text(EmployeePage.employeeLastName, lNameValue)
        time.sleep(2)
        self.logger.info("Entered the Employee Last name in the textbox")

    #Enter the Employee ID
    def enter_employee_ID(self, empID):
        self.enter_text(EmployeePage.emp_id_field, empID)
        self.logger.info("Entered the Employee ID in the textbox")

    #Click On Save Button
    def click_on_Save_Button(self):
        self.safe_click(EmployeePage.saveButton)
        self.logger.info("Clicked on Save Button")

    #Click on Employee List Option
    def naviagte_to_EmployeeList(self):
        self.safe_click(EmployeePage.employeeList)
        self.logger.info("Clicked on Employee List Option")

    #search the employee by emp name
    def search_Employee_by_ID(self,ID):
        self.enter_text(EmployeePage.emp_id_field, ID)
        time.sleep(2)
        self.logger.info("Entered the Employee  ID in the textbox")
        self.logger.info("Entered the employee ID")
        self.click(EmployeePage.searchButton)
        time.sleep(5)
        self.logger.info("Clicked on Search Button")

    # Click on Employee update button
    def click_on_Empoyee_update_icon(self):
        self.safe_click(EmployeePage.updateEmployeeIcon)
        time.sleep(2)
        self.logger.info("Clicked on Employee Update button")


    #update the employee data
    def update_Employee_info(self,value):
        self.enter_text(EmployeePage.employeeFirstName,value)
        time.sleep(2)
        self.logger.info("Updated the Employee Last name in the textbox")
        self.safe_click(EmployeePage.saveButton)
        self.logger.info("Clicked on save Button")

    #get the updated Employee info
    def get_updated_Employee_info(self):
        self.logger.info("Getting updated information of Employee")
        updatedEmpList = self.get_elements_text(EmployeePage.getUpdatedEmpInfo)
        print(type(updatedEmpList))
        print(list(updatedEmpList))
        self.logger.info("Getting updated information of Employee in List")
        return updatedEmpList


    # delete the employee
    def delete_Employee(self):
        self.safe_click(EmployeePage.deleteEmployeeIcon)
        self.logger.info("Clicked on delete icon")
        time.sleep(2)
        self.safe_click(EmployeePage.deleteBtnInPopup)
        self.logger.info("Clicked on delete button in the popup")
        self.logger.info("Deleted the Employee")

    # clear the employee id field
    def clear_emp_id_field(self):
        self.clear(EmployeePage.emp_id_field)

    # clear the employee name field
    def clear_emp_name_field(self):
        self.clear(EmployeePage.employeeFirstName)

    #verify the delete icon is present or not
    def is_delete_icon_present_or_not(self):
        time.sleep(2)
        deleteiconflag = self.is_element_visible(EmployeePage.deleteEmployeeIcon)
        self.logger.info("Delete icon is not present")
        return deleteiconflag

    #verify employee is added,updated and deleted successfully
    def verify_employee_status_msg(self):
        self.wait_for_element(EmployeePage.empStatusMsg)
        empStatus = self.get_element_text(EmployeePage.empStatusMsg)
        self.logger.info("Getting employee successful message")
        return empStatus