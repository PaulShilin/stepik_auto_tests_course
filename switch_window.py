from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

btn_troll = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary')
btn_troll.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

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