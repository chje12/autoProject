from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys, os

driver =  webdriver.Chrome('../driver/chromedriver.exe')
driver.implicitly_wait(3)


url = 'https://google.co.kr'
driver.get('https://www.naver.co.kr')

search = driver.find_element_by_css_selector('#query')
search.send_keys('고슴도치')
# search.send_keys(Keys.ENTER)

btn = driver.find_element_by_css_selector('#search_btn')
btn.click()


time.sleep(3)
driver.quit()