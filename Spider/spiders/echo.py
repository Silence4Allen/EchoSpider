# -*- coding: utf-8 -*-
import json
import re

import scrapy
from Spider.items import EchoChannelItem, EchoSoundItem


class EchoSpider(scrapy.Spider):
    name = 'echo'
    allowed_domains = ['app-echo.com']
    url = 'http://www.app-echo.com/api/channel/index?page={}'
    channel_list_page_num = 1
    # start_urls = [url.format(channel_list_page_num)]
    headers = {
        'Host': 'www.app-echo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }

    def parse(self, response):
        # 页面数据
        page_data = json.loads(response.text)
        # 频道数据
        channels = page_data['channels']
        if len(channels) == 0:
            return
        for channelData in channels:
            channel_item = EchoChannelItem()
            channel_item['id'] = channelData['id']
            channel_item['name'] = channelData['name']
            channel_item['pic'] = channelData['pic']
            channel_item['info'] = channelData['info']
            channel_item['type'] = channelData['type']
            channel_item['tag_id'] = channelData['tag_id']
            channel_item['sound_count'] = channelData['sound_count']
            channel_item['follow_count'] = channelData['follow_count']
            channel_item['like_count'] = channelData['like_count']
            channel_item['share_count'] = channelData['share_count']
            channel_item['user_id'] = channelData['user_id']
            channel_item['update_user_id'] = channelData['update_user_id']
            channel_item['list_order'] = channelData['list_order']
            channel_item['create_time'] = channelData['create_time']
            channel_item['update_time'] = channelData['update_time']
            channel_item['status'] = channelData['status']
            channel_item['desp'] = channelData['desp']
            channel_item['pic_100'] = channelData['pic_100']
            channel_item['pic_200'] = channelData['pic_200']
            channel_item['pic_500'] = channelData['pic_500']
            channel_item['pic_640'] = channelData['pic_640']
            channel_item['pic_750'] = channelData['pic_750']
            channel_item['pic_1080'] = channelData['pic_1080']
            yield channel_item
            # 获取音乐数据
            music_normal_url = 'http://www.app-echo.com/api/channel/info?id={}&page=1'
            music_hot_url = 'http://www.app-echo.com/api/channel/info?id={}&order=hot&page=1'
            music_new_url = 'http://www.app-echo.com/api/channel/info?id={}&order=new&page=1'
            yield scrapy.Request(music_normal_url.format(channelData['id']), callback=self.parse_music_list)
            yield scrapy.Request(music_hot_url.format(channelData['id']), callback=self.parse_music_list)
            yield scrapy.Request(music_new_url.format(channelData['id']), callback=self.parse_music_list)
        # 获取下一页频道数据
        self.channel_list_page_num += 1
        yield scrapy.Request(self.url.format(self.channel_list_page_num), callback=self.parse)

    def parse_music_list(self, response):
        print(response.url)
        # 页面数据
        page_data = json.loads(response.text)
        # 音乐列表数据
        sounds = page_data['sounds']
        if len(sounds) == 0:
            return
        for soundData in sounds:
            sound_item = EchoSoundItem()
            sound_item['id'] = soundData['id']
            sound_item['name'] = soundData['name']
            sound_item['length'] = soundData['length']
            sound_item['pic'] = soundData['pic']
            sound_item['channel_id'] = soundData['channel_id']
            sound_item['user_id'] = soundData['user_id']
            sound_item['source'] = soundData['source']
            sound_item['web_source'] = soundData['web_source']
            sound_item['status_mask'] = soundData['status_mask']
            sound_item['commend_time'] = soundData['commend_time']
            sound_item['status'] = soundData['status']
            sound_item['share_count'] = soundData['share_count']
            sound_item['like_count'] = soundData['like_count']
            sound_item['exchange_count'] = soundData['exchange_count']
            sound_item['comment_count'] = soundData['comment_count']
            sound_item['view_count'] = soundData['view_count']
            sound_item['is_edit'] = soundData['is_edit']
            sound_item['is_pay'] = soundData['is_pay']
            sound_item['check_visition'] = soundData['check_visition']
            sound_item['translate_mask'] = soundData['translate_mask']
            sound_item['cover_song_id'] = soundData['cover_song_id']
            sound_item['cover_song_type'] = soundData['cover_song_type']
            sound_item['sound_type'] = soundData['sound_type']
            sound_item['create_time'] = soundData['create_time']
            sound_item['parent_id'] = soundData['parent_id']

            sound_item['pic_100'] = soundData['pic_100'] if 'pic_100' in soundData else ""
            sound_item['pic_200'] = soundData['pic_200'] if 'pic_200' in soundData else ""
            sound_item['pic_500'] = soundData['pic_500'] if 'pic_500' in soundData else ""
            sound_item['pic_640'] = soundData['pic_640'] if 'pic_640' in soundData else ""
            sound_item['pic_750'] = soundData['pic_750'] if 'pic_750' in soundData else ""
            sound_item['pic_1080'] = soundData['pic_1080'] if 'pic_1080' in soundData else ""
            yield sound_item
        # 获取下一页音乐列表数据
        result = re.match('.*page=([0-9]+).*', response.url)
        current_page_num = result.group(1)
        next_url = response.url.replace("page=" + current_page_num, "page=" + str(int(current_page_num) + 1))
        yield scrapy.Request(next_url, callback=self.parse_music_list)
