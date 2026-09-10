import os
from flask import Flask
import telebot

TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Bot is active!"

# پاسخ به دستور start/
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "سلام خوبی\nبه مشهد استار خوش اومدی امیدوارم حال دلت خوب باشه"
    bot.reply_to(message, welcome_text)

# حساسیت به کلمه سلام در متن پیام‌ها
@bot.message_handler(func=lambda message: 'سلام' in message.text.lower())
def handle_hello(message):
    reply_text = "سلام خوبی\nبه مشهد استار خوش اومدی امیدوارم حال دلت خوب باشه"
    bot.reply_to(message, reply_text)

# پاسخ به بقیه پیام‌ها
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    import threading
    t = threading.Thread(target=run_flask)
    t.start()
    bot.infinity_polling()
