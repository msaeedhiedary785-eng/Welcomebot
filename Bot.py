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

# تابع تشخیص سلام واقعی (جلوی جملاتی مثل «سلام کرد» را می‌گیرد)
def check_real_greeting(text):
    text = text.strip()
    if text == 'سلام':
        return True
    if text.startswith('سلام'):
        words = text.split()
        # کلماتی که اگر بعد از سلام بیودند یعنی ربات نباید جواب بدهد
        bad_words = ['کرد', 'داد', 'گفت', 'رسوند', 'فرستاد', 'اومد', 'کردند', 'دادند', 'کردی']
        if len(words) > 1 and words[1] in bad_words:
            return False
        return True
    return False

# ۱. پاسخ به سلام واقعی
@bot.message_handler(func=lambda message: message.text and check_real_greeting(message.text))
def send_welcome(message):
    bot.send_message(message.chat.id, "سلام، خوبین ؟\nبه مشهد استار خوش اومدی 💫\nامیدوارم حال دلت خوب باشه 💞", reply_to_message_id=message.message_id)

# ۲. پاسخ به خداحافظ، خدافظ یا بای
@bot.message_handler(func=lambda message: message.text and bool(re.search(r'\b(خداحافظ|خدافظ|بای)\b', message.text)) and len(message.text.split()) <= 3)
def send_goodbye(message):
    bot.send_message(message.chat.id, "چه زود داری میری 🥺", reply_to_message_id=message.message_id)

# ۳. پاسخ به لف یا لفت
@bot.message_handler(func=lambda message: message.text and message.text.strip() in ['لف', 'لفت'])
def send_left(message):
    bot.send_message(message.chat.id, "خیلی بدی کجا میری منو تنها میزاری؟ 💔", reply_to_message_id=message.message_id)

if __name__ == '__main__':
    keep_alive()
    t_ping = Thread(target=self_ping)
    t_ping.start()
    
    bot.infinity_polling()
