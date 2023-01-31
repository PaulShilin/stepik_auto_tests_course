from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

btn_book = browser.find_element(By.ID, 'book')
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '100')
)
btn_book.click()

numb = browser.find_element(By.ID, 'input_value')
numb = int(numb.text)
def calc(numb):
  return str(math.log(abs(12*math.sin(int(numb)))))
answ = calc(numb)

inp1 = browser.find_element(By.ID, 'answer')
inp1.send_keys(answ)

button_submit = browser.find_element(By.ID, 'solve')
#time.sleep(1)
button_submit.click()

time.sleep(60)