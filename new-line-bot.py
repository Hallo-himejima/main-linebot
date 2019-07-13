#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

import random

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = "Okmn/+loVcvxpPO9LauGC8IGAYFdCjRGxlzw0EIa3XTwxJaQh0b/H7rBIQjRDLLD9ie9yn1nuGUgletZRjcyue//Y9tPKb5sBc8icSXcY0Y2b5uJ/DurOd1kSmq4P7xg58Ux8teOYnxlclYbDL4wGwdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET = "38eb69f2d123b875e8537d35ba63aa39"

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    username = profile.display_name

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=hoge(username)))

def hoge(username):
    reply=["おはよう","こんにちわ","こんばんわ"]
    return "%sさん、\n%s" % (username,random.choice(reply))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)