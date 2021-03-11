from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = '/Users/jeonjeonghun/Documents/python/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('http://www.python.org')

elem = driver.find_element_by_name('q')

elem.clear()

elem.send_keys('python')

elem.send_keys(Keys.RETURN)



