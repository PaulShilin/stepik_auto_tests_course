from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'Blabla.txt') 

input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
input1.send_keys('Blabla1')
input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
input2.send_keys('Blabla2')
input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
input3.send_keys('Blabla1@Blabla1mail.com')

ChooseFile = browser.find_element(By.ID, 'file')
ChooseFile.send_keys(file_path)

button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
button.click()

time.sleep(60)