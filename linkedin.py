import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumrequests import Firefox
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


my_email = "nlyu2@illinois.edu"
my_pass = "756251901"


def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 10:
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return

def start():
	html = urlopen("https://www.linkedin.com")
	bsObj = BeautifulSoup(html, "html.parser")
	allText = bsObj.findAll("input",{"name":"checksum"})
	checksum=allText[0]['value']
	url="https://secure31.omnimagnet.com/uialumninetwork.org/magnet_sso.php?checksum="+checksum
	return url


def login(driver):

	email = driver.find_element_by_id("login-email")
	password = driver.find_element_by_id("login-password")
	button = driver.find_element_by_id("login-submit")

	email.send_keys(my_email)
	password.send_keys(my_pass)

	button.click()
	return


def sparce_text(i):
	i = i.replace('\nLife Member', '')
	i = i.replace('   ', '\n') 
	return i  


url = "https://www.linkedin.com"

driver = Firefox()
driver.get(url)

login(driver)
waitForLoad(driver)

driver.get("https://www.linkedin.com/school/2650/alumni?filterByOption=graduated")
# waitForLoad(driver)

# directory_button = driver.find_element_by_xpath("//a[@href='http://www.uialumninetwork.org/directory.html']")
# directory_button.click()

# waitForLoad(driver)

# company_text=driver.find_element_by_id("work_company2")
# company_text.send_keys("")

# company_button=driver.find_element_by_xpath("//div[@id='search_geography']")
# company_button.click()

# waitForLoad(driver)

# for page in range(5):
# 	result_text=driver.find_elements_by_class_name("result")
# 	for i in result_text:
# 		name_card = sparce_text(i.text)
# 		print(name_card, '\n')
	
# 	next_button=driver.find_elements_by_xpath("//div[@class='text_butt']")
# 	next_button[page].click()
# 	waitForLoad(driver)

# # result_text = driver.find_elements_by_class_name("result")
# # for i in result_text:
# # 	name_card = sparce_text(i.text)
# # 	print(name_card, '\n')
# cur_html=driver.page_source

driver.close()
