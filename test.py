# # _*_encoding:utf-8_*_
# import requests
# from lxml import etree
#
# url = 'https://www.baidu.com'
#
# response = requests.get(url)
# response.encoding = 'utf8'
#x
# head = etree.HTML(response.text).xpath('//head')
# print(type(head[0].xpath('/title')))
# print(head[0].xpath('./title/text()'))
# # print(head.xpath('./title'))


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)


move(3, 'A', "B", 'C')
