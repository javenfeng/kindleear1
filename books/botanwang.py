#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return botanwang

class botanwang(BaseFeedBook):
    title                 = u'博谈网'
    description           = u'从各种角度评论时事、社会现象、新观点、财经、历史、人物。辅以自由论坛便于读者深层次讨论。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 20
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = True
    feeds = [
            (u'博谈网', 'http://www.botanwang.com/rss.xml', True),
           ]