from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('chromedriver', options=options)

driver.get("http://www9.health.gov.au/cda/source/rpt_4_sel.cfm")

soup = BeautifulSoup(driver.page_source)

table = soup.find('select')

rows = table.find_all('option')

with open("data/causeList.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(["idNo", "cause"])
    for tag in rows:
        idNo = tag.get('value')
        cause = tag.text.strip()
        wr.writerow([idNo, cause])

driver.quit()