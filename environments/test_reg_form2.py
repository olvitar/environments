import time
import unittest
from selenium import webdriver


class TestForms(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def fill_form(self, url):
        """
        Вспомогательный метод для заполнения форм
        """
        input_fields = ('.first_block .first', '.first_block .second',
                        '.first_block .third')
        values = ('Ivan', 'Ivanov', 'ivan@test.com')
        self.browser.get(url)

        for selector, value in zip(input_fields, values):
            input_field = self.browser.find_element_by_css_selector(selector)
            input_field.send_keys(value)

        button = self.browser.find_element_by_css_selector('button.btn')
        button.click()

        time.sleep(1)
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        result = welcome_text_elt.text
        return result

    def test_registration1(self):
        form_url = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(form_url)
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!",
                         registration_result)

    def test_registration2(self):
        form_url = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(form_url)
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!",
                         registration_result)


if __name__ == '__main__':
    unittest.main()
