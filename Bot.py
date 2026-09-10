import os
from flask import Flask
from threading import Thread
import telebot

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

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات شما با موفقیت روشن شد و آماده به کار است. 🎉")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "پیام شما دریافت شد: " + message.text)

if __name__ == '__main__':
    keep_alive()
    bot.infinity_polling()
