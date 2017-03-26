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

def waitForLoad(driver, wait_time):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > wait_time:
            return
        time.sleep(1)
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

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver = webdriver.Firefox(firefox_profile=firefox_profile)

url = "https://www.linkedin.com"

#driver = Firefox()
driver.get(url)

login(driver)
waitForLoad(driver, 1.0)

driver.get("https://www.linkedin.com/school/2650/alumni?filterByOption=graduated")
waitForLoad(driver, 1.0)

start= time.time()

while(True):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	waitForLoad(driver, 0.7)
	end = time.time()
	if(end - start >= 3):
		break

name_button=driver.find_elements_by_xpath("//a[@class='Sans-17px-black-85%-semibold']")
window_main = driver.window_handles[0]
for i in range(0, len(name_button)):
	name_button[i+2].click()
	waitForLoad(driver, 1.0)
	window_cur = driver.window_handles[1]
	driver.switch_to_window(window_cur)
	waitForLoad(driver, 1.0)

	driver.execute_script("window.scrollTo(0, 1000);")

	waitForLoad(driver, 2.0)
	result_main = driver.find_element_by_xpath("//section[@class='pv-profile-section experience-section ember-view']")
	
	#result_main = result_main1.find_element_by_xpath("//ul[@class='pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more']")
	#print(result_main.text)
	result_text = result_main.find_elements_by_xpath("//h3[@class='Sans-17px-black-85%-semibold']")
	result_text1 = result_main.find_elements_by_xpath("//span[@class='pv-entity__secondary-title Sans-15px-black-55%']")

	print(len(result_text), len(result_text1))
	for j in range(0, min(len(result_text), len(result_text1))):
		name_card = result_text[j].text + '\n' 
		name_card = name_card + result_text1[j].text + '\n'
		print(name_card)
		
	# name_card = result_text[0].text + '\n' 
	# name_card = name_card + result_text1[0].text + '\n'
	# print(name_card)
	driver.close()
	driver.switch_to_window(window_main)

#print(len(name_button))

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

driver.quit()
