from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys, os

driver =  webdriver.Chrome('../driver/chromedriver.exe')


url = 'https://google.co.kr'
driver.get(url)
# driver.implicitly_wait(3)
# driver.fullscreen_window() #전체
# time.sleep(1)
# driver.maximize_window() #최대

driver.set_window_rect(0,0,500,500)

print(driver.get_window_rect())

time.sleep(3)
driver.quit()