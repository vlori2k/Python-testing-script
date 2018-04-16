from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:\path\chromedriver.exe')
driver.get('https://www.facebook.com/')

username_box = driver.find_element_by_id('email')
username_box.send_keys("Type your email inside here")
time.sleep(1)
passElem = driver.find_element_by_id("pass")
passElem.send_keys("Type your password inside here")
time.sleep(1)
passElem.send_keys(Keys.RETURN)
time.sleep(3)
userTargetUrl = "https://www.facebook.com/messages/t/" + "Type your friend`s user ID here, example: daniel.smith23"
driver.get(userTargetUrl)


elem = driver.find_element(By.XPATH, '//div[@class="notranslate _5rpu"]')


elem.send_keys("Python-Script-test-Completed")

elem.send_keys(Keys.RETURN)
driver.find_element_by_id("u_0_t").click()