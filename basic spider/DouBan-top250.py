# -*- coding: utf-8 -*-
# @Author  : Silas9187
# @Email    : silas9187@gmail.com
# @Site     : https://blog.csdn.net/acarsar
"""爬取豆瓣图书top250"""
from requests.exceptions import RequestException
from lxml import etree
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import requests
import time,json
# 1.分析url地址
#  2.分析网页源代码


def getPage(url):
    """爬取指定url地址的信息"""
    try:
            # 定义请求头信息
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
            # 执行爬取
            res = requests.get(url, headers=headers)
            if res.status_code ==200:
                # 返回爬取网页的内容
                return res.text
            else:
                return None
    except RequestException as e:
            print(e)
            return None


def parsePage(content):
    """解析爬取网页中的内容，并返回结果
    使用三种方法爬取 1.xpath 2.beautifulsoup 2.pyquery
    """
    '''
    # 1.使用Xpath解析内容
    # 初始化，返回根节点对象
    html = etree.HTML(content)
    # 解析网页中所需要的<tr class="item">...</tr>中的内容
    items = html.xpath("//tr[@class='item']")
    # print(len(items))
    # 遍历并解析每本图书的具体信息
    for item in items:
        yield {
            'title': item.xpath('normalize-space(.//a[@title]/text())'),  # 去除掉爬取内容中的空格换行用normalize-space()
            'image': item.xpath(".//img[@width='90']/@src")[0],
            'author': item.xpath(".//p[@class='pl']/text()")[0],
            'score': item.xpath(".//span[@class='rating_nums']/text()")[0],
        }
    '''
    '''
    # 2.使用BeautifulSoup解析内容
    # 初始化，返回BeautifulSoup对象(创建解析器)
    soup = BeautifulSoup(content, 'lxml')
    # 解析网页中所需要的<tr class="item">...</tr>中的内容
    items = soup.find_all(name="tr", attrs={'class': 'item'})
    # print(len(items))
    # 遍历并解析每本图书的具体信息
    for item in items:
        yield {
            'title': item.select("div.pl2 a")[0].get_text().strip().replace('\n', '').replace(' ', ''),
            'image': item.find(name='img', attrs={'width': '90'}).attrs['src'],
            'author': item.find(name='p', attrs={'class': 'pl'}).string,
            'score': item.find(name='span', attrs={'class': 'rating_nums'}).string,
        }
    '''
    # 3.使用pyquery解析内容
    # 初始化，返回pyquery对象
    doc = pq(content)
    # 解析网页中所需要的<tr class="item">...</tr>中的内容
    items = doc("tr.item")
    # print(len(items))
    # 遍历并解析每本图书的具体信息
    for item in items.items():  # 要将item转换为可迭代的遍历器
        yield {
            'title': item.find("div.pl2 a").text().strip().replace('\n', '').replace(' ', ''),
            'image': item.find("a.nbg img").attr('src'),
            'author': item.find("p.pl").text(),
            'score': item.find("span.rating_nums").text(),
        }


def writeFile(content):
    """保存爬取内容"""
    with open("./result.txt", 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(offset):
    """主程序函数，调用"""
    url = 'https://book.douban.com/top250?start=' + str(offset)
    # 传入爬取地址的内容
    html = getPage(url)
    if html:
        # 解析爬取网页的内容
        for item in parsePage(html):  # 执行解析并遍历
            print(item)
            # 执行写入保存爬取内容
            writeFile(item)


# 判断当前是否为主程序，并调用主程序来爬取
if __name__ == '__main__':
    # main(0)
    for i in range(10):
        main(offset=i*25)
        time.sleep(1)
