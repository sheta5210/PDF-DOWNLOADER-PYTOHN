import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import json
from bs4 import BeautifulSoup, NavigableString, Tag
import datetime

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

wd = webdriver.Chrome("chromedriver.exe")
wd.maximize_window()
wd.get("https://www.osc.ca/en/securities-law/osc-bulletin?keyword=61-101&date%5Bmin%5D=&date%5Bmax%5D=&sort_bef_combine=field_start_date_DESC")

link = []
i = 1

for r in range(10, 300):
    if i % 3 == 0:
        r = r+1
    desc = wd.find_elements_by_xpath(
        f'//*[@id="block-osc-glider-content"]/article/section[3]/div[2]/section[3]/div/div/div/div/div[2]/div/div[3]/div/div[2]/div[' + str(r) + ']/div/div[1]/div[2]/span[1]/a')


    for test in desc:
        try:

            print(test.get_attribute("href"))

            link.append(test.get_attribute("href"))

        except:
            print("yyyy")

i = i+1


data = json.dumps(link)

with open(f"link.json", "w") as outfile:
    outfile.write(data)
