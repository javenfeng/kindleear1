#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return dwnews

class dwnews(BaseFeedBook):
    title                 = u'多维新闻'
    description           = u'對中國負面事件報道的言辭比較溫和中立，有亲共倾向，不正面與新華社報道口徑發生對立。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 20
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'多维新闻', 'http://ftr.fivefilters.org/makefulltextfeed.php?url=http%3A%2F%2Fcreatefeed.fivefilters.org%2Fextract.php%3Furl%3Dm.dwnews.com%252F%26in_id_or_class%3D%26url_contains%3D&max=10', True),
           ]