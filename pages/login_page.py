import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected

from pages.base_page import BasePage


class LoginPage(BasePage):
    pin_locator = (By.XPATH, "//input[@id='pin']")
    submit_button_locator = (By.XPATH, "//button[@id='sign-in-button']")
    accept_btn = (By.XPATH, "(//button[@aria-label='Accept All'])[1]")


    def login(self,pin):
        """

        :param pin:
        :return:
        """
        element = self.driver.find_element(By.XPATH, "(//button[@aria-label='Accept All'])[1]")
        if element:
            element.click()


        self.send_keys(self.pin_locator, pin)
        time.sleep(4)
        self.click(self.submit_button_locator)
        time.sleep(20)

