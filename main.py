import requests
import time
import telebot

TOKEN = '7635618563:AAEHHu5pBIULmQM00MefFvAZaGxdJBZywW8'
CHANNEL = '@NebesnaVarta'

bot = telebot.TeleBot(TOKEN)

def get_alerts():
    url = 'https://alerts.com.ua/api/states'
    try:
        r = requests.get(url)
        data = r.json()
        active = [region['name'] for region in data if region['alert']]
        return active
    except:
        return []

last_alerts = []

while True:
    current_alerts = get_alerts()
    if current_alerts != last_alerts:
        if current_alerts:
            text = "🔴 Повітряна тривога!\n\n" + "\n".join(current_alerts)
        else:
            text = "🟢 Відбій повітряної тривоги."
        bot.send_message(CHANNEL, text)
        last_alerts = current_alerts
    time.sleep(30)
