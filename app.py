import os,json
from flask import Flask, abort, request, send_file

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

from utils.reply import reply_richmenu,reply_about_coffee,reply_coffee_flavor,reply_coffee_items,reply_coffee_extract,reply_coffee_kind,reply_coffee_equipment,reply_coffee_filter_cup,reply_coffee_filter,reply_coffee_knife
app = Flask(__name__)

# line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
# handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))

line_bot_api = LineBotApi("dbbM28ETJ+6ot/LxKG5sORKg8LmevRxQ/4s3q8YLsH67eWLPKOfwYcBcw5Wy7RD3XqazJNuF7JQEcARruCxKWFgqY5TlPCv98sAlg1LfliDuIwVZSHVbNRN3/Y3cEXVCg/z3rx927elBhTVZDgsl8AdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("2ce0c6f86949b311bcafe1be06eccbe6")


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
    elif get_message in json_file["about_coffee"]:
        reply_about_coffee(line_bot_api,get_message,reply_token)
    elif get_message in json_file["coffee_kind"]:
        reply_coffee_kind(line_bot_api,get_message,reply_token)
    elif get_message in json_file["coffee_extract"]:
        reply_coffee_extract(line_bot_api,get_message,reply_token)
    elif get_message in json_file["coffee_filter_cup"]:
        reply_coffee_filter_cup(line_bot_api,get_message,reply_token)
    elif get_message in json_file["coffee_equipment"]:
        reply_coffee_equipment(line_bot_api,get_message,reply_token)
    elif get_message in json_file["coffee_filter"]:
        reply_coffee_filter(line_bot_api,get_message,reply_token)
    elif get_message in json_file["coffee_knife"]:
        reply_coffee_knife(line_bot_api,get_message,reply_token)
    elif get_message in json_file["coffee_flavor"]:
        reply_coffee_flavor(line_bot_api,get_message,reply_token)
    elif get_message in json_file["items"]:
        reply_coffee_items(line_bot_api,get_message,reply_token)


if __name__ == "__main__":
    app.run(debug=True,port=8000)