import teleKeys
import telebot
from telebot import types


bot = telebot.TeleBot(teleKeys.key)


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Наш веб-сайт')
        btn2 = types.KeyboardButton('Наши новости')
        btn3 = types.KeyboardButton('О нас')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Нажмите на одну из понравившихся кнопок',
                         reply_markup=markup)  # ответ бота

    elif message.text == 'Наш веб-сайт':
        bot.send_message(message.from_user.id, 'Вы можете получить полезную информацию на нашем веб-сайте.\n \nПолный текст можно прочитать по ' +
                         '[ссылке](https://majotrade.net/)', parse_mode='Markdown')

    elif message.text == 'Наши новости':
        bot.send_message(message.from_user.id, 'В настоящий момент идёт разработка робота для торговли фьючерсами Binance ' +
                         '[ссылка](https://github.com/MajotraderLucky/PythonMarketsRobots/blob/main/longAndShortBot.py)', parse_mode='Markdown')

    elif message.text == 'О нас':
        bot.send_message(message.from_user.id, 'Чтобы узнать об авторе канала - нажмите на ' +
                         '[ссылку](https://majotrade.net/sample-page/)', parse_mode='Markdown')


print(f"Bot is running")

bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
