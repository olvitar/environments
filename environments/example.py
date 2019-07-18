from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()

def feedback(link):
    answer = str(math.log(int(time.time())))
    browser.get(link)

    input1 = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    input1.send_keys(answer)

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    feed_lmnt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
    feed = feed_lmnt.text
    print(feed)

link = "https://stepik.org/lesson/236895/step/1"
feedback(link)

feed_lmnt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
feed = feed_lmnt.text
assert "Correct!" == feed, "Should be 'Correct!'"
time.sleep(1)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
browser.quit()


