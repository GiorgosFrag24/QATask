from mainDriver import MainDriverClass as Driver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AlarmControllerPage:
    _idLocatorOfMainHeader = "android:id/action_bar"
    _classLocatorOfMainHeaderText = "android.widget.TextView"
    _idLocatorOfClickableElementsList = 'android:id/list'
    _xpathLocatorOneShotAlarmButton = "//*[contains(@text, 'ONE SHOT ALARM')]"
    _xpathLocatorToastMessage = "//android.widget.Toast"

    def getMainHeader(self):
        return Driver.getElementById(self._idLocatorOfMainHeader)

    def getMainHeaderText(self):
        return self.getMainHeader().find_element(MobileBy.CLASS_NAME, 'android.widget.TextView').text

    def getListOfClickableElements(self):
        return Driver.getElementById(self._idLocatorOfClickableElementsList)

    def getOneShotAlarmButton(self):
        listOfClickableElements = self.getListOfClickableElements()
        return Driver.getChildElementFromParent(listOfClickableElements, self._xpathLocatorOneShotAlarmButton)

    def getToastMessageElement(self):
        wait = WebDriverWait(self.driver, 1)
        toastElement = wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Toast")))
        return toastElement

