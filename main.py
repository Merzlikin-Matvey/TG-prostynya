import telebot
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, "Привет! Я твой бот-помощник.", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Создать файл':
        pass
        # !TODO Создать отдельный файл с функцией обработки "Создать файл"
    elif message.text == 'Начать игру':
        pass
        # !TODO Создать отдельный файл с функцией обработки "Начать игру"


if __name__ == "__main__":
    bot.polling(none_stop=True)
