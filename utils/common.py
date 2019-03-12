# _*_encoding:utf-8_*_
__author__ = 'Allen'
__date__ = '2018/12/18 22:31'


def cookie_str_2_cookie_format(cookies_str):
    return {cookie.split("=")[0]: cookie.split("=")[1] for cookie in cookies_str.split("; ")}


def dict_2_items(dict_str):
    l = [line.split(":")[0] + "=" + "scrapy.Field()" for line in dict_str.replace('"', '').split(',')]
    str = ""
    for m in l:
        str += m
    return str


def itemAttrSameAsDictAttr(itemName, dictName, str):
    l = [itemName + "['" + line.split("=")[0] + "']" + "=" + dictName + "['" + line.split("=")[0] + "']" for line in
         str.split("\n")]
    str = ""
    for m in l:
        str += m + "\n"
    return str
