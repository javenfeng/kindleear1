#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return faguang

class faguang(BaseFeedBook):
    title                 = u'法廣'
    description           = u'法国国际广播电台（RFI）用法语和其他十二个语种向全世界广播。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'法廣', 'http://cn.rfi.fr/general/rss', True),
           ]