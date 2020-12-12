from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page_objects.main_page import MainPage
import allure


class BookmarksPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def bookmarked_course_name(self):
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        return self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//app-course-item)[1]//div[contains(@class, 'content-title')]"))).text
