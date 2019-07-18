import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

"""
#фикстура browser, которая создает нам экземпляр браузера для тестов в данном файле - перенесена в файл 'conftest.py'
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

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestLogin(object):
    def test_feedback(self, browser, lesson):
        link = "https://stepik.org/lesson/{}/step/1".format(lesson)
        answer = str(math.log(int(time.time())))
        browser.get(link)

        input1 = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        input1.send_keys(answer)

        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()

        feed_lmnt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
        feed = feed_lmnt.text
        assert feed == "Correct!", "Should be Correct"
