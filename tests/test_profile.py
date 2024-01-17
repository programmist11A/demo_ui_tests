import allure
from allure_commons.types import Severity

from demo_ui_tests.pages.books_page import BooksPage
from demo_ui_tests.pages.login_page import LoginPage
from demo_ui_tests.pages.profile_page import ProfilePage

pytestmark = [
    allure.label('layer', 'UI tests'),
    allure.label('owner', 'anton_fomin'),
    allure.epic('BookStore Web'),
    allure.tag('web'),
    allure.feature('Profile page')
]


profile_page = ProfilePage()
login_page = LoginPage()
books_page = BooksPage()

@allure.title("Logout after login")
@allure.severity(Severity.CRITICAL)
def test_profile_logout(login_to_book_store):
    # WHEN
    profile_page.click_log_out_button()
    # THEN
    login_page.verify_login_url_open()
    login_page.verify_login_page_open()

@allure.title("Login form not available after login")
@allure.severity(Severity.NORMAL)
def test_login_page_not_available_for_logged_user(login_to_book_store):
    # WHEN
    profile_page.click_login_menu()
    # THEN
    login_page.verify_login_url_open()
    login_page.verify_login_page_open()
    login_page.verify_you_already_logged_in_text()