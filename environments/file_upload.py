from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла
print(current_dir)
print(file_path)


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
name = browser.find_element_by_name("firstname")
name.send_keys("Ivan")

surname = browser.find_element_by_name("lastname")
surname.send_keys("Petrov")

email = browser.find_element_by_name("email")
email.send_keys("mail@test.ru")

upload_button = browser.find_element_by_id("file") #находим кнопку загрузки файла
upload_button.send_keys(file_path) #отправляем файл file.txt, который находится в директории даного скрипта
time.sleep(1)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

