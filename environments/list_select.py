from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

num1_el = browser.find_element_by_id("num1")# ищем элемент
num1 = num1_el.text # преобразовываем веб-элемент в строку
num2_el = browser.find_element_by_id("num2")
num2 = num2_el.text
print(type(num1))
val = int(num1)+ int(num2)
print("sum is: ", val)
val = str(val) # преобразовываем число обратно в строку

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(val) # ищем элемент

time.sleep(1)

button = browser.find_element_by_css_selector("button.btn")
button.click()
