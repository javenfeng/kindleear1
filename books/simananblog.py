#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return simananblog

class simananblog(BaseFeedBook):
    title                 = u'司马南的博客'
    description           = u'在20世纪末因反伪科学和揭露伪气功、假神医而闻名；21世纪初，活跃于政治评论领域，引发强烈争议。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'司马南的博客', 'http://blog.sina.com.cn/rss/1263406744.xml', True),
           ]