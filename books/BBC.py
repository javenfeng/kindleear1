#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return BBC

class BBC(BaseFeedBook):
    title                 = u'BBC中文网'
    description           = u'英国广播公司，在相当长的一段时间内，BBC一直垄断着英国的电视、电台。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'BBC', 'http://www.bbc.co.uk/zhongwen/simp/index.xml', True),
           ]