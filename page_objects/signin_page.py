from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class SignInPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def email_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='email']")))

    @property
    def password_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='password']")))

    @property
    def login_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

    @allure.step("Enter user's E-mail address")
    def enter_email(self, email):
        self.email_field.send_keys(email)

        return self

    @allure.step("Enter password")
    def enter_password(self, password):
        self.password_field.send_keys(password)

        return self

    @allure.step("Press Sign-in button")
    def login(self):
        from page_objects.main_page import MainPage

        self.login_button.click()
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return MainPage(self.driver)
