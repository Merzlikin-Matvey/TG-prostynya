import telebot
from dotenv import load_dotenv
import os


# Загрузка бота
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Запуск
@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, "Привет! Я твой бот-помощник.", reply_markup=markup)


# Обработка входящих команд
@bot.message_handler(func=lambda message: message.text == "Создать файл")
def create_file_handler(message):
    def get_num(message, user_data):
        user_data['num'] = message.text
        bot.send_message(message.from_user.id, 'Введите количество задач')
        bot.register_next_step_handler(message, get_num, user_data)

    def get_size(message, user_data):
        user_data['size'] = message.text
        bot.send_message(message.from_user.id, 'Введите длину чисел')
        bot.register_next_step_handler(message, get_size, user_data)

    def get_title(message, user_data):
        user_data['title'] = message.text
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_title, user_data)

    def get_file_name(message, user_data):
        user_data['fileName'] = message.text


    user_data = {}  # словарь для хранения данных пользователя
    bot.send_message(message.from_user.id, "Как тебя зовут?")
    bot.register_next_step_handler(message, get_file_name, user_data)  # передаем user_data в первую функцию




if __name__ == "__main__":
    bot.polling(none_stop=True)
