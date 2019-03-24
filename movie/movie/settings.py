# -*- coding: utf-8 -*-

# Scrapy settings for movie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movie'

SPIDER_MODULES = ['movie.spiders']
NEWSPIDER_MODULE = 'movie.spiders'

DOWNLOAD_PATH = 'F:\movie'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'movie (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
   "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
   "accept-encoding":"gzip, deflate, br",
   "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
   "cache-control":"max-age=0",
   # "cookie":"api_uid=rBTyKFxsuYOd2kqZDt5lAg==; ua=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F72.0.3626.109%20Safari%2F537.36; webp=1; _nano_fp=XpdyX0ExlpPjX0EonT_wOtXh95aFL_zMdgqihOvw; msec=1800000; rec_list_catgoods=rec_list_catgoods_bhfhlB; single=single_qzvVE0; vgl=vgl_M8E8IS; evaluation=evaluation_9srjkC; mf-rec=mf-rec_SynvYQ; rec_list_index=rec_list_index_zlvKXL; rec_list=rec_list_oMWZrr; goods_detail_mall=goods_detail_mall_5WSwmB; pdd_user_id=2255380472147; PDDAccessToken=U2HAYC5KT3WZQNEKSPMGWUHHDHKXOEZ7ZLRZ3U2IOM4CQAUMJAYA101539e; rec_list_personal=rec_list_personal_YUpnqN; JSESSIONID=251D77DD4836189AA18DFB9B16D7DEC4; ab=0; sp=0; gp=0; egrp=6",
   "upgrade-insecure-requests":"1",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'movie.middlewares.MovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'movie.middlewares.RandomUserAgent': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'movie.pipelines.MoviePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

LOG_LEVEL= 'INFO'

# 保存ts文件的地址
ts_dir = r'F:\ts_liulangdiqiu'

# 二级目录
SOAP_NAME = 'doutinghao'  # 电视剧剧名
SOAP_DIR = f"F:/{SOAP_NAME}"  # 电视剧文件夹
SOAP_ID = 28230 # 暂时通过手工查询获取
EPISODE = 12 # 剧集