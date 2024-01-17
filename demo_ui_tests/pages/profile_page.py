import allure
from selene import browser, command, have, by


class ProfilePage:
    def open(self):
        with allure.step('Open profile page'):
            browser.open('/profile')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def click_log_out_button(self):
        with allure.step('Click Log out'):
            browser.element(by.text('Log out')).click()

    def click_login_menu(self):
        with allure.step('Open login page'):
            browser.element(by.text('Login')).click()