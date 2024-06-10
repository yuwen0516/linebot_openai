from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from flask import Flask, request, abort

app = Flask(__name__)

# 替換為你的實際channel access token和channel secret
line_bot_api = LineBotApi('mJEbuHyFP8/Z+qMyD6Zhtxd8eY1403ryTIrNuoHSKz42f0TBlW3765kaLz/nRzrRA4sg4qEBH5oPQPa2TCz+CPR9w9tmoEpodOA0b7pHtas4auFyILcKO/fXE7upkK3RbwRu9mcDLYNQ55VMW002JgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('27f0cee2620555e6fc4e95338c69ad4e')

@app.route("/callback", methods=['POST'])
def callback():
    # 獲取X-Line-Signature頭信息
    signature = request.headers['X-Line-Signature']

    # 獲取請求主體作為文本
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 處理Webhook主體
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text.lower()

    if "預約資訊" in user_message or "reservation information" in user_message:
        response = get_waxing_info()
    elif "價格" in user_message or "price" in user_message:
        response = get_waxing_price()
    elif "服務" in user_message or "services" in user_message:
        response = get_waxing_services()
    elif "流程" in user_message or "process" in user_message:
        response = get_waxing_process()
    elif "好處" in user_message or "benefits" in user_message:
        response = get_waxing_benefits()
    elif "護理" in user_message or "aftercare" in user_message:
        response = get_waxing_aftercare()
    elif "常見問題" in user_message or "faq" in user_message:
        response = get_waxing_faq()
    else:
        response = "哈囉，請問想預約甚麼時候呢。"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response)
    )

def get_waxing_info():
    return (
        "這是預約資訊：\n"
        "1. 營業時間：週一至週五，上午10點至晚上8點\n"
        "2. 預約電話：123-456-789\n"
        "3. 地址：台北市某某路123號"
    )

def get_waxing_price():
    return (
        "這是我們熱蠟除毛服務的價格：\n"
        "1. 全腿：$50\n"
        "2. 半腿：$30\n"
        "3. 腋下：$20\n"
        "4. 巴西式：$70"
    )

def get_waxing_services():
    return (
        "我們提供以下熱蠟除毛服務：\n"
        "1. 全身除毛\n"
        "2. 面部除毛\n"
        "3. 腿部除毛\n"
        "4. 手臂除毛\n"
        "5. 腋下除毛\n"
        "6. 巴西式除毛"
    )

def get_waxing_process():
    return (
        "熱蠟除毛的流程如下：\n"
        "1. 清潔要除毛的區域。\n"
        "2. 塗上一層薄薄的溫蠟。\n"
        "3. 在蠟上覆蓋一條布條。\n"
        "4. 快速撕下布條，將毛髮從根部拔除。\n"
        "5. 塗抹舒緩乳液以減輕刺激。"
    )

def get_waxing_benefits():
    return (
        "熱蠟除毛的好處包括：\n"
        "1. 與刮毛相比，效果更持久。\n"
        "2. 長期使用會使毛髮變得更細、更軟。\n"
        "3. 使皮膚光滑並去除死皮。\n"
        "4. 減少刮傷和割傷的風險。"
    )

def get_waxing_aftercare():
    return (
        "熱蠟除毛後的護理建議：\n"
        "1. 24小時內避免熱水浴或淋浴。\n"
        "2. 避免使用含香精的產品。\n"
        "3. 穿寬鬆的衣物以避免刺激。\n"
        "4. 使用蘆薈膠或舒緩乳液來鎮定皮膚。\n"
        "5. 幾天後輕柔去角質以防止毛髮倒生。"
    )

def get_waxing_faq():
    return (
        "關於熱蠟除毛的常見問題：\n"
        "1. 熱蠟除毛會痛嗎？\n"
        "   - 會有一定的疼痛感，但隨著次數增加會減輕。\n"
        "2. 效果能持續多久？\n"
        "   - 通常效果可持續2到6週。\n"
        "3. 敏感肌膚可以使用熱蠟除毛嗎？\n"
        "   - 可以，但需要告知技術人員以便使用適當產品。\n"
        "4. 如何準備熱蠟除毛？\n"
        "   - 確保毛髮至少有1/4英寸長，並避免日曬或去角質。"
    )

if __name__ == "__main__":
    app.run()
