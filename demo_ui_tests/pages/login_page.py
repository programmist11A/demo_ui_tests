import allure
from selene import have, command, be
from selene.support.shared import browser

from demo_ui_tests.constants import profile_page_url, login_page_error_message, login_page_url, user_name


class LoginPage:
    def open(self):
        with allure.step('Open login page'):
            browser.open('/login')
            browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
                have.size_greater_than_or_equal(3)
            )
            browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_user_name(self, value):
        with allure.step(f'Enter username "{value}"'):
            browser.element('#userName').type(value)

    def fill_password(self, value):
        with allure.step(f'Enter password "{value}"'):
            browser.element('#password').type(value)

    def click_login(self):
        with allure.step('Click Login button'):
            browser.element('#login').click()

    def verify_profile_url_open(self, url=profile_page_url):
        with allure.step(f'Verify that user profile page opened, url: "{url}"'):
            browser.should(have.url(url))

    def verify_profile_page_open(self):
        with allure.step(f'Verify that user profile page opened'):
            browser.element('//div[contains(@class, "main-header") and text()="Profile"]').should(be.visible)

    def verify_login_page_open(self):
        with allure.step('Verify that login page opened'):
            browser.element('//div[contains(@class, "main-header") and text()="Login"]').should(be.visible)

    def verify_login_url_open(self, url=login_page_url):
        with allure.step(f'Verify that login page opened, url: "{url}"'):
            browser.should(have.url(url))

    def verify_user_label(self, value=user_name):
        with allure.step(f'Verify that user label on profile page is: "{value}"'):
            browser.element('#userName-value').should(have.exact_text(value))

    def verify_error_messge(self, value=login_page_error_message):
        with allure.step(f'Verify that error message shown on login page: "{value}"'):
            browser.element('#name').should(have.exact_text(value))

    def verify_you_already_logged_in_text(self, value="You are already logged in"):
        with allure.step(f'Verify that text "{value}" shown on login page'):
            browser.element('#loading-label').should(have.text(value))