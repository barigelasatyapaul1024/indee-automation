

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait(self,locator,timeout =150):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))

    def click(self,locator):
        """

        :param locator:
        :return:
        """
        self.driver.find_element(*locator).click()

    def send_keys(self,locator,text):
        """

        :param locator:
        :param text:
        :return:
        """
        element = self.wait(locator)
        element.clear()
        element.send_keys(text)
