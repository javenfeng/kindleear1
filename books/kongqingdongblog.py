#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return kongqingdongblog

class kongqingdongblog(BaseFeedBook):
    title                 = u'孔庆东的博客'
    description           = u'北京大学中文系教授，常发争议性言论，如极端仇视“西方资本主义自由化”思想而被受到网民注意。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 20
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'孔庆东的博客', 'http://ftr.fivefilters.org/makefulltextfeed.php?url=http%3A%2F%2Fblog.sina.com.cn%2Frss%2F1198367585.xml&max=10', True),
           ]