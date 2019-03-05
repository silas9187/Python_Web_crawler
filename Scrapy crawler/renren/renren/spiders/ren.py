# -*- coding: utf-8 -*-
import scrapy
import time,random


class RenSpider(scrapy.Spider):
    name = 'ren'
    allowed_domains = ['renren.com']
    # start_urls = ['http://www.renren.com/']

    def start_requests(self):
        base_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp='
        # 构造uniqueTimestamp
        localtime = time.localtime()
        today = int(time.strftime("%w"))
        millisec = random.randint(0, 999)
        uniqueTimestamp = str(localtime[0]) + str(localtime[1] - 1) + str(today) + str(localtime[3]) + str(localtime[4]) + str(millisec)

        '''
        headers = {
            'Accept': '* / *',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9, en;q = 0.8',
            'Connection': 'keep - alive',
            'Content - Length': '279',
            'Content - Type': 'application / x - www - form - urlencoded',
            'Cookie': 'anonymid=jpttpf7zyzpo94; depovince=GW; _r01_=1; JSESSIONID=abc3WL6cqsEH86cKtPbFw; ick_login=04e4188d-d6e1-4521-9af0-3c92fe9f540a; ick=8e238493-465f-4563-8131-44fc1f7bb1bd; __utma=151146938.871791549.1545142527.1545142527.1545142527.1; __utmc=151146938; __utmz=151146938.1545142527.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; first_login_flag=1; ln_uact=15025415548; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=b12398f8-1b19-453b-9edc-2cbb3129152d%7C990412152d9d6af30d6009a2e04098e9%7C1545142605342%7C1%7C1545142606672; wp_fold=0; vip=1; wp=0; loginfrom=null; jebecookies=9a3dc8b8-b37b-4ee2-9eeb-7b38d2e3bddb|||||',
            'Host': 'www.renren.com',
            'Origin': 'http: // www.renren.com',
            'Referer': 'http: // www.renren.com / SysHome.do',
            'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.110Safari / 537.36',
            'X - Requested - With': 'XMLHttpRequest',
        }
        '''
        url = base_url + uniqueTimestamp
        data = {'email': '15025415548',
                'icode': '',
                'origURL': 'http://www.renren.com/home',
                'domain': 'renren.com',
                'key_id': '1',
                'captcha_type': 'web_login',
                'password': 'ab2a9c64256d9e104f083b4ff0d9fe4593c68db9f7ac02ad898f18ceb3e319f6',
                'rkey': '47fd626fc836a5aac66995a8cd960384',
                'f': 'http%3A%2F%2Fwww.renren.com%2F514538180}',
                'Cookie': 'anonymid=jpttpf7zyzpo94; depovince=GW; _r01_=1; JSESSIONID=abc3WL6cqsEH86cKtPbFw; ick_login=04e4188d-d6e1-4521-9af0-3c92fe9f540a; ick=8e238493-465f-4563-8131-44fc1f7bb1bd; __utma=151146938.871791549.1545142527.1545142527.1545142527.1; __utmc=151146938; __utmz=151146938.1545142527.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; first_login_flag=1; ln_uact=15025415548; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=b12398f8-1b19-453b-9edc-2cbb3129152d%7C990412152d9d6af30d6009a2e04098e9%7C1545142605342%7C1%7C1545142606672; wp_fold=0; vip=1; wp=0; loginfrom=null; jebecookies=9a3dc8b8-b37b-4ee2-9eeb-7b38d2e3bddb|||||',
                }

        yield scrapy.FormRequest(
            url=url,
            formdata=data,
            # headers=headers,
            callback=self.parse,
            )

    def parse(self, response):
        # print(response.xpath("//head").re("<title>(.*?)</title>"))
        print(response.body)
        # print(response.selector.xpath('/html/head/title/text()').extract_first())


