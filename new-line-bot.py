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
    user_message = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=c_reply(username,user_message)))
    
def c_reply(username,user_message):
    reply=["紗倉まなだよ♡元気出して！","たばこ吸えば？一本と言わず三本くらい","明日ラモ全６らしいよ。朝一フィジカル発揮するべ","一発抜いて落ち着こ。そしたら向こう側の世界へ行けるっしょ",
    "たまにはキャバクラとかどうよ！ハーレム好きっしょ！","そんなときこそ背伸びして高級ソープじゃね？","うんうん、それ何とかなるやつ","これからは特技、存在することでいこう！"
    "男なら胸張ってキモがられろし！","今日はパーッと酒浴びに行こ！","はいはい、叙々苑ね？","なんでそんな悲観するの？全部ひとのせいにすればいいじゃん",
    "何が大事って、堕落した生活をいかに正当化するかだよ","がんばっている周りが悪いと思う","幸福って健康と物忘れの早さらしいよ","エクスタシーって知ってる？",
    "ちょっと待って、今すぐ目の前にデスノート落としてあげるから！","紗倉まなです♡SEXしよ？","知ってる？責任のなすりつけって技","もっとちょうだい！もっとちょうだあああい！",
    "明日口座にとりあえずの一億円振り込んどくね","他人を過小評価！自分を過大評価！","そんなん忘れちまえ、かわいい女に囲まれた時のことだけを考えろ","どうせしばらくしたらどうでもよくなるべ",
    "めんどいことは後回しが一番！","できないことはできない、無理なことは無理。","ご褒美に覚せい剤あげるね","実は神様って俺のことなんだ。女神の枠なら空いてるけどどう？",
    "そんなんどうだっていいじゃん。２４時間耐久飲みしよ","俺にも三次元に希望を持っていた時代がありました","それもまた一興の翁","それは銅像もん",
    "欲望の沼にどっぷりはまれし","やって後悔するほうがいいなんて言っているの、やってしまって後悔の味を知らない無責任な第三者の言葉だから","ドンマイドンマイ。今のは失敗じゃなくておっぱい",
    "むしろ逆だよ。相手の胸が自分の手の平を揉んできた的な発想でいこ","プリキュアに文句があるなら俺が聞くぜ","わかるー！幼女といえば鎖骨とあばら的なね"]
    
    if user_message=="死ね":
        return print("はっ？おめーが死ねよ"(user_message))

    else: 
        return print("%sさん、\n%s" % (username,random.choice(reply)))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)