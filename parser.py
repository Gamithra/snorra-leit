#!/usr/bin/python3

import urllib.request
from bs4 import BeautifulSoup
import beygingarmyndir

import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def word(keyword):
    return beygingarmyndir.data(keyword)

def data(keyword):
    try:
        page = urllib.request.urlopen("https://www.snerpa.is/net/snorri/gylf.htm")
    except:
        return "Page not found :("

    words = beygingarmyndir.data(keyword)
    soup = BeautifulSoup(page, "lxml")

    kaflaheiti = [remove_tags(str(x)) for x in soup.body.find_all('b')[1:-1]]
    kaflar = [list() for i in range(len(kaflaheiti)+1)]
    kafli = 0

    for line in soup.body.find_all("p"):
        isChapter = False
        for heiti in kaflaheiti:
            if heiti in line.text:
                kafli += 1
                isChapter = True
                break
        if not isChapter:
            line = line.text
            line = line.replace('\r', '')
            line = line.replace('\n', '')
            kaflar[kafli].append(line)

    result = []

    for i in range(1, len(kaflaheiti)+1):
        for w in words:
            if re.search(w, "\n".join(kaflar[i]), re.IGNORECASE):
                rs = []
                rs.append(str(i) + ". kafli ")
                rs.append(kaflar[i])
                result.append(rs)
                break

    if result != "":
        return result
    else: return "Fannst ekki!"



#kw = input()
#data(kw)
