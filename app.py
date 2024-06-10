from flask import Flask, request, abort, render_template_string
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from gemini import Gemini

app = Flask(__name__)

# 設置LINE Bot的配置信息
line_bot_api = LineBotApi('mJEbuHyFP8/Z+qMyD6Zhtxd8eY1403ryTIrNuoHSKz42f0TBlW3765kaLz/nRzrRA4sg4qEBH5oPQPa2TCz+CPR9w9tmoEpodOA0b7pHtas4auFyILcKO/fXE7upkK3RbwRu9mcDLYNQ55VMW002JgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('27f0cee2620555e6fc4e95338c69ad4e')

# 創建Gemini實例
bot = Gemini()

# 定義熱蠟除毛相關的對話
bot.add_dialogue("你想了解什麼關於熱蠟除毛的問題？", [
    ("我想知道熱蠟除毛的步驟", "熱蠟除毛的步驟如下：\n1. 清潔皮膚\n2. 加熱蠟\n3. 塗抹蠟\n4. 撕除蠟\n5. 保濕皮膚"),
    ("熱蠟除毛有什麼注意事項？", "熱蠟除毛的注意事項包括：\n1. 確保皮膚乾淨\n2. 測試蠟溫度\n3. 避免重複除毛同一區域\n4. 使用後保濕"),
    ("熱蠟除毛的優點是什麼？", "熱蠟除毛的優點有：\n1. 可以去除短毛\n2. 效果持久\n3. 能夠去除角質\n4. 毛髮再生較細軟"),
    ("熱蠟除毛有什麼缺點？", "熱蠟除毛的缺點包括：\n1. 可能引起皮膚刺激\n2. 可能會痛\n3. 需要時間學習技巧\n4. 可能引起過敏反應")
])

def render_response(response_text):
    # 這裡可以使用 Flask 的 render_template_string 渲染回應內容
    template = """
    {{ response_text }}
    """
    return render_template_string(template, response_text=response_text)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    # 使用Gemini處理用戶信息
    response = bot.generate_response(user_message)
    # 渲染回應
    rendered_response = render_response(response)
    # 回覆用戶
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=rendered_response)
    )

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

if __name__ == "__main__":
    app.run()
