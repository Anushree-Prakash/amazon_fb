
from sources.generic_utilities.generic_methods import GenericMethods
from sources.utilities import custom_logger as cl
import  logging

class HomePage(GenericMethods):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def searchBox(self, product_name):
        # self.driver.find_element_by_id("twotabsearchtextbox").send_keys(product_name)
        self.sendKeys(product_name,"twotabsearchtextbox")
        self.elementClick("//input[@class='nav-input' and @value='Go']", "xpath")
        # self.driver.find_element_by_xpath("//input[@class='nav-input' and @value='Go']").click()
        self.timeSleep(3)
        self.elementClick("//span[text()='Apple iPhone 11 (64GB) - White']/..", "xpath")
        # //span[text()='Apple iPhone 11 (64GB) - White']/..
        self.timeSleep(5)
