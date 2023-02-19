import os,json
from flask import Flask, abort, request, send_file

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

from utils.reply import reply_richmenu,reply_coffee_roasting,reply_coffee_flavor
app = Flask(__name__)

# line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
# handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))



@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    get_message = event.message.text
    reply_token = event.reply_token

    with open("utils/keyword.json",'r',encoding='utf-8') as j:
        json_file=json.load(j)
    
    if get_message in json_file["rich_menu"]:
        reply_richmenu(line_bot_api,get_message,reply_token)
    elif get_message in json_file["coffee_roasting"]:
        reply_coffee_roasting(line_bot_api,get_message,reply_token)
    elif get_message in json_file["coffee_flavor"]:
        reply_coffee_flavor(line_bot_api,get_message,reply_token)


if __name__ == "__main__":
    app.run(debug=True,port=8080)