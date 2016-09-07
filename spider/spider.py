# /usr/bin/python
# -*- coding:utf-8 -*-
import sys
import json
from weibopipelines import MainPageMongoPipeline
import time
import random
from logconfig import LogConfig

reload(sys)
sys.setdefaultencoding("utf-8")
logger = LogConfig.get_logger()


class Spider(object):

    def __init__(self):
        self.json = ""
        self.data = []
        self.login = ""
        self.count = 0

    # 获得respond文件
    def get_respond(self, search_url):
        s = self.login
        logger.info("main_url: " + search_url)
        r = s.get(search_url, headers=s.headers)
        self.json = r.text
        print self.json

    # 判断数据时候为空
    def is_empty(self):
        pass

    # 不同spider处理不同,利用多态实现
    def process_main(self, page):
        pass

    # 将数据写入缓存,缓存达到一定量时写入数据库
    def insert(self, datum):
        self.data.append(datum)
        if len(self.data) == 10:
            self.flush()
            logger.info("-----成功插入10条数据---")
            self.data = []

    # 写入数据库
    def flush(self):
        try:
            doc = self.data
            mp = MainPageMongoPipeline()
            mp.insert_main_info(doc, self.count)
            self.count += len(self.data)
        except Exception as e:
            logger.error(e.message)

    def make_url(self, base_url, page):
        return base_url+str(page)

    def run(self, urls, s_login):
        num = 0
        self.login = s_login
        for base_url in urls:
            num += 1
            if num % 100 == 0:
                time.sleep(120)

            for i in range(100):
                page = i+1
                search_url = self.make_url(base_url, page)
                self.get_respond(search_url)

                try:
                    # 当页数超过可提供数时 cards：[]，利用此跳出
                    if self.is_empty():
                        print "页数没了!!!!!\n"
                        break

                    self.process_main(page)
                    logger.info("-----uid: %s main page has finished---" % str(i))
                    time.sleep(random.uniform(1, 3))
                except Exception as e:
                    logger.error(e.message)

        # 结束前刷一次缓存
        self.flush()
        print "RCSpider运行结束"
