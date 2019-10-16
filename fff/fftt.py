#!/usr/bin/python
#-*-coding:utf8-*-

import requests
from pyquery import PyQuery as pq
response = requests.get('http://www.quanshuwang.com/book/1/1612')
response.encoding = response.apparent_encoding
doc = pq(response.text)
links = doc('div >li a')
for link in links.items():
    print('http://www.quanshuwang.com/book/1/1612'+link.attr.href)



    response = requests.get('http://www.quanshuwang.com/book/1/1612'+link.attr.href)
    response.encoding = response.apparent_encoding
    #print(response.text)
    doc = pq(response.text)
    title = doc('.bookInfo > h1:nth-child(1)').text()
    content = doc('#content').text()

    # print(title)
    # print(content)
    with open('很纯很爱昧.txt',mode='a+',encoding='utf-8') as f:
        f.write(title)
        f.write(content)
        f.write('\n')

