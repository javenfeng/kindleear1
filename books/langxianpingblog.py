#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return langxianpingblog

class langxianpingblog(BaseFeedBook):
    title                 = u'郎咸平的博客'
    description           = u'曾任香港中文大学财务学讲座教授，公司治理和金融方面的专家。对郎咸平的争议主要在于他的阴谋论。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 20
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = False
    feeds = [
            (u'郎咸平的博客', 'http://ftr.fivefilters.org/makefulltextfeed.php?url=http%3A%2F%2Fblog.sina.com.cn%2Frss%2F1092672395.xml&max=10', True),
           ]