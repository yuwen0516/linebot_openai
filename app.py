from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from flask import Flask, request, abort

app = Flask(__name__)

# Replace these with your actual channel access token and channel secret
line_bot_api = LineBotApi('7iQrbcc3b04UWN4sULXeiHvSHwNsxXywQlxEKdJBRYeYbPGH95qQBBnqF6WlHpBaA4sg4qEBH5oPQPa2TCz+CPR9w9tmoEpodOA0b7pHtatBSprrXtPjXb1v9x7jHMEH9kz6dHP44u2RHdK31VfgNwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('27f0cee2620555e6fc4e95338c69ad4e')

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
    user_message = event.message.text.lower()

    if "流程" in user_message or "流程" in user_message::
        response = get_waxing_info()
    elif "痛" in user_message:
        response = get_waxing_price()
    elif "部位" in user_message:
        response = get_waxing_services()
    elif "多久" in user_message:
        response = get_waxing_process()
    elif "降低疼痛感" in user_message:
        response = get_waxing_benefits()
    elif "粗" in user_message:
        response = get_waxing_aftercare()
    elif "不適合" in user_message "不能" in user_message "不可以" in user_message:
        response = get_waxing_faq()
    else:
        response = "你好，我是你的專屬聊天機器人可以詢問我關於熱蠟方面的小知識哦 !"
        response = "如果還有其他問題 我可以盡力回答你哦 !"


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response)
    )

def get_waxing_info():
    return (
        "這裡有幾個小流程:\n"
        "1.清潔皮膚：在開始除毛之前，需要清潔和乾燥要處理的皮膚區域。\n"
        "2. 加熱蠟：蠟加熱到適宜的溫度，通常為溫熱但不會燙傷皮膚。\n"
        "3. 塗抹蠟：用蠟刀或木棒將蠟均勻地塗抹在皮膚上，順著毛髮生長的方向塗抹。\n"
        "4. 覆蓋蠟布：在蠟還熱的時候，迅速覆蓋一條蠟布或紙條。\n"
        "5. 撕除蠟布：待蠟稍微冷卻並變硬後，逆著毛髮生長的方向迅速撕除蠟布，將毛髮拔除。\n"
        "6. 舒緩皮膚：最後，塗抹舒緩的乳液或芦荟膠來減輕刺激和紅腫。\n"
    )

def get_waxing_price():
    return (
        "會有一定的疼痛感，尤其是第一次。但隨著次數增加，疼痛感會減輕。\n"
    )

def get_waxing_services():
    return (
        "熱蠟除毛適用於全身各部位，包括腿部、手臂、腋下、面部和比基尼區。\n"
    )

def get_waxing_process():
    return (
        "由於每個人的體質與毛髮生長的速度、週期不同，大約維持3-6個禮拜\n"
    )

def get_waxing_benefits():
    return (
        "除毛前不喝含咖啡因或酒精的飲品，因為咖啡因跟酒精會加速血液循環、讓痛感傳遞較快。也避免月事來的前五天後三天進行除毛，這段時程的皮膚會比較敏感，痛覺比較容易被放大。\n"
    )

def get_waxing_aftercare():
    return (
        "使用熱蠟除毛時，雖然會將毛髮連根拔除，因為過程中會讓毛囊周圍的養分供應降低，所以毛髮生長速度會變慢，長出來的毛髮也比較細緻。人體也會自動修復，每做一次熱蠟除毛，都會讓毛髮從頭開始生長，所以毛髮重生的時候會更細軟。\n"
    )

def get_waxing_faq():
    return (
        "1.欲除毛處皮膚變薄，如：果酸換膚、磨皮\n"
        "2. 近一週內有接受皮膚科痘痘藥物治療中，如：維他命A\n"
        "4. 近一週內有皮下為整修注射，如：肉毒桿菌、微晶瓷、玻尿酸\n"
        "4. 近一週內皮膚有使用果酸換膚產品\n"  
    )

if __name__ == "__main__":
    app.run()
