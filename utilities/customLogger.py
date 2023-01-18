# generate the log file
import logging


class LogGen:
    @staticmethod
    def test_loggen():
        logging.basicConfig(
            filename="C:\\Users\\Pallavi_Tanpure\\PycharmProjects\\EmployeeSystem\\Logs\\automation.log",
            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I%M%S %p',filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.ERROR)
        return logger

# import logging
#
# class LogGen:
#     @staticmethod
#     def test_loggen():
#         logger = logging.getLogger(__name__)
#
#         fileHandler = logging.FileHandler('C:\\Users\\Pallavi_Tanpure\\PycharmProjects\\EmployeeSystem\\Logs\\automation.log')
#         formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
#         fileHandler.setFormatter(formatter)
#
#         logger.addHandler(fileHandler)  #filehandler object
#
#         logger.setLevel(logging.CRITICAL)
#         logger.debug("A debug statement is executed")
#         logger.info("Information statement")
#         logger.debug("A debug statement is executed")
#         logger.warning("Something is in warning mode")
#         logger.error("A Major error has happend")
#         logger.critical("Critical issue")




