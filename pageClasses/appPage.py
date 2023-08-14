from mainDriver import MainDriverClass as Driver
from appium.webdriver.common.mobileby import MobileBy
from pageClasses.basePage import BasePage

class AppPage(BasePage):
    _xpathLocatorAlarmButton = "//*[contains(@text,'Alarm')]"

    def getAlarmButton(self):
        listOfClickableElements = self.getListOfClickableElements()
        return self.driver.getChildElementFromParent(listOfClickableElements, self._xpathLocatorAlarmButton)


