import pytest

from Configurations.AutoConfigCostants import AutoConstants
from pageObjects.BasePage import BasePage
from pageObjects.EmployeePage import EmployeePage
from pageObjects.LoginPage import  LoginPage
from testCases import conftest
from utilities import readProperties
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_003_UpdateEmployee:
    baseURL = readProperties.ReadConfig.getApplicationURL();
    username = readProperties.ReadConfig.getUsername();
    password = readProperties.ReadConfig.getPassword();

    logger = LogGen.test_loggen()

    @pytest.mark.sanity
    #verify the employee is updated successfully
    def test_update_employee(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(10)
        # creating object of LoginPage class
        self.loginpage = LoginPage(self.driver)
        # accessing the methods of LoginPage Class
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassword(self.password)
        self.loginpage.clickLogin()
        self.emppage = EmployeePage(self.driver)
        self.employeeID = AutoConstants.empID

        #click on PIM Module
        self.emppage.click_on_PIM_module()

        #Click on add Emp Button
        self.emppage.click_on_AddEmployee_button()

        #enter the Name of the employee
        self.emppage.add_EmployeeDetails(AutoConstants.employeeUpdateFirstName,AutoConstants.employeeUpdateMiddleName,AutoConstants.employeeUpdateLastName)

        #clear the emp field
        self.emppage.clear_emp_id_field()

        #enter emp id
        self.emppage.enter_employee_ID(self.employeeID)

        #click on Add Button
        self.emppage.click_on_Save_Button()

        # #verify employee is added succcessfully
        addEmpStatusMessage = self.emppage.verify_employee_status_msg()
        assert addEmpStatusMessage == AutoConstants.addEmployeeSuccessStatus, "Employee is not added successfully"

        time.sleep(3)
        #Click on employee list option
        self.emppage.naviagte_to_EmployeeList()

        time.sleep(3)
        #enter the emp ID and click on search button
        self.emppage.search_Employee_by_ID(self.employeeID)

        #get the added employee
        empInfoList = self.emppage.get_updated_Employee_info()
        print(list(empInfoList))

        # verify the employee is added successfully
        actual_Name = AutoConstants.empAddedName in empInfoList
        assert True == actual_Name , "Employee is not added successfully"

        #click on update employee icon
        self.emppage.click_on_Empoyee_update_icon()

        #clear the emp name field
        self.emppage.clear_emp_name_field()

        #update the employee name
        self.emppage.update_Employee_info(AutoConstants.updateEmpName)

        # #verify employee is updated succcessfully
        updateEmpStatusMessage = self.emppage.verify_employee_status_msg()
        assert updateEmpStatusMessage == AutoConstants.updateEmployeeSuccessStatus, "Employee is not updated successfully"

        time.sleep(3)
        # Click on employee list option
        self.emppage.naviagte_to_EmployeeList()

        time.sleep(3)
        # enter the emp ID and click on search button
        self.emppage.search_Employee_by_ID(self.employeeID)

        # get the updated employee
        empUpdateInfoList = self.emppage.get_updated_Employee_info()
        print(list(empUpdateInfoList))

        # verify the employee is updated successfully
        actual_UpdatedEmpName = AutoConstants.employeeUpdateSearchName in empUpdateInfoList
        assert True == actual_UpdatedEmpName, "Employee Information is not updated successfully"

        #driver close
        self.driver.quit()


