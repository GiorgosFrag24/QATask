from mainDriver import MainDriverClass as Driver
from pageClasses.basePage import BasePage


class AlarmPage(BasePage):
    _xpathLocatorAlarmControllerButton = "//*[contains(@text,'Alarm Controller')]"

    def getAlarmControllerButton(self):
        listOfClickableElements = self.getListOfClickableElements()
        return Driver.getChildElementFromParent(listOfClickableElements, self._xpathLocatorAlarmControllerButton, 'XPATH')


