from bot import telegram_chatbot

update_id = None

bot = telegram_chatbot("config.cfg")

def make_reply(msg):
    reply = None
    if msg == "123456":
        user = "Harsh"
        reply = "Hello Mr. Harsh, please tell me how you are feeling."
    elif msg == "I have cough and fever":
        reply = "Do you have any other symptoms."
    elif msg == "Yes I have difficulty in breathing":
        reply = "You have been in public places a lot recently. An immediate checkup is adviced. Please type Yes to continue to booking."
    elif msg == "I am feeling well":
        reply = "You have been in public places a lot recently. A checkup is adviced even though you seem to have no symptoms. You will be sent expert suggested remedies shortly, type Yes if you would like to book a medical appointment."
    elif msg == "Yes":
        reply = "Please visit https://github.com/harshagr18/DiseaseAssistant"
    elif msg == "234567":
        user = "Jagjeet"
        reply = "Hello Mr. Jagjeet, please tell me how you are feeling."
    elif msg == "I have fever":
        reply = "You have been at home for most of the past 15 days, So for your safety you will be sent a mail with expert suggested medicines and home remedies shortly. Please type Yes if you want to book a medical appointment."
    elif msg == "I am well":
        reply = "You have been at home for most of the past 15 days, you were probably flagged for recent unhealthy interactions. Be sure to avoid such interactions next time."
    elif msg == "Thank you":
        reply = "Stay safe, follow all safety guidelines and report all symptoms to get checked as soon as possible."
    elif msg is not None or "Reset":
        reply = "Hi! My name is CovidDiseaseAssistant, I am an AI Chatbot. Please tell me your CDA-ID. Type thank you to end the chat."
    return reply


while True:
    print("....")
    updates = bot.get_updates(offset = update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)