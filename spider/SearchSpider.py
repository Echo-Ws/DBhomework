# /usr/bin/python
# -*- coding:utf-8 -*-
import sys
from weibo_login import WeiboLogin
from request_main import MainRequest
import requests
import time
import random
from logconfig import LogConfig
logger = LogConfig.get_logger()
reload(sys)
sys.setdefaultencoding( "utf-8" )





class SearchSpider(object):

    def run(self, urls, s_login):
        num = 0
        for base_url in urls:
            num += 1
            if num % 100 == 0:
                time.sleep(500)

                # main page
            r_m = MainRequest()
            for i in range(100):
                page = i+1
                search_url = base_url+str(page)
                # 当页数超过可提供数时 cards：[]，利用此跳出
                try:
                    if not r_m.request_main(search_url, s_login):
                        print "页数没了!!!!!\n"
                        break

                    r_m.process_main(page)
                    logger.info("-----uid: %s main page has finished---" % str(i))
                    time.sleep(random.uniform(2, 4))
                except Exception as e:
                    logger.error(e.message)

            r_m.insert_more()
        print "SearchSpider运行结束"