from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);") #скрипт скрола страницы на 100 пикселей вниз

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()

option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()
time.sleep(1)

button = browser.find_element_by_css_selector("button.btn")
button.click()
