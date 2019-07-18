import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
link = "http://selenium1py.pythonanywhere.com/ru/"
def test_exception():
    browser.get(link)
    time.sleep(1)
    print(browser.get)
    with pytest.raises(NoSuchElementException, match = "Не должно быть кнопки Отправить"):
        browser.find_element_by_css_selector("button.btn")
