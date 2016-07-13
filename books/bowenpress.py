#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return bowenpress

class bowenpress(BaseFeedBook):
    title                 = u'博聞社'
    description           = u'新興新聞社，給全球華文讀者提供高質量、全面、及時、可靠的全方位新聞服務。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'博聞社', 'http://bowenpress.com/feed', True),
           ]