from appium.webdriver.common.mobileby import MobileBy
from mainDriver import MainDriverClass as Driver


class BasePage:
    driver = Driver()

    def __init__(self):
        self._idLocatorOfMainHeader = "android:id/action_bar"
        self._classLocatorOfMainHeaderText = "android.widget.TextView"
        self._idLocatorOfClickableElementsList = 'android:id/list'

    def getMainHeader(self):
        return self.driver.getElementById(self._idLocatorOfMainHeader)

    def getMainHeaderText(self):
        return self.getMainHeader().find_element(MobileBy.CLASS_NAME, 'android.widget.TextView').text

    def getListOfClickableElements(self):
        return self.driver.getElementById(self._idLocatorOfClickableElementsList)
