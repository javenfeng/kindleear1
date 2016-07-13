#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return lichangxinwen

class lichangxinwen(BaseFeedBook):
    title                 = u'立場新聞'
    description           = u'非牟利新聞網站，立足香港主場，致力守護民主、人權、自由、法治與公義等香港核心價值。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'立場新聞', 'https://www.thestandnews.com/rss/', True),
           ]