# /usr/bin/python
# -*- coding:utf-8 -*-
import sys
from spider import Spider
from logconfig import LogConfig
import json
import re

logger = LogConfig.get_logger()
reload(sys)
sys.setdefaultencoding("utf-8")


class RCSpider(Spider):

    def is_empty(self):
        try:
            self.json = json.loads(self.json)[-1]
            return self.json["mod_type"] == "mod/empty"
        except Exception as e:
            logger.error(e.message)
            return 1

    def get_respond(self, search_url):
        s = self.login
        logger.info("main_url: " + search_url)
        r = s.get(search_url, headers=s.headers)
        self.json = r.text
        self.omid = re.findall('.*?id=(\d+)&.*', search_url)[0]
        print self.json

    def process_main(self, page):
        data_json = self.json
        try:
            cards = data_json['card_group']
        except Exception as e:
            logger.error(e.message)

        for comment in cards:
            print comment['text']
            comment['omid'] = self.omid
            print comment['omid']
            self.insert(comment)

