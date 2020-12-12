from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # WRAPPER FUNCTION
    @allure.step("Click library menu item {1}")
    def select_library_item(self, item):
        self.library_menu.click()
        return self.driver.find_element_by_css_selector(f"[href*='{item}']").click()

    @property
    def library_menu(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='library']")))

    @property
    def locale_menu(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "(//footer//p-dropdown)[1]")))

    @allure.step("Select page locale: English/Ukrainian")
    def select_locale(self, locale):
        self.locale_menu.click()
        if locale == 'EN':
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//footer//p-dropdown)[1]//li[1]"))).click()
        if locale == 'UA':
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//footer//p-dropdown)[1]//li[2]"))).click()
