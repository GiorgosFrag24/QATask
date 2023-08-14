import logging
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import yaml


class MainDriverClass:

    desiredCapabilities = {}
    driver = None

    def __init__(self):
        logging.info("Setting up driver with the desired capabilities")
        with open('desiredCapabilities.yaml', 'r') as desiredCapabilitiesFile:
            desiredCapabilities = yaml.safe_load(desiredCapabilitiesFile)
        self.driver = webdriver.Remote("http://127.0.0.1:4723", desiredCapabilities)

    def getElementById(self, locator):
        try:
            logging.info(f'Attempting to find element with locator:"{locator}" and locator type "ID" ')
            element = self.driver.find_element(MobileBy.ID, locator)
            logging.info(f'Found the requested element with locator:"{locator}" and locator type "ID"')
            return element
        except NoSuchElementException:
            logging.error(f'No element could be found with locator:"{locator}" and locator type "ID"')
        except TimeoutException:
            logging.error(f'Timed out after trying to find element with locator:"{locator}" and locator type "ID"')
        except Exception as exception:
            logging.error(f'An unexpected error occurred. {exception}')

    def getElementByClass(self, locator):
        try:
            logging.info(f'Attempting to find element with locator:"{locator}" and locator type "Class Name" ')
            element = self.driver.find_element(MobileBy.CLASS_NAME, locator)
            logging.info(f'Found the requested element with locator:"{locator}" and locator type "Class Name"')
            return element
        except NoSuchElementException:
            logging.error(f'No element could be found with locator:"{locator}" and locator type "Class Name"')
        except TimeoutException:
            logging.error(f'Timed out after trying to find element with locator:"{locator}" and locator type "Class Name"')
        except Exception as exception:
            logging.error(f'An unexpected error occurred. {exception}')

    def getElementByXpath(self, locator):
        logging.info(f'Attempting to find element with locator:"{locator}" and locator type "XPATH" ')
        element = self.driver.find_element(MobileBy.XPATH, locator)
        logging.info(f'Found the requested element with locator:"{locator}" and locator type "XPATH"')
        return element

    @staticmethod
    def getChildElementFromParent(parentElement, childLocator, locatorType):
        logging.info(f'Attempting to find child element {childLocator} with locator type {locatorType}')
        match locatorType:
            case "ID":
                return parentElement.find_element(MobileBy.ID, childLocator)
            case "CLASS":
                return parentElement.find_element(MobileBy.CLASS_NAME, childLocator)
            case "XPATH":
                return parentElement.find_element(MobileBy.XPATH, childLocator)

    @staticmethod
    def getElementText(self, element):
        logging.info(f'Retrieving the text of requested element')
        return element.text
