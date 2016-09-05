#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import re
import sys
from weibopipelines import MainPageMongoPipeline
import logging
logger = logging.getLogger('searchlogger')
reload(sys)
sys.setdefaultencoding("utf-8")


# 请求用户主页得到部分信息url一般为 u/uid
class MainRequest(object):
    def __init__(self):
        self.json = ""
        self.data = []
        pass

    def request_main(self, search_url, s):
        """
        构建请求主页url
        :param u_id:
        :param s:w
        :return:
        """
        logger.info("main_url: "+search_url)
        r = s.get(search_url, headers = s.headers)
        data_json = json.loads(r.text)
        self.json = data_json
        return data_json["cards"]

    def insert_more(self):

        try:
            doc = self.data
            mp = MainPageMongoPipeline()
            mp.insert_main_info(doc)
        except Exception as e:
            logger.error(e.message)

    def process_main(self,page):
        """
        fansNum
        mblogNum
        nativePlace
        attNum
        favourites_count
        mbrank
        description
        :param result:
        :return:
        """
        try:
            data_json = self.json
            if page == 1:
                cards = data_json['cards'][-1]['card_group']
            else:
                cards = data_json['cards'][0]['card_group']
        except Exception as e:
            logger.error(e.message)


        # 用户信息以json串形式保存，暂时不作分析，爬取用户主页的信息已经足够了
        for c_group in cards:
            mblog = c_group['mblog']
            user = mblog['user']
            print(user)
            print "\n!!!!!!!!!!!!!\n"
            f = open("bloom/bloom_weibo.txt", "a")
            f.write(str(mblog["id"]))
            f.close()
            self.data.append(mblog)
            if len(self.data) == 10:
                self.insert_more()
                self.data = []
            #  将cgroup放入MongoDB永久保存




if __name__ == "__main__":
    MR = MainRequest()
    MR.request_main()