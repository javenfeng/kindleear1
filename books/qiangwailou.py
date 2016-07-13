#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return qiangwailou

class qiangwailou(BaseFeedBook):
    title                 = u'墙外楼'
    description           = u'提供每天更新的网文精选，订阅人数众多的新闻聚合网站。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'墙外楼', 'http://feeds.feedburner.com/letscorp/aDmw', True),
           ]