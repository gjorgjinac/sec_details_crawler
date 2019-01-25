# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlerPipeline(object):
    count=0
    def process_item(self, item, spider):
        print ("PRINTING FROM PIPELINE")
        print("ITEM NUMBER {0}: ".format(self.count))
        self.count+=1
        print (item['title'])
        print (item['subtitle'])
        print (item['content'])
        return item
