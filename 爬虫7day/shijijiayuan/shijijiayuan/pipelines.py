# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import scrapy.http
import requests
from shijijiayuan import settings
import os
import json
from datetime import datetime


class ShijijiayuanPipeline(object):
    def process_item(self, item, spider):
        # return item
        content = json.dumps(dict(item),ensure_ascii=False) + "\n"
        with open("jiayuan.json",'a') as f:
            f.write(content.encode('utf-8'))
        uid = item['userid']
        images_ulrs = item["images_urls"]
        dir_path = '%s/%s'%(settings.IMAGES_STORE,spider.name)

        for url in images_ulrs:
            image_name= url.split('/')[-1:][0]
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            file_path = '%s/%s'%(dir_path,uid)
            if not os.path.exists(file_path):
                os.makedirs(file_path)
                item["imagepath"] = file_path
            with open(file_path + "/" + image_name,'wb') as f:
                response = requests.get(url,stream=True)
                for block in response.iter_content(1024):
                    if not block:
                        break
                    f.write(block)

        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        return item
