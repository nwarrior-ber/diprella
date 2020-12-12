import pytest
from helpers.test_helpers import get_random_string
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from page_objects.start_page import StartPage


@pytest.fixture
def email():
    return f"{get_random_string()}@gmail.com"


@pytest.fixture
def first_name():
    return get_random_string()


@pytest.fixture
def last_name():
    return get_random_string()


@pytest.fixture
def password():
    return get_random_string()


@pytest.fixture
def start_page(request):
    driver = Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.get('https://demo.diprella.com/')

    start_page = StartPage(driver)

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return start_page
