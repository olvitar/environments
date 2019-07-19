import pytest
from selenium import webdriver

#фикстура browser, которая создает нам экземпляр браузера для тестов в данном файле
@pytest.fixture(scope="class")
def browser(request):
    print("\n start browser for test..")
    browser = webdriver.Chrome()

    def fin():
        print("\n quilt browser")
        browser.close( )

    request.addfinalizer(fin)
    return browser

"""
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
"""

@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin(object):
    def test_guest_should_see_login_link(self, browser, language):
        link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
        # этот тест тоже запустится дважды
        assert True
