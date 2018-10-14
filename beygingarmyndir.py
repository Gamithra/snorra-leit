#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import urllib.request
from bs4 import BeautifulSoup
import re

def bin(link):
    try:
        options = Options()
        options.headless = True

        driver = webdriver.Firefox(firefox_options=options)
        driver.get(link)
        page = driver.page_source
        driver.quit()
    except: return "BÍN page not found"

    return page

def data(keyword):
    res = bin("http://bin.arnastofnun.is/leit/?q="+keyword+"&ordmyndir=on")
    soup = BeautifulSoup(res, "lxml")

    myndir = soup.body.find_all("span", {"class": "VO_beygingarmynd"})

    if myndir == []:
        strong = soup.body.find_all("strong")
        for s in strong:
            if "href" in str(s):
                leit = re.findall("'([^' ]+)'", str(s))[0]
                res = bin("http://bin.arnastofnun.is/leit/?id=" + leit)

                soup = BeautifulSoup(res, "lxml")
                for r in soup.body.find_all("span", {"class": "VO_beygingarmynd"}):
                    myndir.append(r)

    for i in range(len(myndir)):
        #leit = re.findall("'([^ ]+)'", str(s))[0]
        myndir[i] = myndir[i].text

    print(myndir)
    return myndir

kw = input()
print(data(kw))
