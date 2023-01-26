# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VideoItem(scrapy.Item):
    # define the fields for your item here like:
    video_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    duration = scrapy.Field()
    keywords = scrapy.Field()
    release_time = scrapy.Field()
    view_count = scrapy.Field()
    likes = scrapy.Field()
    comments = scrapy.Field()

class PlaylistItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    video_counts = scrapy.Field()
    url = scrapy.Field()
