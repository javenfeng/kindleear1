#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return chinadigitaltimes

class chinadigitaltimes(BaseFeedBook):
    title                 = u'中国数字时代'
    description           = u'加州大学柏克莱分校研究项目，是结合网络2.0最新技术和网民群体智慧的新闻聚合网站。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'中国数字时代', 'http://chinadigitaltimes.net/chinese/feed', True),
           ]