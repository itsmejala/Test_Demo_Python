import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass():

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG) #DEBUG , INFO , WARNING , ERROR , CRITICAL
        return logger

    def waitTillElementWithLinkTextPresent(self,wait_time=5,text_present=''):
        wait = WebDriverWait(self.driver, wait_time )
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text_present)))


    def selectValueWithText(self,dropdown_element,text_to_select):
        select = Select(dropdown_element)
        select.select_by_visible_text(text_to_select)