import os
from flask import Flask
from threading import Thread
import telebot
import time
import requests

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

# ۱. بررسی دقیق کلمه‌ی سلام به صورت مستقل (به سلامتی گیر نمی‌دهد)
@bot.message_handler(func=lambda message: message.text and any(word.strip('،!؟.,؛»«()[]{}') == 'سلام' for word in message.text.split()))
def send_welcome(message):
    bot.send_message(message.chat.id, "سلام، خوبین ؟\nبه مشهد استار خوش اومدی 💫\nامیدوارم حال دلت خوب باشه 💞", reply_to_message_id=message.message_id)

# ۲. بررسی دقیق کلمات خداحافظ، خدافظ یا بای به صورت مستقل
@bot.message_handler(func=lambda message: message.text and any(word.strip('،!؟.,؛»«()[]{}') in ['خداحافظ', 'خدافظ', 'بای'] for word in message.text.split()))
def send_goodbye(message):
    bot.send_message(message.chat.id, "چه زود داری میری 🥺", reply_to_message_id=message.message_id)

# ۳. بررسی دقیق کلمات لف یا لفت به صورت مستقل
@bot.message_handler(func=lambda message: message.text and any(word.strip('،!؟.,؛»«()[]{}') in ['لف', 'لفت'] for word in message.text.split()))
def send_left(message):
    bot.send_message(message.chat.id, "خیلی بدی کجا میری منو تنها میزاری؟ 💔", reply_to_message_id=message.message_id)

if __name__ == '__main__':
    keep_alive()
    t_ping = Thread(target=self_ping)
    t_ping.start()
    
    bot.infinity_polling()
