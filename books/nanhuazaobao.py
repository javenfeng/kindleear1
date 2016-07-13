#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return nanhuazaobao

class nanhuazaobao(BaseFeedBook):
    title                 = u'南華早報'
    description           = u'其报道具权威性，且独立中肯，在业内享负盛名。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'南華早報', 'http://www.nanzao.com/tc/rss/all/rss.xml', True),
           ]