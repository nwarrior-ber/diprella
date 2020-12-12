from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def user_name(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".user-banner__name"))).text

    @property
    def avatar_menu_link(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class*=avatar]")))

    @property
    def recommended_course_name(self):
        return self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//app-course-item)[1]//div[contains(@class, 'content-title')]"))).text

    @allure.step("Click bookmark flag icon fro the first recommended course")
    def click_bookmark(self):
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//div[@class='course-box-container-content-flag'])[1]"))).click()

    @allure.step("Navigate to Bookmarks page")
    def go_to_bookmarks(self):
        from page_objects.bookmarks_page import BookmarksPage

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/bookmarks']"))).click()
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return BookmarksPage(self.driver)

    def click_avatar_menu_link(self):
        self.avatar_menu_link.click()
        return self

    def logout(self):
        from page_objects.start_page import StartPage

        self.click_avatar_menu_link().wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[class='user__dropdown']/a[last()]"))).click()

        return StartPage(self.driver)
