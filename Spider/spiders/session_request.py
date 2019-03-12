# _*_encoding:utf-8_*_
import re

import requests

__author__ = 'Allen'
__date__ = '2018/12/16 23:54'

try:
    import cookielib
except:
    import http.cookiejar as cookielib

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")

try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie未能加载")

headers = {
    'Host': 'www.app-echo.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}


def get_csrf():
    response = session.get("https://www.app-echo.com/#/", headers=headers, verify=False, allow_redirects=False)
    match_obj = re.match('.*<meta name="csrf-token" content="(.*?)"', response.text.replace('\n', ''))
    if match_obj:
        return match_obj.group(1)
    else:
        return ""


def login_echo():
    url = 'http://www.app-echo.com/user/ajax-login'
    account = 18126106725
    password = 'Allen501983707'
    data = {
        'login_form[name]': account,
        'login_form[password]': password,
        'login_form[area-code]': '+86',
        '_csrf': get_csrf()
    }
    session.post(url=url, data=data, headers=headers)
    session.cookies.save()


def get_index():
    response = session.get('http://www.app-echo.com/#/channel?order=my-channels', headers=headers)
    with open("index_page.html", "wb")as f:
        f.write(response.text.encode('utf-8'))
    print("ok")


if __name__ == "__main__":
    login_echo()
    # get_index()
