from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button_start = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
button_start.click()

confirm = browser.switch_to.alert
confirm.accept()

numb = browser.find_element(By.ID, 'input_value')
numb = int(numb.text)
def calc(numb):
  return str(math.log(abs(12*math.sin(int(numb)))))
answ = calc(numb)

inp1 = browser.find_element(By.ID, 'answer')
inp1.send_keys(answ)

button_submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
button_submit.click()


time.sleep(60)