#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Solidot

class Solidot(BaseFeedBook):
    title                 = u'Solidot'
    description           = u'CNET中国旗下的一个中国的科技资讯网站和奇客交流社区，其口号是“奇客的资讯，重要的东西”。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = True
    feeds = [
            (u'Solidot', 'http://feeds2.feedburner.com/solidot', True),
           ]