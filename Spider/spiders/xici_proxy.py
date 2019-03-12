# -*- coding: utf-8 -*-
import MySQLdb
import requests
import scrapy
from Spider.items import XiciIPItem

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="allen", db="echo", charset="utf8")
cursor = conn.cursor()


class XiciProxySpider(scrapy.Spider):
    name = 'xici_proxy'
    allowed_domains = ['www.xicidaili.com']
    page_num = 1
    url = 'http://www.xicidaili.com/nn/{}'
    start_urls = [url.format(page_num)]

    def parse(self, response):
        ip_list = response.css('#ip_list tr')
        ip_list = response.css('#ip_list tr td::text')
        for ip_info in ip_list[1:]:
            item = XiciIPItem()
            item['ip'] = ip_info.css('td')[1].root.text
            item['port'] = ip_info.css('td')[2].root.text
            if len(ip_info.css('td')[3].css('a::text').extract()) != 0:
                item['position'] = ip_info.css('td')[3].css('a::text').extract()[0]
            else:
                item['position'] = ''
            item['anonymous'] = ip_info.css('td')[4].root.text
            item['proxy_type'] = ip_info.css('td')[5].root.text
            item['speed'] = ip_info.css('td div[title]')[0].root.attrib['title']
            item['connect_time'] = ip_info.css('td')[7].css('div[title]').attrib['title']
            item['alive_time'] = ip_info.css('td')[8].root.text
            item['verify_time'] = ip_info.css('td')[9].root.text
            yield item

        if 'href' in response.css('.next_page').attrib:
            self.page_num += 1
            yield scrapy.Request(self.url.format(self.page_num), callback=self.parse)


class GetIP(object):
    def delete_ip(self, ip):
        delete_sql = "DELETE FROM proxy_ip WHERE ip='{0}' ".format(ip)
        cursor.execute(delete_sql)
        conn.commit()
        return True

    def judge_ip(self, ip, port, proxy_type):
        # 判断ip是否可用
        http_url = "http://www.baidu.com"
        proxy_url = "{0}://{1}:{2}".format(proxy_type, ip, port)
        try:
            proxy_dict = {
                proxy_type: proxy_url,
            }
            response = requests.get(http_url, proxies=proxy_dict)
        except Exception as e:
            print("invalid ip and port")
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                print("effective ip")
                return True
            else:
                print("invalid ip and port")
                self.delete_ip(ip)
                return False

    def get_random_ip(self):
        # 从数据库中随机获取一个可用的ip
        random_sql = "SELECT ip,port,proxy_type FROM proxy_ip ORDER BY RAND() LIMIT 1"
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            proxy_type = ip_info[2]
            judge_re = self.judge_ip(ip, port, proxy_type)
            if judge_re:
                return "{0}://{1}:{2}".format(proxy_type, ip, port)
            else:
                return self.get_random_ip()
