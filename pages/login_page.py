import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    pin_locator = (By.XPATH, "//input[@id='pin']")
    submit_button_locator = (By.XPATH, "//button[@id='sign-in-button']")


    def login(self,pin):
        """

        :param pin:
        :return:
        """
        self.send_keys(self.pin_locator, pin)
        time.sleep(4)
        self.click(self.submit_button_locator)
        time.sleep(20)

