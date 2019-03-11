import requests
import re
import random
import configparser
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

# from helper.ptt import *
# from helper.ptt_class import ptt_craw
from db.connect import Heroku_DB
from imgur.upload import uploader
from helper.function import *
from helper.reply import *


app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")

line_bot_api = LineBotApi(os.environ.get('Channel_Access_Token'))
handler = WebhookHandler(os.environ.get('Channel_Secret'))
client_id = os.environ.get('Client_ID')
client_secret = os.environ.get('Client_Secret')
access_token = os.environ.get('access_token')
refresh_token = os.environ.get('refresh_token')
album_id = os.environ.get('Album_ID')
ptt_beauty_album_id = os.environ.get('ptt_beauty_Album_ID')

conn = Heroku_DB()
uploader = uploader()
# ptt_craw = ptt_craw()

userid = ""
groupid = ""

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)

        profile = line_bot_api.get_profile(userid)
        print(profile.display_name)
        print(profile.user_id)
        print(profile.picture_url)
        print(profile.status_message)
        print("2019/02/22")

    except InvalidSignatureError:
        abort(400)

    if conn.IsExistUser(profile.user_id):
        db_info = conn.GetUserInfo(profile.user_id) #user_id, display_name, picture_url, status_message
        if ( db_info[1] != profile.display_name or db_info[2] != profile.picture_url or 
            db_info[3] != profile.status_message ):
            conn.UpdateUser(profile.user_id,profile.display_name, profile.picture_url, profile.status_message)

    else:
        conn.AddUser(profile.user_id,profile.display_name, profile.picture_url, profile.status_message)


    return 'ok'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)

    global userid
    global groupid
    userid = event.source.user_id
    groupid = event.source.user_id
    print("userid={},groupid={}".format(userid,groupid))

    line_bot_api.reply_message(
            event.reply_token,
            reply_content(event.message.text)
    )
    return 0

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    print("package_id:", event.message.package_id)
    print("sticker_id:", event.message.sticker_id)
    # ref. https://developers.line.me/media/messaging-api/sticker_list.pdf
    sticker_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 100, 101, 102, 103, 104, 105, 106,
                   107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,
                   126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 401, 402]
    index_id = random.randint(0, len(sticker_ids) - 1)
    sticker_id = str(sticker_ids[index_id])
    print(index_id)
    sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id=sticker_id
    )
    line_bot_api.reply_message(
        event.reply_token,
        sticker_message)


if __name__ == '__main__':

    app.run()