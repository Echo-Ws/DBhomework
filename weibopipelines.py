# -*- coding:utf-8
"""
处理微博解析后的数据并放入数据库中
"""

# import MySQLdb
import sys
import logging
import pymongo
logger = logging.getLogger('mylogger')
reload(sys)
sys.setdefaultencoding("utf-8")


class MainPageMongoPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host="222.201.139.158", port=27017)
        self.db = client.yulin

    def insert_main_info(self, data):
        """
        插入用户微博主页信息 weibo_main_users
        :param data:
        :return:
        """
        try:
            # collection = self.db['weibo_main_user']
            collection = self.db['weibo_search'] # 爬low部分
            for item in data:
                collection.insert(item)

        except Exception as e:
            logger.info(e.message)
            logger.info("Main Page Pipeline error")

# class MainPageSQLPipeline(object):
#     def __init__(self):
#         # self.db = MySQLdb.connect("110.64.66.196","root","ibm212","weibo",charset='utf8')
#         self.db = MySQLdb.connect("125....","Tiger","123456","weibo",charset='utf8')
#         # self.db = MySQLdb.connect("localhost","Tiger","123456","weibo",charset='utf8')
#         self.cursor = self.db.cursor()
#     def insert_item(self,item):
#         try:
#             sql = "insert into user_profile values( %s,%s,%s,%s,%s,  %s,%s,%s,%s,%s    ,%s,%s,%s,%s,%s  ,%s,%s,%s)"
#             param = item
#             self.cursor.execute(sql,param)
#             self.db.commit()
#
#         except Exception as e:
#             logger.error(e.message)
#
#         # try:
#         #     sql2 = "insert into profile_already VALUES (%s)"
#         #     param2 = item[0]
#         #     print(sql2,param2)
#         #     self.cursor.execute(sql2,param2)
#         #     self.db.commit()
#         # except Exception as e:
#         #     logger.error(e.message)

