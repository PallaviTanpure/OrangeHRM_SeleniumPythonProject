import configparser

#reading data from config.ini file
config = configparser.RawConfigParser()
config.read("C:\\Users\\Pallavi_Tanpure\\PycharmProjects\\EmployeeSystem\\Configurations\\config.ini")


#get the data from config.ini file i.e BaseURL, username and password
class ReadConfig:
    @staticmethod  #directly access this method using class without creating object
    def getApplicationURL():
        url = config.get("common info","baseURL")
        return url

    @staticmethod
    def getUsername():
        uname = config.get("common info","username")
        return uname

    @staticmethod
    def getPassword():
        pswd = config.get("common info","password")
        return pswd
