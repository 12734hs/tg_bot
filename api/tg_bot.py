import telebot
from api import *

bot = telebot.TeleBot('8587387706:AAFp-xuZJaUXTiUDLfcv7sKr9UyzrvsYbms')

@bot.message_handler(commands=["start"])
def print(message):
    bot.reply_to(message, "Hi, please write /info for getting name of person")

@bot.message_handler(commands=["info"])
def print_name(message):
    bot.reply_to(message, name_surname)
    bot.reply_to(message, scores)
    bot.reply_to(message, print_events())

@bot.message_handler(func=lambda message: True)
def answer_on_their_questions(message):
    bot.reply_to(message, "Please, write command /info for getting information about the person")

bot.infinity_polling()
