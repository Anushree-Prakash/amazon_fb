# '''
# name : Anu
# email_id : anu@gmail.com
# date : 23/06/2020
# '''
#
# import logging
# from traceback import print_stack
#
# from selenium.webdriver.common.by import By
# from sources.generic_utilities.webdriver_factory import WebDriverFactory
# import sources.utilities.custom_logger as cl
#
# class GenericUtilities(WebDriverFactory):
#     log = cl.customLogger(logging.DEBUG)
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     # it is responsible for inspecting locators
#     def getByType(self,locatorType):
#         locatorType = locatorType.lower()
#         if locatorType == "id":
#             return By.ID
#         if locatorType == "name":
#             return By.NAME
#         if locatorType == "xpath":
#             return By.XPATH
#         if locatorType == "css":
#             return By.CSS_SELECTOR
#         if locatorType == "class":
#             return By.CLASS_NAME
#         if locatorType == "tagname":
#             return By.TAG_NAME
#         if locatorType == "link":
#             return By.LINK_TEXT
#         if locatorType == "partial":
#             return By.PARTIAL_LINK_TEXT
#         else:
#             self.log.info("locator type" + locatorType + "NOT Correct/ TRY ONCE AGAIN...!!!")
#         return False
#
#         # self.driver.find_element(By.ID,"asdfertrgsrzd")
#     def getElement(self,locator, locatorType='id'):
#         element = None
#         try:
#             locatorType = locatorType.lower()
#             byType = self.getByType(locatorType)
#             element = self.driver.find_element(byType, locator)
#             self.log.info("Element found with locator" + locatorType + "value : " + locator)
#         except:
#             self.log.info("Element is not found with locator"+ locatorType+"value : " + locator)
#             print_stack()
#         return element
#
#     def sendKeys(self,data, locator, locatorType='id'):
#         try:
#             self.getElement(locator, locatorType).send_keys(data)
#             print("Data is send successfully with locator type" + locatorType + "value : " + locator)
#         except:
#             print("Data is not send successfully with locator type" + locatorType + "value : " + locator)
#             # print_stack()


import os
import time
from logging import Logger

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import sources.utilities.custom_logger as cl
import logging
import time
class GenericMethods():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver


    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage+ "." +str(round(time.time() * 1000))+ ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory:" + destinationFile)
        except:
            self.log.error("### Exception Occurred")
            print_stack()

    # it'll return the title of the page
    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def clearText(self,locator,locatorType="id"):
        try:
            self.getElement(locator , locatorType).clear()
            self.log.info("The text field is cleared with locator " + locator + " and locator type " + locatorType)
        except:
            self.log.error("#### Not able to clear ####")
            print_stack()


    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def screenShot(self, resultMessage):
        filename = resultMessage + "."+ str(round(time.time()*1000)) + ".png"
        screenshortDirectory  = "../screeshots/"
        relativeFileName = screenshortDirectory + filename
        currenDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currenDirectory, relativeFileName)
        destinationDirectory = os.path.join(currenDirectory, screenshortDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("screenshot saved to directory :" + destinationFile)

        except:
            self.log.error("####Exception occured####")
            print_stack()

    def clearText(self,locator,locatorType="id"):
        try:
            self.getElement(locator, locatorType).clear()
            self.log.info("text filed is  cleared with locator: " +locator +"locator type" +locatorType)
        except:
            self.log.info("the text filed can't be cleared with locator: " + locator + "locator type" + locatorType)
            print_stack()

    def elementClick(self,locator, locatorType='id'):
        try:
            self.getElement(locator,locatorType).click()
            self.log.info("clicked on element with locator " + locator+"locatorType"+locatorType)
        except:
            self.log.info("Cann't click on element with locator " + locator + "locatorType" + locatorType)
            print_stack()

    def waitForElement(self, locator, locatorType='id', timeout=10,pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum ::" +str(timeout)+"::seconds for elemnet to be clicable" )
            wait = WebDriverWait(self.driver, timeout, poll_frequency=[NoSuchElementException,
                                                                    ElementNotVisibleException,
                                                                    ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("element appeared on the web page")
        except:
            self.log.error("element not appeared on the wed page")
            print_stack()
        return element

    def switch_to_child_window(self, driver):
        child_window = None
        parent_window = driver.current_window_handle
        window_ids = driver.window_handles
        try:
            for window_id in window_ids:
                if window_id != parent_window:
                    child_window = window_id
                    break
            driver.switch_to.window(child_window)

        except:
            self.log.info("unable to change the focus to the child window")
            print_stack()
    def timeSleep(self,sec):
        time.sleep(sec)




