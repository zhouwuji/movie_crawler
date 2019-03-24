# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings

class MoviePipeline(object):
    def process_item(self, item, spider):
        with open(f"{settings['DOWNLOAD_PATH']}/{item['file_name']}.ts", 'wb') as f:
            f.write(item['content'])
            print(f"{item['file_name']} has been downloaded!")
        return item
