#!/usr/bin/python3

import urllib.request
from bs4 import BeautifulSoup

import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def data(keyword):
    try:
        page = urllib.request.urlopen("https://www.snerpa.is/net/snorri/gylf.htm")
    except:
        return "Page not found :("

    soup = BeautifulSoup(page, "lxml")
    #contents = soup.body.find('b.child(div)')
    kaflaheiti = [remove_tags(str(x)) for x in soup.body.find_all('b')[1:-1]]

    kaflar = [list() for i in range(len(kaflaheiti)+1)]
    kafli = 0
    for line in soup.body.text.split("\n"):
        isChapter = False
        for heiti in kaflaheiti:
            if heiti in line:
                kafli += 1
                isChapter = True
                break
        if not isChapter:
            line = line.replace('\r', '')
            kaflar[kafli].append(line)

    for i in range(1, len(kaflaheiti)+1):
        kaflar[i] = ("\n").join(kaflar[i])

    #print(("\n").join(kaflar))

    result = ""

    for i in range(1, len(kaflaheiti)+1):
        if keyword in kaflar[i]:
            result += str(i)
            result += ". kafli \n \n"
            result += kaflar[i]
            result += "\n \n"
    print(result)

    if result != "":
        return result
    else: "Fannst ekki!"
    #if str(names[i].encode('utf-8')) != "" and "1" not in str(names[i].encode('utf-8')):



data("Baldur")

