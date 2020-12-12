import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def diprella_logo(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo__icon")))

    @property
    def signin_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/sign-in']")))

    @property
    def signup_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/sign-up']")))

    @property
    def search_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "search")))

    def search(self, criteria):
        self.search_field.send_keys(criteria)
        return self

    @allure.step("Click Sign-up button in the top right corner")
    def click_signup_button(self):
        from page_objects.signup_page import SignUpPage

        self.signup_button.click()

        return SignUpPage(self.driver)

    @allure.step("Click Sign-in link")
    def click_signin_link(self):
        from page_objects.signin_page import SignInPage

        self.signin_link.click()

        return SignInPage(self.driver)
