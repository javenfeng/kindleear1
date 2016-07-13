#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return dwworld

class dwworld(BaseFeedBook):
    title                 = u'德国之声'
    description           = u'中文频道通过文字、音频、视频相结合的多媒体方式提供以中国、欧洲为主同时包括世界的政经资讯。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'德国之声', 'http://rss.dw.de/rdf/rss-chi-all', True),
           ]