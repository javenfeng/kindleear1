#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return wyzxwk

class wyzxwk(BaseFeedBook):
    title                 = u'乌有之乡'
    description           = u'中国著名左派网站，提供强大正能量。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'乌有之乡', 'http://www.wyzxwk.com/e/web/?type=rss2&classid=0', True),
           ]