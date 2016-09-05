# /usr/bin/python
# -*- coding:utf-8 -*-
import sys
from spider import Spider
from logconfig import LogConfig
import json

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

    def process_main(self, page):
        data_json = self.json
        try:
            cards = data_json['card_group']
        except Exception as e:
            logger.error(e.message)

        for comment in cards:
            print comment['text']
            print "\n!!!!!!!!!!!!!\n"
            self.insert(comment)

