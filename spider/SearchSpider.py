# /usr/bin/python
# -*- coding:utf-8 -*-
import sys
from spider import Spider
from logconfig import LogConfig
import json
logger = LogConfig.get_logger()
reload(sys)
sys.setdefaultencoding("utf-8")


class SearchSpider(Spider):
    def is_empty(self):
        data_json = json.loads(self.json)
        self.json = data_json
        return not self.json["cards"]

    def process_main(self, page):
        try:
            data_json = self.json
            if page == 1:
                cards = data_json['cards'][-1]['card_group']
            else:
                cards = data_json['cards'][0]['card_group']
        except Exception as e:
            logger.error(e.message)

        for c_group in cards:
            mblog = c_group['mblog']
            user = mblog['user']
            print(user)
            print "\n!!!!!!!!!!!!!\n"

            self.insert(mblog)

