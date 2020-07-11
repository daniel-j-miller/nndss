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

col_headings = ['condition', 'ACT', 'NSW', 'NT', 'Qld', 'SA', 'Tas', 'Vic', 'WA', 'Aust', 'Aust YTD', "month", "year",'updated']

years = list(map(str, range(1991,2021)))
months = list(map(str, range(1,13)))

with open("data/detail_count.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(col_headings)


driver.get("http://www9.health.gov.au/cda/source/rpt_1_sel.cfm")

for y in years:
    for m in months:

        report = driver.find_element_by_id("REPORT_TYPE_b")
        report.click()
        month = driver.find_element_by_name("Sel_Month")
        month.send_keys(m)
        year = driver.find_element_by_name("Sel_Year")
        year.send_keys(y)
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
            for row_element in row.findAll(['td']):
                # append the array with the elements inner text
                row_text.append(row_element.text.replace('\n', '').strip())
            # append the text array to the row text array
            row_text_array.append(row_text)


        with open("data/detail_count.csv", "a") as f:
            wr = csv.writer(f)
            # loop through each row array
            for row_text_single in row_text_array:
                wr.writerow(row_text_single + [m, y, updated])

        driver.get("http://www9.health.gov.au/cda/source/rpt_1_sel.cfm")
        time.sleep(3)

