# /usr/bin/python
# -*- coding:utf-8 -*-
import sys
from weibo_login import WeiboLogin
from request_main import MainRequest
import requests
import time
import random
from logconfig import LogConfig
logger = LogConfig.get_logger()
reload(sys)
sys.setdefaultencoding( "utf-8" )


# 登录，保存Session
s_login = requests.session()
w = WeiboLogin()
# s_login = w.login()
s_login = w.login_un()
logger.info("login has finished")
time.sleep(1.5)


Search_urls = [
    # 搜索关键词语：傅园慧 可以运行
    "http://m.weibo.cn/page/pageJson?containerid=&containerid=100103type%3D1%26q%3D%E5%82%85%E5%9B%AD%E6%85%A7&type=all&queryVal=%E5%82%85%E5%9B%AD%E6%85%A7&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%82%85%E5%9B%AD%E6%85%A7&title=%E5%82%85%E5%9B%AD%E6%85%A7&v_p=11&ext=&fid=100103type%3D1%26q%3D%E5%82%85%E5%9B%AD%E6%85%A7&uicode=10000011&next_cursor=&page=",
    # 搜索关键词语：洪荒少女 可以运行
    "http://m.weibo.cn/page/pageJson?containerid=&containerid=100103type%3D1%26q%3D%E6%B4%AA%E8%8D%92%E5%B0%91%E5%A5%B3&type=all&queryVal=%E6%B4%AA%E8%8D%92%E5%B0%91%E5%A5%B3&title=%E6%B4%AA%E8%8D%92%E5%B0%91%E5%A5%B3&v_p=11&ext=&fid=100103type%3D1%26q%3D%E6%B4%AA%E8%8D%92%E5%B0%91%E5%A5%B3&uicode=10000011&next_cursor=&page=",
    # 搜索关键词语：洪荒少女傅园慧 可以运行
    "http://m.weibo.cn/page/pageJson?containerid=&containerid=100103type%3D1%26q%3D%E6%B4%AA%E8%8D%92%E5%B0%91%E5%A5%B3%E5%82%85%E5%9B%AD%E6%85%A7&type=all&queryVal=%E6%B4%AA%E8%8D%92%E5%B0%91%E5%A5%B3%E5%82%85%E5%9B%AD%E6%85%A7&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%B4%AA%E8%8D%92%E5%B0%91%E5%A5%B3&title=%E6%B4%AA%E8%8D%92%E5%B0%91%E5%A5%B3%E5%82%85%E5%9B%AD%E6%85%A7&v_p=11&ext=&fid=100103type%3D1%26q%3D%E6%B4%AA%E8%8D%92%E5%B0%91%E5%A5%B3%E5%82%85%E5%9B%AD%E6%85%A7&uicode=10000011&next_cursor=&page=",
    # 搜索关键词语：傅园慧表情包 可以运行
    "http://m.weibo.cn/page/pageJson?containerid=&containerid=100103type%3D1%26q%3D%E5%82%85%E5%9B%AD%E6%85%A7%E8%A1%A8%E6%83%85%E5%8C%85&type=all&queryVal=%E5%82%85%E5%9B%AD%E6%85%A7%E8%A1%A8%E6%83%85%E5%8C%85&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%B4%AA%E8%8D%92%E5%B0%91%E5%A5%B3%E5%82%85%E5%9B%AD%E6%85%A7&title=%E5%82%85%E5%9B%AD%E6%85%A7%E8%A1%A8%E6%83%85%E5%8C%85&v_p=11&ext=&fid=100103type%3D1%26q%3D%E5%82%85%E5%9B%AD%E6%85%A7%E8%A1%A8%E6%83%85%E5%8C%85&uicode=10000011&next_cursor=&page=",
    # 搜索关键词语：傅园慧直播 可以运行
    "http://m.weibo.cn/page/pageJson?containerid=&containerid=100103type%3D1%26q%3D%E5%82%85%E5%9B%AD%E6%85%A7%E7%9B%B4%E6%92%AD&type=all&queryVal=%E5%82%85%E5%9B%AD%E6%85%A7%E7%9B%B4%E6%92%AD&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%82%85%E5%9B%AD%E6%85%A7%E8%A1%A8%E6%83%85%E5%8C%85&title=%E5%82%85%E5%9B%AD%E6%85%A7%E7%9B%B4%E6%92%AD&v_p=11&ext=&fid=100103type%3D1%26q%3D%E5%82%85%E5%9B%AD%E6%85%A7%E7%9B%B4%E6%92%AD&uicode=10000011&next_cursor=&page=",
    # 搜索关键词语：洪荒之力 可以运行
    "http://m.weibo.cn/page/pageJson?containerid=&containerid=100103type%3D1%26q%3D%E6%B4%AA%E8%8D%92%E4%B9%8B%E5%8A%9B&type=all&queryVal=%E6%B4%AA%E8%8D%92%E4%B9%8B%E5%8A%9B&title=%E6%B4%AA%E8%8D%92%E4%B9%8B%E5%8A%9B&v_p=11&ext=&fid=100103type%3D1%26q%3D%E6%B4%AA%E8%8D%92%E4%B9%8B%E5%8A%9B&uicode=10000011&next_cursor=&page=",
    # 搜索关键词语：奥运傅园慧 可以运行
    "http://m.weibo.cn/page/pageJson?containerid=&containerid=100103type%3D1%26q%3D%E5%A5%A5%E8%BF%90%E5%82%85%E5%9B%AD%E6%85%A7&type=all&queryVal=%E5%A5%A5%E8%BF%90%E5%82%85%E5%9B%AD%E6%85%A7&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%B4%AA%E8%8D%92%E4%B9%8B%E5%8A%9B&title=%E5%A5%A5%E8%BF%90%E5%82%85%E5%9B%AD%E6%85%A7&v_p=11&ext=&fid=100103type%3D1%26q%3D%E5%A5%A5%E8%BF%90%E5%82%85%E5%9B%AD%E6%85%A7&uicode=10000011&next_cursor=&page=",
    # 搜索关键词语：里约傅园慧 可以运行
    "http://m.weibo.cn/page/pageJson?containerid=&containerid=100103type%3D1%26q%3D%E9%87%8C%E7%BA%A6%E5%82%85%E5%9B%AD%E6%85%A7&type=all&queryVal=%E9%87%8C%E7%BA%A6%E5%82%85%E5%9B%AD%E6%85%A7&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%A5%A5%E8%BF%90%E5%82%85%E5%9B%AD%E6%85%A7&title=%E9%87%8C%E7%BA%A6%E5%82%85%E5%9B%AD%E6%85%A7&v_p=11&ext=&fid=100103type%3D1%26q%3D%E9%87%8C%E7%BA%A6%E5%82%85%E5%9B%AD%E6%85%A7&uicode=10000011&next_cursor=&page=",
    # 搜索关键词语：傅园慧（香港） 可以运行
    "http://m.weibo.cn/page/pageJson?containerid=&containerid=100103type%3D1%26q%3D%E5%82%85%E5%9B%AD%E6%85%A7%EF%BC%88%E9%A6%99%E6%B8%AF%EF%BC%89&type=all&queryVal=%E5%82%85%E5%9B%AD%E6%85%A7%EF%BC%88%E9%A6%99%E6%B8%AF%EF%BC%89&luicode=10000011&lfid=100103type%3D1%26q%3D%E9%87%8C%E7%BA%A6%E5%82%85%E5%9B%AD%E6%85%A7&title=%E5%82%85%E5%9B%AD%E6%85%A7%EF%BC%88%E9%A6%99%E6%B8%AF%EF%BC%89&v_p=11&ext=&fid=100103type%3D1%26q%3D%E5%82%85%E5%9B%AD%E6%85%A7%EF%BC%88%E9%A6%99%E6%B8%AF%EF%BC%89&uicode=10000011&next_cursor=&page=",

    ]