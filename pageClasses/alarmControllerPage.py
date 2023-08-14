from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AlarmControllerPage:

    _xpathLocatorOneShotAlarmButton = "//*[contains(@text, 'ONE SHOT ALARM')]"
    _xpathLocatorToastMessage = "//android.widget.Toast"

    def __init__(self, appDriver):
        self.driver = appDriver

    def getOneShotAlarmButton(self):
        return self.driver.getElementByXpath(self._xpathLocatorOneShotAlarmButton)

    def getToastMessageElement(self):
        wait = WebDriverWait(self.driver.driver, 1)  # Toast message should appear immediately after clicking action,
        # hence, the timeout of 1
        toastElement = wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Toast")))
        return toastElement

    def getToastMessageElementText(self):
        return self.driver.getElementByXpath(self._xpathLocatorToastMessage).text
