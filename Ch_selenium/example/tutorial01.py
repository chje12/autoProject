from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver =  webdriver.Chrome('../driver/chromedriver.exe')

url = 'https://google.co.kr'
driver.implicitly_wait(3)

driver.get(url)


time.sleep(5)
driver.quit()