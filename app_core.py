# 載入需要的模組
from __future__ import unicode_literals
import os
import requests
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot','channel_access_token'))
handler = WebhookHandler(config.get('line-bot','channel_secret'))
#line_bot_api = LineBotApi('6IVswqsu9eK7XIjm3ez6qK736duTDWp1rSC06sJ1706/3m+9JeNK6IkKWkRqsSc00h2bKyInNA/g3tN+NdAbuGddDIXof+zynVgzcbwVZ2ThX5UHkXgDHYkMFQElkB/N68SQV9drTCGTSkIiiExiNQdB04t89/1O/w1cDnyilFU=')
#handler = WebhookHandler('5ffbfccf710ea7340ada71b68059f959')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# learn you how to talk
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        if event.message.text == "Does igogosport marley put on the shelf...":
            request_page1 = requests.get("https://store.igogosport.com/collections/refurbish?page=1")
            request_page2 = requests.get("https://store.igogosport.com/collections/refurbish?page=2")
            if 'Marley Liberate Air' in request_page1.text or 'Marley Liberate Air' in request_page2.text:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Marley Liberate Air put on the shelf'))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='No Not Yet'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()