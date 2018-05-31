#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Meituan api spider's main runtime program file. In this file, we instantialize
an instance of MT_spider.
'''

from spider_develop import MeituanSpider


# save_mode ：txt存储为txt文件，csv存储为csv文件，db存储在mysql数据库中，无输入默认为txt

# spider = MeituanSpider(save_mode='txt')
spider = MeituanSpider(save_mode='csv')
# spider = MeituanSpider(save_mode='db')

spider.run()
