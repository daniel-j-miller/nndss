#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
from bs4 import BeautifulSoup
import csv
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('chromedriver',options=options)

col_headings = ['YEAR', 'ACT', 'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA', 'Aust', 'condition', 'updated']

with open("/home/pi/nndss/data/count_jur.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(col_headings)

driver.get("http://www9.health.gov.au/cda/source/rpt_4_sel.cfm")
soup = BeautifulSoup(driver.page_source, 'html.parser')
causeList = {}
table = soup.find('select')
rows = table.find_all('option')

for tag in rows:
	idNo = tag.get('value')
	cause = tag.text.strip()
	causeList[idNo] = cause  

for key in causeList:
	report = driver.find_element_by_id("REPORT_OPTION_1")
	report.click()
	elem = driver.find_element_by_name("CAUSE")
	elem.send_keys(causeList[key])
	button = driver.find_element_by_name("CTIME1")
	button.click()
	time.sleep(3)

	soup = BeautifulSoup(driver.page_source, 'html.parser')
	#table = driver.find_element_by_css_selector("#content > div:nth-child(1) > div > div > table")
	table = soup.find('table')
	#updated = driver.find_elements_by_class_name("publish-date")
	updated = soup.find("p", class_ = "publish-date").getText().strip()

	# find all rows
	rows = table.findAll('tr')

	# init row text array
	row_text_array = []

	# loop through rows and add row text to array
	for row in rows[1:]:
		row_text = []
		# loop through the elements
		for row_element in row.findAll(['th', 'td']):
			# append the array with the elements inner text
			row_text.append(row_element.text.replace('\n', '').strip())
		# append the text array to the row text array
		row_text_array.append(row_text)


	with open("/home/pi/nndss/data/count_jur.csv", "a") as f:
		wr = csv.writer(f)
		# loop through each row array
		for row_text_single in row_text_array:
			wr.writerow(row_text_single + [key, updated])

	driver.get("http://www9.health.gov.au/cda/source/rpt_4_sel.cfm")
	time.sleep(2)


with open("/home/pi/nndss/data/rate_jur.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(col_headings)

for key in causeList:
	report = driver.find_element_by_id("REPORT_OPTION_2")
	report.click()
	elem = driver.find_element_by_name("CAUSE")
	elem.send_keys(causeList[key])
	button = driver.find_element_by_name("CTIME1")
	button.click()
	time.sleep(3)

	soup = BeautifulSoup(driver.page_source, 'html.parser')
	#table = driver.find_element_by_css_selector("#content > div:nth-child(1) > div > div > table")
	table = soup.find('table')
	#updated = driver.find_elements_by_class_name("publish-date")
	updated = soup.find("p", class_ = "publish-date").getText().strip()

	# find all rows
	rows = table.findAll('tr')

	# init row text array
	row_text_array = []

	# loop through rows and add row text to array
	for row in rows[1:]:
		row_text = []
		# loop through the elements
		for row_element in row.findAll(['th', 'td']):
			# append the array with the elements inner text
			row_text.append(row_element.text.replace('\n', '').strip())
		# append the text array to the row text array
		row_text_array.append(row_text)


	with open("/home/pi/nndss/data/rate_jur.csv", "a") as f:
		wr = csv.writer(f)
		# loop through each row array
		for row_text_single in row_text_array:
			wr.writerow(row_text_single + [key, updated])

	driver.get("http://www9.health.gov.au/cda/source/rpt_4_sel.cfm")
	time.sleep(2)

############################
############################

col_headings = ['YEAR', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Total', 'condition', 'updated']

with open("/home/pi/nndss/data/count_aus.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(col_headings)

driver.get("http://www9.health.gov.au/cda/source/rpt_3_sel.cfm")
soup = BeautifulSoup(driver.page_source, 'html.parser')

for key in causeList:
	report = driver.find_element_by_id("REPORT_OPTION_1")
	report.click()
	elem = driver.find_element_by_name("CAUSE")
	elem.send_keys(causeList[key])
	button = driver.find_element_by_name("submit")
	button.click()
	time.sleep(3)

	soup = BeautifulSoup(driver.page_source, 'html.parser')
	#table = driver.find_element_by_css_selector("#content > div:nth-child(1) > div > div > table")
	table = soup.find('table')
	#updated = driver.find_elements_by_class_name("publish-date")
	updated = soup.find("p", class_ = "publish-date").getText().strip()

	# find all rows
	rows = table.findAll('tr')

	# init row text array
	row_text_array = []

	# loop through rows and add row text to array
	for row in rows[1:]:
		row_text = []
		# loop through the elements
		for row_element in row.findAll(['th', 'td']):
			# append the array with the elements inner text
			row_text.append(row_element.text.replace('\n', '').strip())
		# append the text array to the row text array
		row_text_array.append(row_text)


	with open("/home/pi/nndss/data/count_aus.csv", "a") as f:
		wr = csv.writer(f)
		# loop through each row array
		for row_text_single in row_text_array:
			wr.writerow(row_text_single + [key, updated])

	driver.get("http://www9.health.gov.au/cda/source/rpt_3_sel.cfm")
	time.sleep(2)

col_headings = ['YEAR', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'condition', 'updated']

with open("/home/pi/nndss/data/rate_aus.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(col_headings)

for key in causeList:
	report = driver.find_element_by_id("REPORT_OPTION_2")
	report.click()
	elem = driver.find_element_by_name("CAUSE")
	elem.send_keys(causeList[key])
	button = driver.find_element_by_name("submit")
	button.click()
	time.sleep(3)

	soup = BeautifulSoup(driver.page_source, 'html.parser')
	#table = driver.find_element_by_css_selector("#content > div:nth-child(1) > div > div > table")
	table = soup.find('table')
	#updated = driver.find_elements_by_class_name("publish-date")
	updated = soup.find("p", class_ = "publish-date").getText().strip()

	# find all rows
	rows = table.findAll('tr')

	# init row text array
	row_text_array = []

	# loop through rows and add row text to array
	for row in rows[1:]:
		row_text = []
		# loop through the elements
		for row_element in row.findAll(['th', 'td']):
			# append the array with the elements inner text
			row_text.append(row_element.text.replace('\n', '').strip())
		# append the text array to the row text array
		row_text_array.append(row_text)


	with open("/home/pi/nndss/data/rate_aus.csv", "a") as f:
		wr = csv.writer(f)
		# loop through each row array
		for row_text_single in row_text_array:
			wr.writerow(row_text_single + [key, updated])

	driver.get("http://www9.health.gov.au/cda/source/rpt_3_sel.cfm")
	time.sleep(2)

os.system("cd /home/pi/nndss && git add . && git commit -m 'automated commit' && git push")

print("Completed job without error!")
