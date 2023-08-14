import logging
import time
from selenium.common.exceptions import NoSuchElementException
from pageClasses import *
import mainDriver
import pytest
import polling


class TestScripts:

    @pytest.mark.run(order=1)
    def testValidateHeaderTitle(self):
        homePage = HomePage()
        headerText = homePage.getMainHeaderText()
        assert (headerText == 'API Demos')
        logging.info('Main header\'s text content equals "API Demos"')

