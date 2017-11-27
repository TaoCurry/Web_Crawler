#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
爬取商品标题、价格、区域和发帖时间
"""
__author__ = "Curry"

from bs4 import BeautifulSoup
import requests

url = 'http://bj.58.com/pingbandiannao/31804057080125x.shtml'


wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')


def get_links_from_list(strings=0):
    urls = []
    list_view = 'http://bj.58.com/pingbandiannao/{}/'.format(str(strings))    # 判断是商家还是个人页面
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.select('a.t'):
        urls.append(link.get('href'))
    return urls


def get_views_from(url):
    id = url.split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api)
    views = js.text.split('=')[-1]
    print(views)



def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.title.text
    price = soup.select('#content span.price')  # 搜索唯一描述元素的标签
    time = soup.select('.time')
    area = soup.select('.c_25d')


    data = {
        'title': title,
        'price': price[0].text,
        'time': time[0].text,
        'area': list(area[0].stripped_strings),
        'cate': None,
        'view': None
    }
    print(data)



# get_item_info(url)
# get_links_from_list(0)
get_views_from('http://bj.58.com/pingbandiannao/30223879694911x.shtml?adtype=1&PGTID=0d305a36-0000-1919-c93a-e6556537329b&entinfo=30223879694911_0&psid=160592680198153067397919988&iuType=_undefined&ClickID=1')
