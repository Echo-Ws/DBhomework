# !/usr/bin/env python
# -*- coding: utf-8 -*-
# from logconfig import LogConfig
# logger = LogConfig.get_logger()
import os
import logging
logger = logging.getLogger('mylogger')


# import MySQLdb
class Bloom(object):

    # filter ids that have been crawled
    @classmethod
    def getIds(self):
        # f = open(r'../files/w_id_high.csv','r')
        # f = open(r'bloom/id_high_un.csv','r')
        # f = open(r'bloom/id_low_un.csv','r')
        f = open(r'bloom/id_root_30_un.csv','r')
        bloom = []
        # index = 0 # 每个爬虫各负责一端Ip
        # end = 50000
        index = 0 # 10万以内好了吗？
        end = 5000
        num = 0
        # for line in f.readlines():
        #     if(line!="\n"):
        #         num += 1
        #         if num>index and num<=end:
        #             lines = line.split(",")
        #             bloom.append(lines[0])
        for line in f.readlines():
            num += 1
            if num>index and num<=end:
                id = line.strip()
                bloom.append(id)
        ids = bloom
        return ids

    # 获取已经爬过的Ids
    # def get_already_ids(self):
    def getdb(self):
        # db = MySQLdb.connect('166.111.134.51','root','fit4-305','weibo',charset = 'utf8')
        db = MySQLdb.connect("localhost","Tiger","123456","weibo",charset='utf8')
        return db

    def getIdsDataBase(self):
        #从数据库获取id
        ids = {}
        db = self.getdb()
        cursor = db.cursor()
        sql = "select id from weibo.user_profile"
        cursor.execute(sql)
        data = cursor.fetchall()
        for each in data:
            # print(each)
            # ids.append(each[0])
            ids[each[0]] = ""
        return ids

from pybloom import ScalableBloomFilter
class FileBloom(object):
    def __init__(self):
        self.file_path = "bloom/bloom_weibo.txt";
        self.bloom_filter = ScalableBloomFilter(initial_capacity=10000,error_rate=0.001)

    def read_bloom(self):
        if os.path.exists(self.file_path):
            f = open(self.file_path,"r")
            ids = f.readlines()
            for id in ids:
                id_s = id.strip()
                self.bloom_filter.add(id_s)
            f.close()
        else:
            f = open(self.file_path,"w")
            f.close()

    def to_file(self):
        pass

    def update_bloom_file(self,m_id):
        f =open(self.file_path,"a")
        f.write(str(m_id)+"\n")
        f.close()

    def update_bloom(self,m_id):
        self.bloom_filter.add(m_id)

    def has_id(self,m_id):
        if m_id in self.bloom_filter:
            return True
        else:
            return False


if __name__ == "__main__":
    fb = FileBloom()
    fb.read_bloom()
    fb.update_bloom_file("23920323")
    fb.update_bloom("23920323")
# if __name__ == "__main__":
#     bl = Bloom()
#     ids = bl.getIdsDataBase()
#     f = open(r'id_root_30.csv','r')
#     uids = []
#     for line in f.readlines():
#         id = line.strip()
#         uids.append(id)
#     f.close()
#     print(len(uids))
#     uids = list(set(uids))
#     print(len(uids))
#     f = open(r'id_root_30_un.csv','w')
#     for uid in uids:
#         if uid not in ids:
#             print(uid)
#             f.write(uid+"\n")
#     f.close()

# ids = Bloom.getIds()
# ids = Bloom.getIdsDataBase()
# logger.info(ids)
# print(len(ids))