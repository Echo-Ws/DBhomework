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

    # 获得需要的json文件
    def getJson(self, search_url):
        s = self.login
        logger.info("main_url: " + search_url)
        r = s.get(search_url, headers=s.headers)
        data_json = json.loads(r.text)
        self.json = data_json
        return data_json["cards"]

    # 不同spider处理不同,利用多态实现
    def process_main(self, page):
        pass

    # 将数据写入缓存,缓存达到一定量时写入数据库
    def insert(self, mblog):
        self.data.append(mblog)
        if len(self.data) == 10:
            self.flush()
            self.data = []

    # 写入数据库
    def flush(self):
        try:
            doc = self.data
            mp = MainPageMongoPipeline()
            mp.insert_main_info(doc)
        except Exception as e:
            logger.error(e.message)

    def run(self, urls, s_login):
        num = 0
        self.login = s_login
        for base_url in urls:
            num += 1
            if num % 100 == 0:
                time.sleep(120)

            for i in range(100):
                page = i+1
                search_url = base_url+str(page)
                # 当页数超过可提供数时 cards：[]，利用此跳出
                try:
                    if not self.getJson(search_url):
                        print "页数没了!!!!!\n"
                        break

                    self.process_main(page)
                    logger.info("-----uid: %s main page has finished---" % str(i))
                    time.sleep(random.uniform(2, 4))
                except Exception as e:
                    logger.error(e.message)

            self.flush()
        print "SearchSpider运行结束"
