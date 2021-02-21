from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys, os

driver =  webdriver.Chrome('../driver/chromedriver.exe')
driver.implicitly_wait(3)


url = 'https://google.co.kr'
driver.get('https://www.google.co.kr')
driver.get('https://www.naver.co.kr')
driver.get('https://www.youtube.com/c/반원')


driver.back()
time.sleep(.5)
driver.back()
time.sleep(.5)

driver.forward()
time.sleep(.5)
driver.forward()
time.sleep(.5)


time.sleep(3)
driver.quit()