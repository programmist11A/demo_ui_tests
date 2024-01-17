import allure
from selene import have, command, by, be
from selene.support.shared import browser


class BooksPage:
    def open(self):
        with allure.step('Open books page'):
            browser.open('/books')
            browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
                have.size_greater_than_or_equal(3)
            )
            browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def verify_book_titles(self, *titles):
        with allure.step(f'Verify books titles: {titles}'):
            browser.all('[id^=see-book]').should(
                have.exact_texts(titles))

    def input_search_text(self, search_string):
        with allure.step(f'Search book with keyword: {search_string}'):
            browser.element('#searchBox').type(search_string)

    def click_book(self, book_title):
        with allure.step(f'Click book title: {book_title}'):
            browser.all('[id^=see-book]').element_by(have.exact_text(book_title)).click()

    def verify_book_properties_page_url_opened(self, value='https://demoqa.com/books?book=9781449325862'):
        with allure.step('Verify book properties page opened'):
            browser.should(have.url(value))

    def verify_book_properties_page_opened(self):
        with allure.step('Verify book properties page opened'):
            browser.element('#ISBN-wrapper').should(be.visible)

    def verify_book_data(self, *data):
        with allure.step('Verify book data'):
            browser.all('[id^="userName"]').should(
                have.exact_texts(data))

    def verify_no_books_found(self):
        with allure.step('Verify no books shown'):
            browser.element('.rt-noData').should(have.exact_text('No rows found'))

    def click_add_to_your_collection_button(self):
        with allure.step('Click add to your collection button'):
            browser.element(by.text('Add To Your Collection')).click()