# -*- coding: utf-8 -*-
# @Author  : Silas9187
# @Email   : silas9187@gmail.com
# @blogsite  :https://blog.csdn.net/acarsar
# @GitHub    :https://github.com/silas9187
"""百度街拍爬取"""
import os, time
import requests
from urllib.parse import urlencode
from urllib.request import urlretrieve
from urllib import error
'''加密关键字用urllib.parse.quote(word)'''

def getPage(offset):
    '''爬取信息'''
    # 定义参数
    params = {
        'pn': offset,
        'rn': 30,
        'gsm': str(hex(offset))
    }
    # 初始化url地址
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
    }
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%97%E6%8B%8D&cl=&lm=&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E8%A1%97%E6%8B%8D&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&selected_tags='+ urlencode(params)
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            # 请求返回的数据格式是json格式。
            return res.json()
    except:
        return None



def decry(url):
    '''破解图片链接'''
    str_table = {
        '_z2C$q': ':',
        '_z&e3B': '.',
        'AzdH3F': '/',
    }
    in_table = u'0123456789abcdefghijklmnopqrstuvw'
    out_table = u'7dgjmoru140852vsnkheb963wtqplifca'
    # 将in和out中每个字符转化为各自的ascii码，返回一个字典（dict）
    char_table = str.maketrans(in_table, out_table)

    # print(char_table)
    # for t in a:
    # 解码
    if True:
        for key, value in str_table.items():
            url = url.replace(key, value)
            # print(a)
        url = url.translate(char_table)
        # print(a, end='')
    return url
def getImage(json):
    '''获取图片信息'''
    # print(type(json))  # json 为字典（dict）格式
    data = json.get('data')
    m = 1
    if data:
        for item in data:
            try:
                if item.get("objURL"):
                    image = decry(item.get("objURL"))
                    title = str(m)
                    yield {
                            'image': image,
                            'title': title,
                        }
                    m += 1
            except error.URLError as e:
                print(e.reason)  # 输出错误信息
"""def getImage(json):# 获取thumbURL
    '''获取图片信息'''
    # print(type(json))  # json 为字典（dict）格式
    data = json.get('data')
    m = 1
    if data:
        for item in data:
            image = item.get("thumbURL")
            title = str(m)
            yield {
                    'image': image,
                    'title': title,
                }
            m += 1
"""
def saveImage(item):
    '''储存图片信息'''
    #处理图片的存储路径
    path = os.path.join("./mypic/", item.get('title'))
    if not os.path.exists(path):
        os.makedirs(path)

    #图片路径的处理
    local_image_url = item.get("image")
    # 判断是否有objURL
    if local_image_url:
        save_pic = path+"/"+local_image_url.split("/").pop(2)+".jpg"

    #存储图片
        urlretrieve(local_image_url, save_pic)


def main(offset):
    '''主函数'''
    json = getPage(offset)
    # print(content)
    for item in getImage(json):
        print(item)
        saveImage(item)


if __name__ == "__main__":
    for i in range(1, 3):
        main(offset=i*30)
        # time.sleep(1)
