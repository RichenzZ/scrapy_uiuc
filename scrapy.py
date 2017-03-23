
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumrequests import Firefox
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


my_email = "nlyu2@illinois.edu"
my_pass = "l7erfe3n"

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 10:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return

def start():
	html = urlopen("http://www.uialumninetwork.org/directory.html")
	bsObj = BeautifulSoup(html, "html.parser")
	allText = bsObj.findAll("input",{"name":"checksum"})
	checksum=allText[0]['value']
	url="https://secure31.omnimagnet.com/uialumninetwork.org/magnet_sso.php?checksum="+checksum
	return url


def login(driver):

	button = driver.find_element_by_id("yes_pass")
	email = driver.find_element_by_id("email")
	password = driver.find_element_by_id("password")

	email.send_keys(my_email)
	password.send_keys(my_pass)

	button.click()
	continu = driver.find_element_by_xpath("//div[@alt='UIAA Alumni Sign-in Here']")
	continu.click()
	return



url = start()

driver = Firefox()
driver.get(url)

login(driver)
waitForLoad(driver)
directory_button=driver.find_element_by_xpath("//a[@href='http://www.uialumninetwork.org/directory.html']")
directory_button.click()
waitForLoad(driver)
company_text=driver.find_element_by_id("work_company2")
company_text.send_keys("")
company_button=driver.find_element_by_xpath("//div[@id='search_geography']")
company_button.click()
waitForLoad(driver)
result_text=driver.find_elements_by_class_name("result")
for i in result_text:
	print(i.text, '\n')
cur_html=driver.page_source
#print(driver.current_url)
#print(cur_html)
driver.close()