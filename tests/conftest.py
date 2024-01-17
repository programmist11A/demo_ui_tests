import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import project
from demo_ui_tests.constants import base_url_value, user_name, user_password
from demo_ui_tests.pages.login_page import LoginPage
from demo_ui_tests.utils import attach

base_url = base_url_value


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = project.config.base_url
    browser.config.window_width = project.config.window_width
    browser.config.window_height = project.config.window_height
    browser.config.timeout = project.config.timeout

    options = Options()
    selenoid_capabilities = {
        "browserName": project.config.driver_name,
        "browserVersion": project.config.browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{project.config.login}:{project.config.password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    if project.config.driver_name == 'chrome':
        attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope="function", autouse=False)
def login_to_book_store(login=user_name, password=user_password):
    login_page = LoginPage()
    # GIVEN
    login_page.open()
    login_page.fill_user_name(login)
    login_page.fill_password(password)
    login_page.click_login()
    login_page.verify_profile_page_open()