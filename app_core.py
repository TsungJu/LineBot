# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('aTGddjQMVPqULNFunkcprUUXJVpp/TVI2UD1aLllH11n/fuPwlDD1hYANRpW9lBj0h2bKyInNA/g3tN+NdAbuGddDIXof+zynVgzcbwVZ2Qn7hRK7PnlL+amkSNiXvtKVgH5L3+xeXPc2Jdf5UYvjgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9c3d76b74b879f46e09f85c65adc4d5b')

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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
