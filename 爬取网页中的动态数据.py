#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
异步加载
"""
__author__ = "Curry"

from bs4 import BeautifulSoup
import requests

url = 'https://movie.douban.com/tv/#!type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start=0'




wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

name = soup.select('#content > div > div.article > div > div.list-wp > div > a:nth-child(17) > p')
print(name)


'''
    for question in questions:
        print(question.get_text())

def get_more_page(start, end):
    for
'''