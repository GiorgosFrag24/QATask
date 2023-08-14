from mainDriver import MainDriverClass as Driver
from appium.webdriver.common.mobileby import MobileBy


class AlarmPage:
    _idLocatorOfMainHeader = "android:id/action_bar"
    _classLocatorOfMainHeaderText = "android.widget.TextView"
    _idLocatorOfClickableElementsList = 'android:id/list'
    _xpathLocatorAlarmControllerButton = "//*[contains(@text,'Alarm Controller')]"

    def getMainHeader(self):
        return Driver.getElementById(self._idLocatorOfMainHeader)

    def getMainHeaderText(self):
        return self.getMainHeader().find_element(MobileBy.CLASS_NAME, 'android.widget.TextView').text

    def getListOfClickableElements(self):
        return Driver.getElementById(self._idLocatorOfClickableElementsList)

    def getAlarmControllerButton(self):
        listOfClickableElements = self.getListOfClickableElements()
        return Driver.getChildElementFromParent(listOfClickableElements, self._xpathLocatorAlarmButton)


