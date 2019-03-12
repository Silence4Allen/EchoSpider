# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import time

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class EchoChannelItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    pic = scrapy.Field()
    info = scrapy.Field()
    type = scrapy.Field()
    tag_id = scrapy.Field()
    sound_count = scrapy.Field()
    follow_count = scrapy.Field()
    like_count = scrapy.Field()
    share_count = scrapy.Field()
    user_id = scrapy.Field()
    update_user_id = scrapy.Field()
    list_order = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    status = scrapy.Field()
    desp = scrapy.Field()
    pic_100 = scrapy.Field()
    pic_200 = scrapy.Field()
    pic_500 = scrapy.Field()
    pic_640 = scrapy.Field()
    pic_750 = scrapy.Field()
    pic_1080 = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
          insert into copy_echo_channel(id,name,pic,info,type,tag_id,sound_count,follow_count,like_count,share_count,user_id,update_user_id,list_order,create_time,update_time,status,desp,pic_100,pic_200,pic_500,pic_640,pic_750,pic_1080)
          VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
          ON DUPLICATE KEY UPDATE name=VALUES(name),pic=VALUES(pic),info=VALUES(info),type=VALUES(type),tag_id=VALUES(tag_id),sound_count=VALUES(sound_count),follow_count=VALUES(follow_count),like_count=VALUES(like_count),share_count=VALUES(share_count),user_id=VALUES(user_id),update_user_id=VALUES(update_user_id),list_order=VALUES(list_order),create_time=VALUES(create_time),update_time=VALUES(update_time),status=VALUES(status),desp=VALUES(desp),pic_100=VALUES(pic_100),pic_200=VALUES(pic_200),pic_500=VALUES(pic_500),pic_640=VALUES(pic_640),pic_750=VALUES(pic_750),pic_1080=VALUES(pic_1080)
          """
        params = (self['id'],
                  self['name'],
                  self['pic'],
                  self['info'],
                  self['type'],
                  self['tag_id'],
                  self['sound_count'],
                  self['follow_count'],
                  self['like_count'],
                  self['share_count'],
                  self['user_id'],
                  self['update_user_id'],
                  self['list_order'],
                  timeformat(self['create_time']),
                  timeformat(self['update_time']),
                  self['status'],
                  self['desp'],
                  self['pic_100'],
                  self['pic_200'],
                  self['pic_500'],
                  self['pic_640'],
                  self['pic_750'],
                  self['pic_1080']
                  )
        return insert_sql, params


class EchoSoundItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    length = scrapy.Field()
    pic = scrapy.Field()
    channel_id = scrapy.Field()
    user_id = scrapy.Field()
    source = scrapy.Field()
    web_source = scrapy.Field()
    status_mask = scrapy.Field()
    commend_time = scrapy.Field()
    status = scrapy.Field()
    share_count = scrapy.Field()
    like_count = scrapy.Field()
    exchange_count = scrapy.Field()
    comment_count = scrapy.Field()
    view_count = scrapy.Field()
    is_edit = scrapy.Field()
    is_pay = scrapy.Field()
    check_visition = scrapy.Field()
    translate_mask = scrapy.Field()
    cover_song_id = scrapy.Field()
    cover_song_type = scrapy.Field()
    sound_type = scrapy.Field()
    create_time = scrapy.Field()
    parent_id = scrapy.Field()
    pic_100 = scrapy.Field()
    pic_200 = scrapy.Field()
    pic_500 = scrapy.Field()
    pic_640 = scrapy.Field()
    pic_750 = scrapy.Field()
    pic_1080 = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
          insert into copy_echo_sound(id,name,length,pic,channel_id,user_id,source,web_source,status_mask,commend_time,status,share_count,like_count,exchange_count,comment_count,view_count,is_edit,is_pay,check_visition,translate_mask,cover_song_id,cover_song_type,sound_type,create_time,parent_id,pic_100,pic_200,pic_500,pic_640,pic_750,pic_1080)
          VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
          ON DUPLICATE KEY UPDATE name=VALUES(name),length=VALUES(length),pic=VALUES(pic),channel_id=VALUES(channel_id),user_id=VALUES(user_id),source=VALUES(source),web_source=VALUES(web_source),status_mask=VALUES(status_mask),commend_time=VALUES(commend_time),status=VALUES(status),share_count=VALUES(share_count),like_count=VALUES(like_count),exchange_count=VALUES(exchange_count),comment_count=VALUES(comment_count),view_count=VALUES(view_count),is_edit=VALUES(is_edit),is_pay=VALUES(is_pay),check_visition=VALUES(check_visition),translate_mask=VALUES(translate_mask),cover_song_id=VALUES(cover_song_id),cover_song_type=VALUES(cover_song_type),sound_type=VALUES(sound_type),create_time=VALUES(create_time),parent_id=VALUES(parent_id),pic_100=VALUES(pic_100),pic_200=VALUES(pic_200),pic_500=VALUES(pic_500),pic_640=VALUES(pic_640),pic_750=VALUES(pic_750),pic_1080=VALUES(pic_1080)
          """

        params = (self['id'],
                  self['name'],
                  self['length'],
                  self['pic'],
                  self['channel_id'],
                  self['user_id'],
                  self['source'],
                  self['web_source'],
                  self['status_mask'],
                  timeformat(self['commend_time']),
                  self['status'],
                  self['share_count'],
                  self['like_count'],
                  self['exchange_count'],
                  self['comment_count'],
                  self['view_count'],
                  self['is_edit'],
                  self['is_pay'],
                  self['check_visition'],
                  self['translate_mask'],
                  self['cover_song_id'],
                  self['cover_song_type'],
                  self['sound_type'],
                  timeformat(self['create_time']),
                  self['parent_id'],
                  self['pic_100'],
                  self['pic_200'],
                  self['pic_500'],
                  self['pic_640'],
                  self['pic_750'],
                  self['pic_1080'])
        return insert_sql, params


class XiciIPItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    position = scrapy.Field()
    anonymous = scrapy.Field()
    proxy_type = scrapy.Field()
    speed = scrapy.Field()
    connect_time = scrapy.Field()
    alive_time = scrapy.Field()
    verify_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
          insert into proxy_ip(ip,port,position,anonymous,proxy_type,speed,connect_time,alive_time,verify_time)
          VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
          ON DUPLICATE KEY UPDATE port=VALUES(port),position=VALUES(position),anonymous=VALUES(anonymous),proxy_type=VALUES(proxy_type),speed=VALUES(speed),connect_time=VALUES(connect_time),alive_time=VALUES(alive_time),verify_time=VALUES(verify_time)
          """

        params = (
            self['ip'],
            self['port'],
            self['position'],
            self['anonymous'],
            self['proxy_type'],
            self['speed'],
            self['connect_time'],
            self['alive_time'],
            self['verify_time'],
        )
        return insert_sql, params


def timeformat(timeStamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(timeStamp)))
