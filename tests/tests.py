import pytest
import allure
from config.test_conf import Config


@allure.title("Create a new account. Sign-up button in the header")
def test_signup(start_page, email, first_name, last_name, password):
    Config.logger.info(f"Creating a new account with {email}, {first_name}, {last_name}, {password}")

    signup_page = start_page.click_signup_button()

    signup_page.enter_first_name(first_name)
    signup_page.enter_last_name(last_name)
    signup_page.enter_email(email)
    signup_page.enter_password(password)
    signup_page.check_terms_checkbox()

    main_page = signup_page.submit_registration()

    expected_user_name = f"{first_name.lower()}" + ' ' + f"{last_name.lower()}"

    assert main_page.user_name.lower() == expected_user_name, f"Actual user's name {main_page.user_name} is not as expected {first_name}" + ' ' + f"{last_name}"


@allure.title("Login with an existing account")
@pytest.mark.parametrize("email, password", [("ia6x@yahoo.com", 123456789)])
def test_login_existing_user(start_page, email, password):
    Config.logger.info(f"Sign-in with existing account credentials {email}, {password}")

    signin_page = start_page.click_signin_link()

    signin_page.enter_email(email)
    signin_page.enter_password(password)

    main_page = signin_page.login()

    assert main_page.avatar_menu_link.is_displayed, f"Login with existing account is not performed"


@allure.title("Login with a non-existing account")
@pytest.mark.parametrize("email, password", [("user@test.com", 123456789)])
def test_login_non_existing_user(start_page, email, password):

    Config.logger.info(f"Sign-in with non-existing account credentials {email}, {password}")

    signin_page = start_page.click_signin_link()

    signin_page.enter_email(email)
    signin_page.enter_password(password)

    main_page = signin_page.login()

    assert main_page.driver.find_element_by_css_selector(
        '.error__text'), f"Login with non-existing account is performed"


@allure.title("Navigation from Library drop-down: Verify library pages are displayed in EN")
@pytest.mark.parametrize("menu_item, expected_header", (
        ("Development", "Development"),
        ("Design", "Design"),
        ("Business", "Business"),
        ("Personal", "Personal Development"),
        ("Marketing", "Marketing"),
        ("Language", "Language"),
        ("Lifestyle", "Lifestyle"),
        ("Arts", "Arts")))
def test_library_pages_EN(start_page, menu_item, expected_header):

    Config.logger.info(f"Open library page {menu_item} and expecting page header {expected_header}")

    start_page.select_locale('EN')
    start_page.select_library_item(menu_item)
    page_header = start_page.driver.find_element_by_tag_name('h1').text

    allure.attach(start_page.driver.find_element_by_tag_name('h1').screenshot_as_png,
                  attachment_type=allure.attachment_type.PNG)

    assert page_header == expected_header, f"Incorrect Page header {page_header}"


@allure.title("Navigation from Library drop-down: Verify library pages are displayed in UA")
@pytest.mark.parametrize("menu_item, expected_header", (
        ("Development", "Розробка"),
        ("Design", "Дизайн"),
        ("Business", "Бізнес"),
        ("Personal", "Особистий розвиток"),
        ("Marketing", "Маркетинг"),
        ("Language", "Мови"),
        ("Lifestyle", "Здоровя та спосіб життя"),
        ("Arts", "Мистецтво")))
def test_library_pages_UA(start_page, menu_item, expected_header):

    Config.logger.info(f"Open library page {menu_item} and expecting page header {expected_header}")

    start_page.select_locale('UA')
    start_page.select_library_item(menu_item)
    page_header = start_page.driver.find_element_by_tag_name('h1').text

    allure.attach(start_page.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    assert page_header == expected_header, f"Incorrect Page header {page_header}"


@allure.title("Bookmark a first course from recommended on Home screen")
@pytest.mark.parametrize("email, password", [("ia6x@yahoo.com", 123456789)])
def test_add_bookmark(start_page, email, password):

    Config.logger.info(f"Adding a to the bookmarks for account {email}")

    signin_page = start_page.click_signin_link()

    signin_page.enter_email(email)
    signin_page.enter_password(password)

    main_page = signin_page.login()

    main_page.click_bookmark()

    bookmarks_page = main_page.go_to_bookmarks()

    assert main_page.recommended_course_name == bookmarks_page.bookmarked_course_name, f"Course {main_page.recommended_course_name} is not bookmarked"
