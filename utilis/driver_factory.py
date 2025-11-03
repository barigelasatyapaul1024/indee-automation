from selenium import webdriver

class DriverFactory:
    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        return driver