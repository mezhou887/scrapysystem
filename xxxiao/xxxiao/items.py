# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class xxxiaoItem(Item):
    # define the fields for your item here like:
    pagelink = Field()
    title = Field()
    image_urls = Field()
    images = Field()
#     file_urls = Field()
#     files = Field()

