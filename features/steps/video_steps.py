import time

from behave import given, when, then

from selenium import webdriver

from pages.login_page import LoginPage
from pages.home_page import HomePage



@given(u'the user launches the platform')
def step_launch(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.driver.maximize_window()
    context.driver.get("https://indeedemo-fyc.watch.indee.tv/login")
    time.sleep(15)
    context.driver.implicitly_wait(50)
    context.login = LoginPage(context.driver)
    context.driver.implicitly_wait(5)
    context.home = HomePage(context.driver)


@when(u'the user logs in with the provided PIN')
def step_login(context):
    context.login = LoginPage(context.driver)
    context.login.login(pin="WVMVHWBS")



@when(u'navigates to the "TEST AUTOMATION PROJECT"')
def step_impl(context):
    context.home = HomePage(context.driver)
    context.home.navigate_to_project()


