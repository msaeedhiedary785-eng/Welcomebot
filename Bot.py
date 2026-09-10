import os
from flask import Flask
from threading import Thread
import telebot
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

# پاسخ به سلام (فقط کلمه‌ی کامل سلام)
@bot.message_handler(func=lambda message: message.text and bool(re.search(r'\bسلام\b', message.text)))
def send_welcome(message):
    bot.send_message(message.chat.id, "سلام، خوبین ؟\nبه مشهد استار خوش اومدی 💫\nامیدوارم حال دلت خوب باشه 💞", reply_to_message_id=message.message_id)

# پاسخ به خداحافظ، خدافظ یا بای (فقط کلمات کامل)
@bot.message_handler(func=lambda message: message.text and bool(re.search(r'\b(خداحافظ|خدافظ|بای)\b', message.text)))
def send_goodbye(message):
    bot.send_message(message.chat.id, "چه زود داری میری 🥺", reply_to_message_id=message.message_id)

# پاسخ به لف یا لفت (فقط کلمات کامل)
@bot.message_handler(func=lambda message: message.text and bool(re.search(r'\b(لف|لفت)\b', message.text)))
def send_left(message):
    bot.send_message(message.chat.id, "خیلی بدی کجا میری منو تنها میزاری؟ 💔", reply_to_message_id=message.message_id)

if __name__ == '__main__':
    keep_alive()
    bot.infinity_polling()
