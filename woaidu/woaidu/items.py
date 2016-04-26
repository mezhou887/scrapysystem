# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class woaiduItem(Item):
    # define the fields for your item here like:
    book_name = Field()
    author = Field()
    book_description = Field()
    book_covor_image_url = Field()
    original_url = Field()