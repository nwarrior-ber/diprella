from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class SignUpPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def first_name_field(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='first_name']")))

    @property
    def last_name_field(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='last_name']")))

    @property
    def email_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='email']")))

    @property
    def password_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='password']")))

    @property
    def terms_checkbox(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".terms")))

    @property
    def registration_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

    @allure.step("Enter user's E-mail address")
    def enter_email(self, email):
        self.email_field.send_keys(email)

        return self

    @allure.step("Enter user's first name")
    def enter_first_name(self, first_name):
        self.first_name_field.send_keys(first_name)

        return self

    @allure.step("Enter user's last name")
    def enter_last_name(self, last_name):
        self.last_name_field.send_keys(last_name)

        return self

    @allure.step("Enter password")
    def enter_password(self, password):
        self.password_field.send_keys(password)

        return self

    @allure.step("Accept Terms and Conditions")
    def check_terms_checkbox(self):
        self.terms_checkbox.click()

        return self

    @allure.step("Press Sign-up button")
    def submit_registration(self):
        from page_objects.main_page import MainPage

        self.registration_button.click()
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return MainPage(self.driver)
