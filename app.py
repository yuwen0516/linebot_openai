from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from flask import Flask, request, abort

app = Flask(__name__)

# 替換為你的實際channel access token和channel secret
line_bot_api = LineBotApi('7iQrbcc3b04UWN4sULXeiHvSHwNsxXywQlxEKdJBRYeYbPGH95qQBBnqF6WlHpBaA4sg4qEBH5oPQPa2TCz+CPR9w9tmoEpodOA0b7pHtatBSprrXtPjXb1v9x7jHMEH9kz6dHP44u2RHdK31VfgNwdB04t89/1O/w1cDnyilFU=')
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

    if "預約資訊" in user_message or "預約" in user_message:
        response = get_waxing_info()
    elif "價格" in user_message or "價錢" in user_message:
        response = get_waxing_price()
    elif "服務" in user_message or "方面" in user_message:
        response = get_waxing_services()
    elif "流程" in user_message or "過程" in user_message:
        response = get_waxing_process()
    elif "好處" in user_message or "優點" in user_message:
        response = get_waxing_benefits()
    elif "護理" in user_message or "保養" in user_message:
        response = get_waxing_aftercare()
    elif "常見問題" in user_message or "問題" in user_message:
        response = get_waxing_faq()
    elif "天氣" in user_message or "氣候" in user_message:
        response = get_waxing_weather()
    else:
        response = "哈囉，我是負責回復熱蠟除毛相關的聊天機器人，有疑問我都能問你解答哦。"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response)
    )

def get_waxing_info():
    return (
        "這是預約資訊：\n"
        "1. 營業時間：週一至週五，上午10點至晚上8點\n"
        "2. 預約電話：0905076895\n"
        "3. 地址：宜蘭縣礁溪鄉林尾路160號"
    )

def get_waxing_price():
    return (
        "這是我們熱蠟除毛服務的價格：\n"
        "1. 半手臂：$500\n"
        "2. 全手臂：$1100\n"
        "3. 腋下：$350\n"
        "4. 小腿：$600"
        "5. 全腿：$1200"
        "6. 全手套餐：$1350"
        "7. 全腿套餐：$1400"
        "4. 手指：$100"
    )

def get_waxing_services():
    return (
        "我們提供以下熱蠟除毛服務：\n"
        "1. 全身除毛\n"
        "2. 腋下除毛\n"
        "3. 腿部除毛\n"
        "4. 手臂除毛\n"
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
    
def get_waxing_weather():
    return (
        "希望今天天氣是良好的!!但我是專門回復熱蠟除毛的聊天機器人哦 ~ 想了解更多可以詢問我相關問題。\n"
        
if __name__ == "__main__":
    app.run()
