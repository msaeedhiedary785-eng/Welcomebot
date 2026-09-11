import os
from flask import Flask
from threading import Thread
import telebot
import time
import requests
import re

TOKEN = '8628828031:AAFK0mSv7Sp2caHb9dmM02N3ITTqIfqVu5g'
bot = telebot.TeleBot(TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Bot is active and running!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

def self_ping():
    time.sleep(10)
    app_url = os.environ.get('RENDER_EXTERNAL_URL')
    if app_url:
        while True:
            try:
                requests.get(app_url)
            except:
                pass
            time.sleep(300)

# ۱. پاسخ به سلام (فقط وقتی پیام با سلام شروع شود)
@bot.message_handler(func=lambda message: message.text and message.text.strip().startswith('سلام'))
def send_welcome(message):
    bot.send_message(message.chat.id, "سلام، خوبین ؟\nبه مشهد استار خوش اومدی 💫\nامیدوارم حال دلت خوب باشه 💞", reply_to_message_id=message.message_id)

# ۲. پاسخ به خداحافظ، خدافظ یا بای (وقتی در انتهای متن یا به صورت کلمه مستقل بیاید)
@bot.message_handler(func=lambda message: message.text and bool(re.search(r'\b(خداحافظ|خدافظ|بای)\b', message.text)) and len(message.text.split()) <= 3)
def send_goodbye(message):
    bot.send_message(message.chat.id, "چه زود داری میری 🥺", reply_to_message_id=message.message_id)

# ۳. پاسخ به لف یا لفت (فقط وقتی خودِ پیام دقیقاً لف یا لفت باشد)
@bot.message_handler(func=lambda message: message.text and message.text.strip() in ['لف', 'لفت'])
def send_left(message):
    bot.send_message(message.chat.id, "خیلی بدی کجا میری منو تنها میزاری؟ 💔", reply_to_message_id=message.message_id)

if __name__ == '__main__':
    keep_alive()
    t_ping = Thread(target=self_ping)
    t_ping.start()
    
    bot.infinity_polling()
