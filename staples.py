#This script requires the python selenium bindings, as well as lxml.

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from lxml import html

# Start the WebDriver and load the page
browser = webdriver.Firefox()
browser.get('http://omni.staples.com/staples-2_1/index.html?category=printers#0')

def click_div(element_xpath):
	
	#wait until the element has loaded
	WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, element_xpath)))
	
	#Used to throttle Selenium on unreliable internet connections.
	#You should get a speed boost if you remove or reduce it, but it
	#might also give you intermittent errors where a click randomly
	#won't register, or it will register on the wrong div.
	#
	#Don't say I didn't warn you.
	time.sleep(2)
	
	#click the element
	browser.find_element_by_xpath(element_xpath).click()

	
click_div("//*[@data-answerid='1']")
click_div("//*[@data-answerid='19']")
click_div("//*[@data-answerid='28']")
click_div("//*[@class='popupBtn column medium-3']")
click_div("//*[@data-answerid='52']/following-sibling::*[2]")
click_div("//*[@data-answerid='53']/following-sibling::*[2]")
click_div("//*[@class='close btn']")

#Turns the resulting source into something lxml can parse
tree = html.fromstring(browser.page_source)

for element in range(len(tree.xpath('//*[@id="products"]/div/@data-productid'))):
	
	print tree.xpath('//*[@id="products"]/div/div/div/div[@class="resultItemNumber"]/text()')[element]
	print tree.xpath('//*[@id="products"]/div/div/div/div[@class="resultModelNumber"]/text()')[element]
	print tree.xpath('//*[@id="products"]/div/@data-producttitle')[element]
	print ""
	
print len(tree.xpath('//*[@id="products"]/div/@data-productid')), "items from the website."

