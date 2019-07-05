from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

inp_val = browser.find_element_by_id("treasure")
x_element = inp_val.get_attribute("valuex")
y = calc(x_element)
#print(x_element)

input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()

option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()
time.sleep(1)

button = browser.find_element_by_css_selector("button.btn")
button.click()
