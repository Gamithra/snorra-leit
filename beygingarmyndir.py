#!/usr/bin/python3

import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
import re


def data(keyword):
    res = urllib.request.urlopen("http://dev.phpbin.ja.is/ajax_leit.php?q="+quote(keyword)+"&ordmyndir=on")
    soup = BeautifulSoup(res, "lxml")

    myndir = soup.body.find_all("span", {"class": "VO_beygingarmynd"})
    if myndir == []:
        strong = soup.body.find_all("strong")
        for s in strong:
            if "href" in str(s):
                leit = re.findall("'([^' ]+)'", str(s))[0]
                res = urllib.request.urlopen("http://dev.phpbin.ja.is/ajax_leit.php?id="+ leit)

                soup = BeautifulSoup(res, "lxml")
                for r in soup.body.find_all("span", {"class": "VO_beygingarmynd"}):
                    myndir.append(r)

    for i in range(len(myndir)):
        myndir[i] = myndir[i].text

    return myndir

'''test code

kw = input()
print(data(kw))


'''



'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options'''
'''
using selenium:

options = Options()
options.headless = True

driver = webdriver.Firefox(firefox_options=options)
driver.get(link)
page = driver.page_source
driver.quit()'''
