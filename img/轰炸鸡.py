import http.cookiejar as cookiejar
import re
import time

import requests
import requests.utils

session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='./security.cookie')

BaseUrl = 'http://58.chuqing1.top/'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Referer": BaseUrl + "passport/login"}


def login(user, psw):
    try:
        data = {
            'username': user,
            'password': psw,
        }
        resp = session.post(url=BaseUrl + 'passport/login', headers=header, data=data)
        if resp.status_code == requests.codes.ok:
            session.cookies.save(ignore_discard=True, ignore_expires=True)
    except Exception as ex:
        print(ex)


def reset_operation():
    header["Referer"] = BaseUrl + "index/index"
    reset_object = {'phones[]': '15817262277',
                    'show_type': '1'}
    return_res = session.post(url=BaseUrl + 'index/stop', verify=False, headers=header)
    result = re.findall('<p class="success">(.*?)</p>', return_res.text, re.S)[0]
    print(result)
    return_res = session.post(url=BaseUrl + 'index/index', data=reset_object, verify=False, headers=header)
    result = re.findall('<p class="success">(.*?)</p>', return_res.text, re.S)[0]
    print(result)


def sleeptime(_hour, _min, _sec):
    return _hour * 3600 + _min * 60 + _sec


second = sleeptime(0, 0, 180)
login('qphhpl', 'pizmUg-cefto1-viczuq')

while 1 == 1:
    try:
        reset_operation()
        time.sleep(second)
    except BaseException as BEx:
        print(BEx)
        login('qphhpl', 'pizmUg-cefto1-viczuq')
        continue
