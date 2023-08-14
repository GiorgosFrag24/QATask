from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pageClasses.basePage import BasePage


class AlarmControllerPage(BasePage):
    _xpathLocatorOneShotAlarmButton = "//*[contains(@text, 'ONE SHOT ALARM')]"
    _xpathLocatorToastMessage = "//android.widget.Toast"

    def getOneShotAlarmButton(self):
        listOfClickableElements = self.getListOfClickableElements()
        return self.driver.getChildElementFromParent(listOfClickableElements, self._xpathLocatorOneShotAlarmButton)

    def getToastMessageElement(self):
        wait = WebDriverWait(self.driver, 1) # Toast message should appear immediately after clicking action, hence the timeout of 1
        toastElement = wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Toast")))
        return toastElement

    def getToastMessageElementText(self):
        return self.driver.find_element(MobileBy.XPATH, self._xpathLocatorToastMessage).text
