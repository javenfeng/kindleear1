#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return daixublog

class daixublog(BaseFeedBook):
    title                 = u'戴旭的博客'
    description           = u'解放军空军上校，言论犀利，多有争议。自称“仗剑直言，血溅文章，为国请命，甘为鹰犬”。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 20
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'戴旭的博客', 'http://ftr.fivefilters.org/makefulltextfeed.php?url=http%3A%2F%2Fblog.sina.com.cn%2Frss%2F1676393397.xml&max=10', True),
           ]