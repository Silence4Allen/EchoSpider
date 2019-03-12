# _*_encoding:utf-8_*_
import json
import re
import time

from utils.common import dict_2_items
from Spider.items import EchoSoundItem

channel = """
id: "1155",
name: "3D音乐奇幻旋律馆",
pic: "https://al-qn-echo-image-cdn.app-echo.com/FqQlWfVj9384hIaTVIjYgsVQsFdg",
info: "echo独家3D音乐，颠覆你的听觉体验",
type: "1",
tag_id: "5",
sound_count: "46482",
follow_count: "1359887",
like_count: "0",
share_count: "17521",
user_id: "160623",
update_user_id: "21380497",
list_order: "582649",
create_time: "1427449337",
update_time: "1511576206",
status: "1",
desp: "",
pic_100: "https://al-qn-echo-image-cdn.app-echo.com/FqQlWfVj9384hIaTVIjYgsVQsFdg?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/100/q/100",
pic_200: "https://al-qn-echo-image-cdn.app-echo.com/FqQlWfVj9384hIaTVIjYgsVQsFdg?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/200/q/100",
pic_500: "https://al-qn-echo-image-cdn.app-echo.com/FqQlWfVj9384hIaTVIjYgsVQsFdg?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/500/q/100",
pic_640: "https://al-qn-echo-image-cdn.app-echo.com/FqQlWfVj9384hIaTVIjYgsVQsFdg?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/640/q/100",
pic_750: "https://al-qn-echo-image-cdn.app-echo.com/FqQlWfVj9384hIaTVIjYgsVQsFdg?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/750/q/100",
pic_1080: "https://al-qn-echo-image-cdn.app-echo.com/FqQlWfVj9384hIaTVIjYgsVQsFdg?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/1080/q/100"
"""
sound = """{
id: "1587706",
name: "Blank Space",
length: "231",
pic: "https://al-qn-echo-image-cdn.app-echo.com/FgBGKnTFx8keqW4SgPpDlWUw15XX",
channel_id: "190",
user_id: "3445531",
source: "https://al-qn-echo-cp-cdn.app-echo.com/c2/0213d3cfc441d6e2e4a1c7854bab5df1f9de4241448dc2cf4fa78ec7fadf6ecf976ed643.mp3?1457936362",
web_source: "",
status_mask: "8",
commend_time: "0",
status: "1",
share_count: "95",
like_count: "252",
exchange_count: "95",
comment_count: "7",
view_count: 6073,
is_edit: "2",
is_pay: 0,
check_visition: 1,
translate_mask: 0,
cover_song_id: 0,
cover_song_type: 0,
sound_type: 1,
create_time: 1521550471,
parent_id: "0",
pic_100: "https://al-qn-echo-image-cdn.app-echo.com/FgBGKnTFx8keqW4SgPpDlWUw15XX?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/100/q/100",
pic_200: "https://al-qn-echo-image-cdn.app-echo.com/FgBGKnTFx8keqW4SgPpDlWUw15XX?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/200/q/100",
pic_500: "https://al-qn-echo-image-cdn.app-echo.com/FgBGKnTFx8keqW4SgPpDlWUw15XX?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/500/q/100",
pic_640: "https://al-qn-echo-image-cdn.app-echo.com/FgBGKnTFx8keqW4SgPpDlWUw15XX?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/640/q/100",
pic_750: "https://al-qn-echo-image-cdn.app-echo.com/FgBGKnTFx8keqW4SgPpDlWUw15XX?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/750/q/100",
pic_1080: "https://al-qn-echo-image-cdn.app-echo.com/FgBGKnTFx8keqW4SgPpDlWUw15XX?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/1080/q/100"
}
"""

# sound_data = {
#     "id": "1587706",
#     "name": "Blank Space",
#     "pic_200": "https://al-qn-echo-image-cdn.app-echo.com/FgBGKnTFx8keqW4SgPpDlWUw15XX?imageMogr2/auto-orient/quality/100%7CimageView2/0/w/200/q/100",
# }
#
# # str = dict_2_items(sound)
# # # str = itemAttrSameAsDictAttr("soundItem", "sound", str)
# sound_item = EchoSoundItem()
# sound_item['id'] = sound_data['id']
# sound_item['name'] = sound_data['name']
#
# if 'pic_100' in sound_data:
#     sound_item['pic_100'] = sound_data['pic_100']
# sound_item['pic_200'] = sound_data['pic_200']
#
# print(sound_item)


print(time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time())))
