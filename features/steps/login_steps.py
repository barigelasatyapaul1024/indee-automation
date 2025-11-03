from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given("I open the Indee demo platform")
def open_platform(context):
    context.driver.get("https://indeedemo-fyc.watch.indee.tv/")

@when("I log in using the provided PIN")
def login(context):
    pin_field = context.driver.find_element(By.NAME, "pin")
    pin_field.send_keys("WVMVHWBS")
    submit_btn = context.driver.find_element(By.XPATH, "//button[text()='Continue']")
    submit_btn.click()
    time.sleep(3)