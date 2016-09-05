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
        return self.json[0]["mod_type"] == "mod/empty"

    def process_main(self, page):
        data_json = self.json
        try:
            cards = data_json[-1]['card_group']
        except Exception as e:
            logger.error(e.message)

        for comment in cards:
            print comment['text']
            print "\n!!!!!!!!!!!!!\n"
            self.insert(comment)

