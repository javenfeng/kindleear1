#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return programthink

class programthink(BaseFeedBook):
    title                 = u'编程随想的博客'
    description           = u'提升思维能力，普及政治常识，网络安全知识，软件开发技术。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'编程随想的博客', 'http://feeds2.feedburner.com/programthink', True),
           ]