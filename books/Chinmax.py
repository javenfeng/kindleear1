#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Chinmax

class Chinmax(BaseFeedBook):
    title                 = u'凤舞血凰的博客'
    description           = u'爱国主义：一堆随时可以被任何野心家所点燃，去照亮他的名字的易燃垃圾。 ——安卜罗斯·皮尔斯'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = True
    feeds = [
            (u'凤舞血凰的博客', 'http://ftr.fivefilters.org/makefulltextfeed.php?url=https%3A%2F%2Fchinmax.info%2F%3Ffeed%3Drss2&max=10', True),
           ]