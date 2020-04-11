from selenium import webdriver
from selenium.webdriver.common.keys import Keys

site = input("Enter the site you want to search: ")

driver = webdriver.Chrome()
driver.get('https://www.'+site+'.com')