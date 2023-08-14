import logging
import polling
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from pageClasses import *


class TestScripts:

    def testValidateHeaderTitle(self):
        homePage = HomePage()
        headerText = homePage.getMainHeaderText()
        assert (headerText == 'API Demos')
        logging.info('Main header\'s text content equals "API Demos"')

    def testAppButtonFunctionality(self):
        homePage = HomePage()
        appButton = homePage.getAppButton()
        assert appButton.is_displayed()
        assert appButton.is_enabled()
        logging.info('App button is present and enabled in DOM')
        appButton.click()
        logging.info('App button has been clicked')

    def testAlarmButtonValidateAndClick(self):
        appPage = AppPage()
        alarmButton = appPage.getAlarmButton()
        assert alarmButton.is_displayed()
        assert alarmButton.is_enabled()
        logging.info('Alarm button is present and enabled in DOM')
        alarmButton.click()
        logging.info('Alarm button has been clicked')

    def testAlarmControllerValidateAndClick(self):
        alarmPage = AlarmPage()
        alarmControllerButton = alarmPage.getAlarmControllerButton()
        assert alarmControllerButton.is_displayed()
        assert alarmControllerButton.is_enabled()
        logging.info('Alarm Controller button is present and enabled in DOM')
        alarmControllerButton.click()
        logging.info('Alarm Controller button has been clicked')

    def testOneShotAlarmFunctionality(self):
        alarmControllerPage = AlarmControllerPage()
        oneShotAlarmButton = alarmControllerPage.getOneShotAlarmButton()
        assert oneShotAlarmButton.is_displayed()
        assert oneShotAlarmButton.is_enabled()
        logging.info('One Shot Alarm button is present and enabled in DOM')
        oneShotAlarmButton.click()
        logging.info('One Shot Alarm button has been clicked')
        toastMessageElement = alarmControllerPage.getToastMessageElement()
        assert '30 seconds' in toastMessageElement.text
        logging.info('The text "30 seconds" is contained in the first alert\'s text')
        logging.info('Sleeping for 30 seconds')
        time.sleep(30)
        polling.poll(lambda: 'gone off' in alarmControllerPage.getToastMessageElementText(),
                     step=1, timeout=60, ignore_exceptions=(NoSuchElementException,))
        logging.info('The text "gone off" is contained in the second alert\'s text')
