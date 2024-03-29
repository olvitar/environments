import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture()
def browser(request):
    print("\n start browser for test..")
    browser = webdriver.Chrome()

    def fin():
        print("\n quilt browser")
        browser.close( )

    request.addfinalizer(fin)
    return browser

class TestMainPage1(object):
     # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")
