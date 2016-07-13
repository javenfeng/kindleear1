#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return heweifangblog

class heweifangblog(BaseFeedBook):
    title                 = u'贺卫方的博客'
    description           = u'山东牟平人，北京大学法学院教授、博士生导师，著名法学家。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'贺卫方的博客', 'http://blog.sina.com.cn/rss/1216766752.xml', True),
           ]