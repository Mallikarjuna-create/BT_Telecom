from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.bt.com/')
time.sleep(30)
driver.switch_to.alert.accept()
actions = ActionChains(driver)
obj = driver.find_element(By.XPATH('//*[@id="bt-navbar"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[4]/a/span'))
actions.move_to_element(obj)
driver.execute_script("window.scrollTo(0,200)")
driver.find_element(By.XPATH('//*[@id="bt-navbar"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[4]/a/span')).click()
driver.switch_to.alert.accept()
driver.find_element(By.XPATH('//*[@id="fef-contents-with-footer"]/div[1]/div/div/div/div[2]/div/div[2]/div/div/div/a[3]')).click()
title = driver.title
assert title == "Exclusive EE Mobiles deals for BT Broadband customers ee.co.uk"
driver.close()
