import telebot
from config import TOKEN
import random


bot = telebot.TeleBot(TOKEN)


def compress(text1):

    count = 1
    text2 = ''

    for i in range(len(text1)-1):
        if text1[i] == text1[i+1]:
            if i != len(text1)-2:
                count += 1
            else:
                count += 1
                text2 += str(count) + text1[i]
                break
        
        else:
            if count == 1:
                text2 += text1[i]
            else:
                text2 += str(count) + text1[i]
            count = 1

            if i == len(text1)-2:
                text2 += text1[i+1]

    return text2

def decompress(text1):

    text2 = ''
    count = 0
    i = 0

    while i < len(text1)-1:
        if text1[i].isdigit():
            count = int(text1[i])
            text2 += text1[i+1] * count
            i += 2

        else:
            text2 += text1[i]
            i += 1
            if i == len(text1)-1:
                text2 += text1[i]

    return text2

kosti = ['☠', '☠☠', '☠☠☠', '☠☠☠☠', '☠☠☠☠☠', '☠☠☠☠☠☠']


"""Команда СТАРТ"""


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Случайное число')
    item2 = telebot.types.KeyboardButton('Кинуть кость')
    item3 = telebot.types.KeyboardButton('Кодироват текст')
    item4 = telebot.types.KeyboardButton('Декодировать текст')
    item5 = telebot.types.KeyboardButton('Калькулятор')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный пункт меню: ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, как дела?')
    elif message.text == 'Случайное число':
        bot.send_message(message.chat.id, str(random.randint(0, 100)))
    elif message.text == 'Кинуть кость':
        bot.send_message(message.chat.id, kosti[(random.randint(0, 5))])


    elif message.text == 'Кодироват текст':
        bot.send_message(message.chat.id, 'Введите текст для кодироки в формате kod*<текст>')
    elif message.text[0:4] == 'kod*':
        bot.send_message(message.chat.id, f'Закодированный текст: {compress(message.text[4:])}')


    elif message.text == 'Декодировать текст':
        bot.send_message(message.chat.id, 'Введите текст для декодироки в формате dekod*<текст>')
    elif message.text[0:6] == 'dekod*':
        bot.send_message(message.chat.id, f'Декодированный текст: {decompress(message.text[6:])}')

    elif message.text == 'Калькулятор':
        bot.send_message(message.chat.id, 'Введите текст для калькулятора в формате calc*(2+3)/4')
    elif message.text[0:5] == 'calc*':
        bot.send_message(message.chat.id, f'Ответ: {str(eval(message.text[5:]))}')

    else:
        bot.send_message(message.chat.id, 'Этот функционал находится в разработке')


bot.polling(none_stop=True)
