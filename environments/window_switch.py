from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

first_window = browser.window_handles[0] #имя первого окна
new_window = browser.window_handles[1] #имя нового, открытого окна
browser.switch_to.window(new_window) #переключение на другое окно

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)
time.sleep(1)

button_confirm = browser.find_element_by_css_selector("button.btn")
button_confirm.click()
