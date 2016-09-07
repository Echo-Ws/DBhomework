# -*-coding:utf-8-*-
username = "huangzhen_hua@yeah.net"
password = "zhenhua123456"

import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import time
# from logconfig import LogConfig
# logger = LogConfig.get_logger()
import logging
logger = logging.getLogger('searchlogger')
class WeiboLogin(object):

    def __init__(self):
        self.headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate",
            "Connection":"keep-alive",
            "Host":"passport.weibo.cn",
            "Referer":"https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F&wm=3349&vt=4",
            "User-Agent":"Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
        }
        self.params = {
        "entry":"mweibo",
        "r":"http://m.weibo.cn/",
        "res":"wel",
        "wm":"3349"
        }

    def login(self):
        s=requests.session()
        s.headers.update(self.headers)
        login_url = "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F"
        r = s.get(login_url,params=self.params,headers = self.headers)
        # print(r.text)
        andriod = "Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
        apple = "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/47.0.2526.70 Mobile/13C71 Safari/601.1.46"
        headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"keep-alive",
        "Host":"passport.weibo.cn",
        "Origin":"https://passport.weibo.cn",
        "Referer":"https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F&wm=3349&vt=4",
        "User-Agent":apple
        }

        url = "https://passport.weibo.cn/sso/login"
        login_data = {
            "username":username,
            "password":password,
            "savestate":1,
            "ec":1,
            "pagerefer":"https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F&wm=3349&vt=4",
            "entry":"mweibo"
        }
        time.sleep(2)
        r = s.post(url,data = login_data, headers=headers)
        # print(r.text)
        # print(s.cookies)

        s.headers.update(host="m.weibo.cn")
        main_url = "http://m.weibo.cn/u/1887790981"
        r = s.get(main_url,headers = s.headers)
        # print(r.text)
        return s

    def login_un(self):
        # cookies = "SUHB=0auBPMPDwjssqA; _T_WM=f91dc78ecf37303868fab47d55d19e37; browser=d2VpYm9mYXhpYW4%3D; h5_deviceID=aead5802f423525493b50cd1b58fee77; H5_INDEX=1; H5_INDEX_TITLE=%E9%BB%84%E6%8C%AF%E5%8D%8E_SCUT; SUB=_2A256P6YQDeRxGeRP71IT8inPyDiIHXVZw8pYrDV6PUJbrdBeLVikkW1LHeucfJTgq2kSrwyQT6mfxcAKg7IdPg..; SSOLoginState=1463539264; gsid_CTandWM=4uLVCpOz5bKnwnPetSDg08YLN5o"
        cookies = "SUHB=010W03JLPX8mn7; _T_WM=f91dc78ecf37303868fab47d55d19e37; browser=d2VpYm9mYXhpYW4%3D; h5_deviceID=aead5802f423525493b50cd1b58fee77; SUB=_2A256OUOzDeTxGeNM41AS8yzMzzSIHXVZwm37rDV6PUJbrdBeLUb4kW1LHeuQyqRSKEJo7Na_eyQIGB5P85AOeg..; H5_INDEX=2; H5_INDEX_TITLE=%E4%BC%8A%E5%8A%BF%E8%B0%B7%E5%B0%8A%E9%AA%82; gsid_CTandWM=4u2YCpOz5qeBDSJ8MnPD2maaU0M"
        # cookies = "SUHB=079imRprMx4HcP; _T_WM=f91dc78ecf37303868fab47d55d19e37; SUB=_2A256K3IjDeRxGeRP71IT8inPyDiIHXVZ1B5rrDV6PUJbrdBeLWzTkW1LHes_HcQ6KZdn1HIPHcVY7Itoh_d0QA..; browser=d2VpYm9mYXhpYW4%3D; h5_deviceID=aead5802f423525493b50cd1b58fee77; H5_INDEX=1; H5_INDEX_TITLE=%E9%BB%84%E6%8C%AF%E5%8D%8E_SCUT; gsid_CTandWM=4uChCpOz5TcReq04qZiBU8YLN5o; M_WEIBOCN_PARAMS=featurecode%3D20000180%26oid%3D3975106739490992%26luicode%3D20000061%26lfid%3D3975106739490992"
        # cookies = "_T_WM=e71a0290dcb15e9ae09d27b6df430c25; SUB=_2A256zpvkDeTxGeVN41AX-CnFzjiIHXVWMCWsrDV6PUJbkdBeLVTRkW0SgemVSBoo0PYgbvYntdQser2VmQ..; SUHB=0wnl0Gl7Q5X7O8; SCF=Ar6fvTQvrEpeTkkEvm8m_PP0x4upYqeuDhHVFjSuXfkg1jTwA2yAXB-kWy-a5URhn3HNdhzAXmHloXQHkf_KJUA.; SSOLoginState=1472916404; M_WEIBOCN_PARAMS=uicode%3D20000174"

        headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', \
                   'Cookie':cookies,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', \
                   'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', \
                   'host': 'm.weibo.cn', 'Referer': 'http://m.weibo.cn/'}
        # headers = {'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',}
        follower_url = "http://m.weibo.cn/page/tpl?containerid=1005051898385314_-_FOLLOWERS"
        s = requests.session()
        s.headers.update(headers)
        r = s.get(follower_url,headers=s.headers)

        return s
def test():
    w_login = WeiboLogin()
    s = w_login.login()

    follower_url = "http://m.weibo.cn/page/tpl?containerid=1005051898385314_-_FOLLOWERS"
    r = s.get(follower_url, headers = s.headers)
    # print(r.text)
    page_num = 1
    import json
    import random
    for i in range(0,10):
        follower_url = "http://m.weibo.cn/page/json?containerid=1005051898385314_-_FOLLOWERS&page=%s"%page_num
        r = s.get(follower_url,headers = s.headers)
        data = r.text
        # print("\n\n")
        print(data)
        data_json = json.loads(data)
        # 判断是否到头
        if data_json['count'] is None:
            print("finish")
            break;
        print(data_json['count'])
        print(data_json['cards'])
        page_num += 1
        time.sleep(random.uniform(0,3))
# test()