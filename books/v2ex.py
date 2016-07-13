#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return v2ex

class v2ex(BaseFeedBook):
    title                 = u'V2EX'
    description           = u'V2EX = way to explore. V2EX是一个知名技术创意网站，由设计师、程序员及有创意的人参与的社区。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = True
    feeds = [
            (u'V2EX', 'http://www.v2ex.com/index.xml', True),
           ]