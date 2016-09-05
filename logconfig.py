# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler


class LogConfig(object):
    @staticmethod
    def get_logger():
        logger = logging.getLogger('searchlogger')
        logger.setLevel(logging.INFO)
        Rthandler = RotatingFileHandler('log/mylog.log', maxBytes=1024*1024*10,backupCount=25)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        Rthandler.setFormatter(formatter)
        logger.addHandler(Rthandler)
        # 输出到控制台
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)
        logger.addHandler(console)
        return logger
