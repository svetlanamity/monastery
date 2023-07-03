import telebot
from telebot import types
import os

API_TOKEN = os.environ['API_TOKEN']

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
        bot.reply_to(message, """\
Hello! This is a bot made by Sveta. You are adorable today ♥ \
""")

@bot.message_handler(commands = ['switch'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    # switch_button = types.InlineKeyboardButton(text = 'Получить комплимент', switch_inline_query="Telegram")
    switch_button = types.InlineKeyboardButton(text='Получить комплимент', callback_data='button_idk')
    markup.add(switch_button)
    bot.send_message(
        message.chat.id,
        "По кнопке ниже можно перейти в мой бот",
        reply_markup = markup)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Вы сказали: " + message.text)


user_dicts = {}


@bot.callback_query_handler(func=lambda message: message.data == "button_idk")
def button_1(message):
    if not user_dicts.get(message.from_user.id):
        user_dicts[message.from_user.id] = 1
    else:
        user_dicts[message.from_user.id] += 1

    bot.send_message(
        message.from_user.id,
        f"Кнопка нажата {user_dicts[message.from_user.id]} раз.")




bot.infinity_polling()