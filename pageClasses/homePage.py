from pageClasses.basePage import BasePage


class HomePage(BasePage):

    _xpathLocatorAppButton = "//*[contains(@text,'App')]"

    def getAppButton(self):
        listOfClickableElements = self.getListOfClickableElements()
        return self.driver.getChildElementFromParent(listOfClickableElements, self._xpathLocatorAppButton, 'XPATH')


