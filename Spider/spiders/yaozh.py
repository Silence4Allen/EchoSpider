# -*- coding: utf-8 -*-
import scrapy


class YaozhSpider(scrapy.Spider):
    name = 'yaozh'
    allowed_domains = ['yaozh.com']
    # start_urls = ['https://www.yaozh.com/login/']

    def parse(self, response):
        login_url = 'https://www.yaozh.com/login/'

        # formhash = response.xpath('//input[@id="formhash"]/@value').extract_first()
        # backurl = response.xpath('//input[@id="backurl"]/@value').extract_first()
        formdata = {
            "username": "silence4allen",
            "pwd": "Allen501983707",
            # "formhash": formhash,
            # "backurl": backurl
        }
        # yield scrapy.FormRequest(url=login_url, formdata=formdata, callback=self.parse_login)
        yield scrapy.FormRequest.from_response(response=response, formid='login_pc', formdata=formdata,
                                               callback=self.parse_login, method='POST')

    def parse_login(self, response):
        member_url = 'https://www.yaozh.com/member/'
        yield scrapy.Request(member_url, callback=self.parse_member)

    def parse_member(self, response):
        with open('login_code2.html', 'wb')as f:
            f.write(response.body)
