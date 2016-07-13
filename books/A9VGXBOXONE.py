#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return A9VGXBOXONE

class A9VGXBOXONE(BaseFeedBook):
    title                 = u'A9VG-XBOX ONE'
    description           = u'A9VG电玩部落，中国电玩领先平台。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    max_articles_per_feed = 30
    mastheadfile          = "mh_javendaily.gif"
    coverfile             = "cv_javendaily.jpg"
    network_timeout       = 120
    fetch_img_via_ssl     = True
    feeds = [
            (u'A9VG-XBOX ONE', 'http://bbs.a9vg.com/forum.php?mod=rss&fid=609&auth=0', True),
           ]