import allure
from allure_commons.types import Severity

from demo_ui_tests.pages.books_page import BooksPage

pytestmark = [
    allure.label('layer', 'UI tests'),
    allure.label('owner', 'anton_fomin'),
    allure.epic('BookStore Web'),
    allure.tag('web'),
    allure.feature('Books page')
]

books_page = BooksPage()


@allure.title('Verify search by keyword in book title')
@allure.severity(Severity.BLOCKER)
def test_search_book_by_title():
    # GIVEN
    books_page.open()
    books_page.verify_book_titles('Git Pocket Guide', 'Learning JavaScript Design Patterns',
                                  'Designing Evolvable Web APIs with ASP.NET',
                                  'Speaking JavaScript', "You Don't Know JS",
                                  'Programming JavaScript Applications',
                                  'Eloquent JavaScript, Second Edition',
                                  'Understanding ECMAScript 6')
    # WHEN
    books_page.input_search_text('Java')
    # THEN
    books_page.verify_book_titles('Learning JavaScript Design Patterns',
                                  'Speaking JavaScript',
                                  'Programming JavaScript Applications',
                                  'Eloquent JavaScript, Second Edition')


@allure.title('Verify search by keyword with no books found')
@allure.severity(Severity.CRITICAL)
def test_search_book_by_title_no_results():
    # GIVEN
    books_page.open()
    books_page.verify_book_titles('Git Pocket Guide', 'Learning JavaScript Design Patterns',
                                  'Designing Evolvable Web APIs with ASP.NET',
                                  'Speaking JavaScript', "You Don't Know JS",
                                  'Programming JavaScript Applications',
                                  'Eloquent JavaScript, Second Edition',
                                  'Understanding ECMAScript 6')
    # WHEN
    books_page.input_search_text('qwerty123')
    # THEN
    books_page.verify_no_books_found()
    books_page.verify_book_titles()


@allure.title('Verify search by author')
@allure.severity(Severity.BLOCKER)
def test_search_book_by_author():
    # GIVEN
    books_page.open()
    # WHEN
    books_page.input_search_text('Kyle')
    # THEN
    books_page.verify_book_titles("You Don't Know JS")

@allure.title('Open book details page')
@allure.severity(Severity.CRITICAL)
def test_open_book():
    # GIVEN
    books_page.open()
    # WHEN
    books_page.click_book('Git Pocket Guide')
    # THEN
    books_page.verify_book_properties_page_url_opened()
    books_page.verify_book_properties_page_opened()
    books_page.verify_book_data('9781449325862',
                                'Git Pocket Guide',
                                'A Working Introduction',
                                'Richard E. Silverman',
                                "O'Reilly Media",
                                '234',
                                "This pocket guide is the perfect on-the-job companion to Git, the distributed "
                                "version control system. It provides a compact, readable introduction to Git for new "
                                "users, as well as a reference to common commands and procedures for those of you "
                                "with Git exp",
                                'http://chimera.labs.oreilly.com/books/1230000000561/index.html')