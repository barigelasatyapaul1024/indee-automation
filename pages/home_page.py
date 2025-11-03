import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class HomePage(BasePage):
    all_titles = (By.XPATH, "(//button[@class='brand-card'])[1]")
    project = (By.XPATH, "//a[@id='videosSection']")
    project_details = (By.XPATH, "//a[@id='detailsSection']")
    play_video_btn= (By.XPATH, "//button[@aria-label='Play Video']")
    session = (By.XPATH, "//div[@id='expiringSoon']")
    # play_video_btn= (By.XPATH, "//span[@id='vidTitle']")
    alert_locator = (By.XPATH, "//div[@class='cky-notice']")




    def navigate_to_project(self):

        """
        Navigate to the project page
        Do the video performance for testing and logout



        :return:
        """
        self.click(self.all_titles)
        # self.driver.switch_to.alert.accept("Accept All")


        element = self.driver.find_element(By.XPATH, "(//div[@title='Test automation project']//div)[2]")
        self.driver.wait_until(lambda: self.driver.find_element(element))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        action.click(element).perform()
        time.sleep(20)
        action.send_keys(Keys.ARROW_DOWN).perform()
        session_id = self.driver.find_element(By.XPATH, "//div[@id='expiringSoon']")
        action.scroll_to_element(session_id).perform()
        # self.driver.find_element(By.XPATH, "//a[@id='videosSection']").click()
        self.driver.find_element(By.XPATH, "//a[@id='detailsSection']").click()
        time.sleep(15)
        self.driver.find_element(By.XPATH, "//a[@id='videosSection']").click()

        # action.send_keys(*(Keys.TAB for _ in range(3))).perform()
        # action.send_keys(Keys.ENTER).perform()
        play_tbn =  self.driver.find_element(By.XPATH, "//button[@aria-label='Play Video']")
        action.move_to_element(play_tbn).perform()
        action.click(play_tbn).perform()
        time.sleep(25)
        action.send_keys(Keys.SPACE).perform()
        time.sleep(10)
        action.send_keys(Keys.SPACE).perform()
        time.sleep(10)
        action.send_keys(*(Keys.DOWN for _ in range(4))).perform()
        time.sleep(30)
        action.send_keys(Keys.SPACE).perform()
        for _ in range(19):
            action.send_keys(Keys.TAB)
        action.perform()
        for _ in range(3):
            action.send_keys(Keys.DOWN)
        action.perform()
        time.sleep(10)
        action.send_keys(Keys.ENTER).perform()
        time.sleep(10)
        self.driver.back()
        time.sleep(10)
        sign_out = self.driver.find_element(By.XPATH, "//button[@id='signOutSideBar']")
        sign_out.click()
        time.sleep(10)

