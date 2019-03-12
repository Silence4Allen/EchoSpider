# _*_encoding:utf-8_*_
__author__ = 'Allen'
__date__ = '2018/12/14 18:30'
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "echo"])
execute(["scrapy", "crawl", "xici_proxy"])
# execute(["scrapy", "crawl", "yaozh"])
