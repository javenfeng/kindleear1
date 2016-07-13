#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return caijing

class caijing(BaseFeedBook):
    title                 = u'財經網'
    description           = u'秉承《财经》杂志理念，严守新闻专业主义精神，坚持客观、中道、理性、建设性前提下批评性立场。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'財經網', 'http://www.caijing.com.cn/rss/rss.xml', True),
           ]