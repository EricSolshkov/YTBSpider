# Scrapy settings for YTBSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'YTBSpider'

SPIDER_MODULES = ['YTBSpider.spiders']
NEWSPIDER_MODULE = 'YTBSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'YTBSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
'''= {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
}
header_list '''
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Accept": "*/*",
    "Accept-Language": "en-US",
    #"Accept-Encoding": "deflate, br",

    "Content-Type": "application/json",
    "Cookie": "PREF=f4=4000000&tz=Asia.Shanghai&f6=40000000&f5=20000&f7=100; SID=SQjPahu_oOcSWn0DFMw_xGCpPGlg5Q_bF6aIkXy0d-Tlwvh8Ez5XCc7K9ggX0FGHhk7Kmw.; __Secure-1PSID=SQjPahu_oOcSWn0DFMw_xGCpPGlg5Q_bF6aIkXy0d-Tlwvh8270qbIL9xfjcEGWBL4yVEw.; __Secure-3PSID=SQjPahu_oOcSWn0DFMw_xGCpPGlg5Q_bF6aIkXy0d-Tlwvh8XQVlSgDXoz5taJiqCJu9jA.; HSID=AlkLlgoUbB1S0Gub2; SSID=AcbEMuPGlh_KzaMzR; APISID=mze1Q3-Aj_rRDOHS/A8ubcw3WHzPpC-XDW; SAPISID=DXB0hsSweHL6k9tT/ACfz_wbM0nc6NnzSA; __Secure-1PAPISID=DXB0hsSweHL6k9tT/ACfz_wbM0nc6NnzSA; __Secure-3PAPISID=DXB0hsSweHL6k9tT/ACfz_wbM0nc6NnzSA; LOGIN_INFO=AFmmF2swRQIgeJ0C-5fbspu-EY3j9q_z0GFdNoR1Ad5UBqJ3OC4_7M8CIQCDdeOVrVs8D2SCCzLgp59x_FzGPUKxjBa6oXUFaG57Tg:QUQ3MjNmeENhZ2lvTks0aEtvdThUS0NDV1RWMTU2aGFkQ1p3NTJBSndEQTJjZnJib3FMUWtnUzVrTVpJZGNMQmc1MGlKUjVjTjdQVXpvVXYzTGVMQXE4QTQxWXhTQnlDWDFCaGtmX2Z3MmoyUFlYZWZOVWlzVHVielJycWI2SXdhWUJHZWQxNnZkQ3VKUi1vVU1ocG05M2IwenVUaWdKd01B; SIDCC=AIKkIs0nSkHU38iUH0Qt9BbJrfc3hCFc2c2hOvLfAgIwHaUuX-9x8EujC8Mja6aLAj5n4Ditqy4; __Secure-3PSIDCC=AIKkIs0c38ItLgJyrtsgeFAk1rjkwDZ1qOG_TUkgoYYqF9LIMbutvAkFBjL4yPQejP_etTO2FA; __Secure-1PSIDCC=AIKkIs05CzGGLykIy4X7mVpcOXaOBEUFsywxT8AVKysAYf5A_yF7XDsp5yGCmqgDuejaeK-KvjA; VISITOR_INFO1_LIVE=uOIil88ZgjQ; DEVICE_INFO=ChxOekU0T1RReE9EWTJNRGszTkRNM09UazJNZz09EK7kl54GGK7kl54G; YSC=qnYlCnMQwb8"
}
header_video = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
   "Accept-Language": "en-US",
   #"Accept-Encoding": "deflate, br",
   "Connection": "keep-alive",
   "Cookie": "PREF=f4=4000000&tz=Asia.Shanghai&f6=40000000&f5=20000&f7=100; SID=SQjPahu_oOcSWn0DFMw_xGCpPGlg5Q_bF6aIkXy0d-Tlwvh8Ez5XCc7K9ggX0FGHhk7Kmw.; __Secure-1PSID=SQjPahu_oOcSWn0DFMw_xGCpPGlg5Q_bF6aIkXy0d-Tlwvh8270qbIL9xfjcEGWBL4yVEw.; __Secure-3PSID=SQjPahu_oOcSWn0DFMw_xGCpPGlg5Q_bF6aIkXy0d-Tlwvh8XQVlSgDXoz5taJiqCJu9jA.; HSID=AlkLlgoUbB1S0Gub2; SSID=AcbEMuPGlh_KzaMzR; APISID=mze1Q3-Aj_rRDOHS/A8ubcw3WHzPpC-XDW; SAPISID=DXB0hsSweHL6k9tT/ACfz_wbM0nc6NnzSA; __Secure-1PAPISID=DXB0hsSweHL6k9tT/ACfz_wbM0nc6NnzSA; __Secure-3PAPISID=DXB0hsSweHL6k9tT/ACfz_wbM0nc6NnzSA; LOGIN_INFO=AFmmF2swRQIgeJ0C-5fbspu-EY3j9q_z0GFdNoR1Ad5UBqJ3OC4_7M8CIQCDdeOVrVs8D2SCCzLgp59x_FzGPUKxjBa6oXUFaG57Tg:QUQ3MjNmeENhZ2lvTks0aEtvdThUS0NDV1RWMTU2aGFkQ1p3NTJBSndEQTJjZnJib3FMUWtnUzVrTVpJZGNMQmc1MGlKUjVjTjdQVXpvVXYzTGVMQXE4QTQxWXhTQnlDWDFCaGtmX2Z3MmoyUFlYZWZOVWlzVHVielJycWI2SXdhWUJHZWQxNnZkQ3VKUi1vVU1ocG05M2IwenVUaWdKd01B; SIDCC=AIKkIs23EgnL82rzHukyvQlFU8nIEFNu0iLt5q6R4LRIrnF-Uzwqk82kJt31ZW1-3PDs-dsP_Bk; __Secure-3PSIDCC=AIKkIs2h0-OxnJdbWhnI4HWoivxwbm89GUVhm6HY3jRnkPy5d268Gkbs_k3AQvcERs6E3hM2SQ; __Secure-1PSIDCC=AIKkIs1BPdMT4Ef7EpRuwdWBa7IK6WtrvZ0m185lkl0yuiLTbo2HZzuqPj76HpGvyoUVyaWInOM; VISITOR_INFO1_LIVE=uOIil88ZgjQ; DEVICE_INFO=ChxOekU0T1RReE9EWTJNRGszTkRNM09UazJNZz09EK7kl54GGK7kl54G; YSC=qnYlCnMQwb8"
   }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'YTBSpider.middlewares.YtbspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'YTBSpider.middlewares.YtbspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'YTBSpider.pipelines.YTBSpiderPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
