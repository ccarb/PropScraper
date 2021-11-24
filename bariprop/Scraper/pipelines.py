# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from scrapController import ScrapController as controller
from scrapy.exceptions import DropItem
import logging



class BaripropPipeline:
    def __init__(self) -> None:
        self.items=[]
        try:
            with open("items.jl","x"):
                print("create file")
        except:
            print("File exists")
        
        with open("items.jl",'r') as f:
            for line in f:
                if line != '':
                    self.items.append(json.loads(line))

    def open_spider(self,spider):
        self.file=open('items.jl','a')

    def close_spider(self,spider):
        self.file.close()
        controller.sendNotification()

    def process_item(self, item, spider):
        if ItemAdapter(item).asdict() not in self.items:
            line = json.dumps(ItemAdapter(item).asdict()) + "\n"
            self.file.write(line)
            controller.newItem()
            return item
        else:
            raise DropItem(f"Duplicate item found: {item!r}")
