from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from flask import Flask, request, abort

app = Flask(__name__)

# Replace these with your actual channel access token and channel secret
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('7iQrbcc3b04UWN4sULXeiHvSHwNsxXywQlxEKdJBRYeYbPGH95qQBBnqF6WlHpBaA4sg4qEBH5oPQPa2TCz+CPR9w9tmoEpodOA0b7pHtatBSprrXtPjXb1v9x7jHMEH9kz6dHP44u2RHdK31VfgNwdB04t89/1O/w1cDnyilFU=')

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

    if "reservation information" in user_message:
        response = get_waxing_info()
    elif "price" in user_message:
        response = get_waxing_price()
    elif "services" in user_message:
        response = get_waxing_services()
    elif "process" in user_message:
        response = get_waxing_process()
    elif "benefits" in user_message:
        response = get_waxing_benefits()
    elif "aftercare" in user_message:
        response = get_waxing_aftercare()
    elif "faq" in user_message:
        response = get_waxing_faq()
    else:
        response = "Hello, when would you like to make a reservation?"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=response)
    )

def get_waxing_info():
    return (
        "Here is the reservation information:\n"
        "1. Business hours: Monday to Friday, 10 AM to 8 PM\n"
        "2. Reservation phone number: 123-456-789\n"
        "3. Address: 123 Some Street, Taipei City"
    )

def get_waxing_price():
    return (
        "Here are the prices for our waxing services:\n"
        "1. Full leg: $50\n"
        "2. Half leg: $30\n"
        "3. Underarm: $20\n"
        "4. Brazilian: $70"
    )

def get_waxing_services():
    return (
        "We offer the following waxing services:\n"
        "1. Full body waxing\n"
        "2. Facial waxing\n"
        "3. Leg waxing\n"
        "4. Arm waxing\n"
        "5. Underarm waxing\n"
        "6. Brazilian waxing"
    )

def get_waxing_process():
    return (
        "The waxing process involves the following steps:\n"
        "1. Cleaning the area to be waxed.\n"
        "2. Applying a thin layer of warm wax.\n"
        "3. Placing a cloth strip over the wax.\n"
        "4. Quickly pulling the strip off, removing the hair from the root.\n"
        "5. Applying a soothing lotion to reduce irritation."
    )

def get_waxing_benefits():
    return (
        "Benefits of waxing include:\n"
        "1. Longer-lasting results compared to shaving.\n"
        "2. Finer and softer regrowth over time.\n"
        "3. Smooth and exfoliated skin.\n"
        "4. Reduced risk of cuts and nicks."
    )

def get_waxing_aftercare():
    return (
        "Aftercare tips for waxing:\n"
        "1. Avoid hot baths or showers for 24 hours.\n"
        "2. Refrain from using perfumed products on the waxed area.\n"
        "3. Wear loose clothing to avoid irritation.\n"
        "4. Apply aloe vera gel or a soothing lotion to calm the skin.\n"
        "5. Exfoliate gently after a few days to prevent ingrown hairs."
    )

def get_waxing_faq():
    return (
        "Frequently Asked Questions (FAQ) about waxing:\n"
        "1. Does waxing hurt?\n"
        "   - Some discomfort is normal, but it becomes less painful over time.\n"
        "2. How long do the results last?\n"
        "   - Typically, waxing results last 3-6 weeks.\n"
        "3. Can I wax if I have sensitive skin?\n"
        "   - Yes, but inform your technician so they can use appropriate products.\n"
        "4. How should I prepare for my waxing appointment?\n"
        "   - Ensure the hair is at least 1/4 inch long and avoid sun exposure or exfoliating the area on the day of your appointment."
    )

if __name__ == "__main__":
    app.run()
