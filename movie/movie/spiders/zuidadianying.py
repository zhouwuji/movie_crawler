# -*- coding: utf-8 -*-
import os

import scrapy
from movie.items import MovieItem
from scrapy.conf import settings

class ZuidadianyingSpider(scrapy.Spider):
    name = 'zuidadianying'
    allowed_domains = ['https://cn2.zuidadianying.com']
    start_urls = ['https://cn2.zuidadianying.com/']

    def start_requests(self):
        files_id = self.get_fileName()
        movie_id = [i for i in range(0, 1807) if i not in files_id]
        movie_id = [str(i) for i in movie_id]
        movie_id = ['0'+i if len(i)==2 else i for i in movie_id]
        movie_id = ['00' + i if len(i) == 1 else i for i in movie_id]
        urls = [(f'https://cn2.zuidadianying.com/20190207/Nj4iG5WQ/800kb/hls/v9XGd6044{i}.ts', i) for i in movie_id]
        print(f"总共有{len(urls)}个文件要爬取")
        for url,i in urls:
            yield scrapy.Request(url, callback=lambda response, i=i:self.parse(response, i), dont_filter=True)

    def parse(self, response, i):
        item = MovieItem()
        item['content'] = response.body
        item['file_name'] = i
        yield item

    def get_fileName(self):
        path = settings['DOWNLOAD_PATH']
        files = []
        for dirpath, dirnames, filenames in os.walk(path, topdown=False):
            files = [i for i in filenames if 'ts' in i]
        if files:
            print(f'已下载了{len(files)}个文件\n其中一个文件为：{files[0]}')
        return [int(i.split('.')[0]) for i in files]