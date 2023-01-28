# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PlaylistItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    video_count = scrapy.Field()
    playlist_id = scrapy.Field()
    videos = scrapy.Field()


class VideoItem(scrapy.Item):
    # define the fields for your item here like:
    video_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    duration = scrapy.Field()
    keywords = scrapy.Field()
    release_time = scrapy.Field()
    view_count = scrapy.Field()
    like_count = scrapy.Field()
    comment_count = scrapy.Field()


class CommentItem(scrapy.Item):
    user_id = scrapy.Field()
    comment_time = scrapy.Field()
    content = scrapy.Field()
    like_count = scrapy.Field()



