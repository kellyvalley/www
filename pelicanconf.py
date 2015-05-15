#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

DEFAULT_LANG = u'zh'
AUTHOR = u'valleyrain'
SITENAME = {'en': 'Valley Rain Reading Club', 'zh':'谷雨书苑'}[DEFAULT_LANG]
SITEURL = 'http://www.valleyrain.org'

TIMEZONE = 'America/Los_Angeles'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  None

# Social widget
SOCIAL = (('FB Group(ValleyRain)', 'http://www.facebook.com/groups/ValleyRain'),
          ('微信群(谷雨書苑)', 'http://weixin.qq.com/g/AduHOh9yLie7It1V'),
          ('微信联系人(Raymond)', 'http://weixin.qq.com/r/NIjVzcvEBZZ6rY_u990m'),
          ('微信联系人(Tao)', 'http://weixin.qq.com/r/SH-27I3EjgDxrRmN9ypa'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MD_EXTENSIONS = (['toc'])

LOCALE = ('zh_CN.utf8', 'en_US.utf8')
DATE_FORMATS = {
	'en': ('en_US.utf8', '%x'),
	'zh': ('zh_CN.utf8', '%x'),
}

# Use bootstrap3 theme
THEME = 'themes/pelican-bootstrap3'
FAVICON = 'images/favicon.ico'
BOOTSTRAP_THEME = 'cosmo'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
