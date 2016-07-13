#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Nytimes

class Nytimes(BaseFeedBook):
    title                 = u'纽约时报'
    description           = u'在美国纽约出版的日报，在全世界发行，有相当的影响力。它是美国严肃报刊的代表。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'纽约时报', 'http://cn.nytimes.com/rss.html', True),
           ]
		   