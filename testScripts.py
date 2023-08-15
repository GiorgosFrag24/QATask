import logging
import time
from selenium.common.exceptions import NoSuchElementException
from pageClasses import *
from mainDriver import MainDriverClass as Driver
import pytest
import polling


class TestScripts:

    driver = Driver()

    @pytest.mark.run(order=1)
    def testValidateHeaderTitle(self):
        homePage = HomePage(self.driver)
        headerText = homePage.getMainHeaderText()
        assert (headerText == 'API Demos')
        logging.info('Main header\'s text content equals "API Demos"')

    @pytest.mark.run(order=2)
    def testAppButtonFunctionality(self):
        homePage = HomePage(self.driver)
        appButton = homePage.getAppButton()
        assert appButton.is_displayed()
        assert appButton.is_enabled()
        logging.info('App button is present and enabled in DOM')
        appButton.click()
        logging.info('App button has been clicked')

    @pytest.mark.run(order=3)
    def testAlarmButtonValidateAndClick(self):
        appPage = AppPage(self.driver)
        alarmButton = appPage.getAlarmButton()
        assert alarmButton.is_displayed()
        assert alarmButton.is_enabled()
        logging.info('Alarm button is present and enabled in DOM')
        alarmButton.click()
        logging.info('Alarm button has been clicked')

    @pytest.mark.run(order=4)
    def testAlarmControllerValidateAndClick(self):
        alarmPage = AlarmPage(self.driver)
        alarmControllerButton = alarmPage.getAlarmControllerButton()
        assert alarmControllerButton.is_displayed()
        assert alarmControllerButton.is_enabled()
        logging.info('Alarm Controller button is present and enabled in DOM')
        alarmControllerButton.click()
        logging.info('Alarm Controller button has been clicked')

    @pytest.mark.run(order=5)
    def testOneShotAlarmFunctionality(self):
        alarmControllerPage = AlarmControllerPage(self.driver)
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
                     step=2, timeout=60, ignore_exceptions=(NoSuchElementException,))
        logging.info('The text "gone off" is contained in the second alert\'s text')
