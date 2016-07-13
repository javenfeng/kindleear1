#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return yueguangblog

class yueguangblog(BaseFeedBook):
    title                 = u'月光博客'
    description           = u'是一个专注于互联网、社会化网络、IT技术、谷歌地图、软件应用等领域的原创IT科技著名博客。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'月光博客', 'http://feed.williamlong.info', True),
           ]