import os
from scrapy import cmdline
import youtube_comment_scraper_python as comspi
os.chdir(os.path.dirname(os.path.abspath(__file__)))
cmdline.execute('scrapy crawl ytb -o ytb.csv'.split())