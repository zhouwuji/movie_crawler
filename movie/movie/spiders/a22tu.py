# -*- coding: utf-8 -*-
import scrapy
import json
import requests
import os
from scrapy.conf import settings

class A22tuSpider(scrapy.Spider):
    name = '22tu'
    allowed_domains = ['22tu.com']
    # start_urls = [f"https://22tu.cc/play-{settings['SOAP_ID']}-1-{settings['EPISODE']}/"]

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
        SOAP_ID = self.SOAP_ID if hasattr(self, 'SOAP_ID') else settings['SOAP_ID']
        EPISODE = self.EPISODE if hasattr(self, 'EPISODE') else settings['EPISODE']
        SOAP_NAME = self.SOAP_NAME if hasattr(self, 'SOAP_NAME') else settings['SOAP_NAME']
        self.SOAP_DIR = f"F:/{SOAP_NAME}"
        self.url = f"https://22tu.cc/play-{SOAP_ID}-1-{EPISODE}/"

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, dont_filter=False)

    def parse(self, response, ts_bit=None):
        if 'https://22tu' in response.request.url:
            print(f"response.request.url: {response.request.url}")
            url = json.loads(response.css('#play script::text').extract()[0].replace('\\', '').split('=')[1])['url']
            print(f"url: {url}")
            r = requests.get(url)
            if ('iqiyi' in url) or ('bili' in url):
                print(f"资源来自于爱奇艺或哔哩哔哩")
                all_ts_base = '/'.join(url.split('/')[:-1])
                all_ts_url = all_ts_base + '/' + r.text.strip().split('\n')[-1]
                all_ts_base = '/'.join(all_ts_url.split('/')[:-1])
            elif 'sohu' in url:
                print(f"资源来自于搜狐")
                all_ts_base = '/'.join(url.split('/')[:3])
                all_ts_url = all_ts_base + r.text.strip().split('\n')[-1]
            else:
                print(f'无法识别视频来源：{url}')
                return
            print(f'all_ts_url: {all_ts_url}')
            print(f'all_ts_base: {all_ts_base}')
            r = requests.get(all_ts_url)
            ts_urls = r.text.split('\n')
            ts_urls = [all_ts_base + '/' + i for i in ts_urls if '.ts' in i]
            print(f'已经拿到ts信息，总共有{len(ts_urls)}条\n其中三条为：\n{ts_urls[:3]}')
            for i in ts_urls:
                yield scrapy.Request(url=i, callback=lambda x, ts_bit=len(str(len(ts_urls))):self.parse(x, ts_bit), dont_filter=True)
        elif '.ts' in response.request.url:
            if not os.path.exists(f"{self.SOAP_DIR}/{self.EPISODE}"):
                os.makedirs(f"{self.SOAP_DIR}/{self.EPISODE}")
                print(f"创建 {self.SOAP_DIR}/{self.EPISODE} 成功！")
            with open(f"{self.SOAP_DIR}/{self.EPISODE}/{response.request.url.split('/')[-1][-(ts_bit+3):]}", 'wb') as f:
                f.write(response.body)
