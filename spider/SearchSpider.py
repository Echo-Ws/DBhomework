# /usr/bin/python
# -*- coding:utf-8 -*-
import sys
from spider import Spider
from logconfig import LogConfig
logger = LogConfig.get_logger()
reload(sys)
sys.setdefaultencoding( "utf-8" )


class SearchSpider(Spider):
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
            f = open("bloom/bloom_weibo.txt", "a")
            f.write(str(mblog["id"]))
            f.close()
            self.insert(mblog)

