import telebot
from config import TOKEN
import random


bot = telebot.TeleBot(TOKEN)


def compress(mess):

    text1 = mess.text
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

    bot.send_message(mess.chat.id, f'Результат: {text2}')

def decompress(mess):

    text1 = mess.text
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

    bot.send_message(mess.chat.id, f'Результат: {text2}')

def calculator(mess):
    bot.send_message(mess.chat.id, f'Результат: {str(eval(mess.text))}')

def zodiac_signs(mess):

    with open('zodiac.txt', 'r', encoding='utf-8') as file:
        text = file.read().splitlines()

    for i in text:
        if mess == i.split('*/')[0]:
            result = i.split('*/')[1]
            break
    
    return result

def guess(mess):
    text1 = mess.text
    rand = random.randint(1, 5)
    if text1 == str(rand):
        text2 = 'Ура! Вы угадали число 👍'
    else:
        text2 = f'Акела промахнулся 🤦\nПравильное число: {rand}'

    bot.send_message(mess.chat.id, text2)

def throw_kosti2(mess):

    kosti2 = ['🦴', '🦴🦴', '🦴🦴🦴', '🦴🦴🦴🦴', '🦴🦴🦴🦴🦴', '🦴🦴🦴🦴🦴🦴']

    if mess == 'Одну':
        result = kosti2[(random.randint(0, 5))]
    elif mess == 'Две':
        result = f'{kosti2[(random.randint(0, 5))]} ∣ {kosti2[(random.randint(0, 5))]}'
    return result

"""Команда СТАРТ"""

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Как дела?')
    item2 = telebot.types.KeyboardButton('Кинуть кость')
    item3 = telebot.types.KeyboardButton('Угадай число')
    item4 = telebot.types.KeyboardButton('Калькулятор')
    item5 = telebot.types.KeyboardButton('Кодировка')
    item6 = telebot.types.KeyboardButton('Декодировка')
    item7 = telebot.types.KeyboardButton('Случайное число (0-100)')
    item8 = telebot.types.KeyboardButton('Знак зодиака')

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный пункт меню', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет 😉')

    elif message.text == 'Как дела?':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('He очень', callback_data='He очень')
        item2 = telebot.types.InlineKeyboardButton('Супер', callback_data='Супер')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Отлично, a y вас?', reply_markup=markup)

    elif message.text == 'Случайное число (0-100)':
        bot.send_message(message.chat.id, str(random.randint(0, 100)))

    elif message.text == 'Кинуть кость':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('Одну', callback_data='Одну')
        item2 = telebot.types.InlineKeyboardButton('Две', callback_data='Две')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Сколько костей кунуть?', reply_markup=markup)

    elif message.text == 'Кодировка':
        text = bot.send_message(message.chat.id, 'Введите текст для кодировки')
        bot.register_next_step_handler(text, compress)

    elif message.text == 'Декодировка':
        text = bot.send_message(message.chat.id, 'Введите текст для декодировки')
        bot.register_next_step_handler(text, decompress)

    elif message.text == 'Калькулятор':
        text = bot.send_message(message.chat.id, 'Введите текст для калькулятора, например: (2+3)/((5-1)*1)')
        bot.register_next_step_handler(text, calculator)

    elif message.text == 'Знак зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')
        item2 = telebot.types.InlineKeyboardButton('Телец', callback_data='Телец')
        item3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='Близнецы')
        item4 = telebot.types.InlineKeyboardButton('Рак', callback_data='Рак')
        item5 = telebot.types.InlineKeyboardButton('Лев', callback_data='Лев')
        item6 = telebot.types.InlineKeyboardButton('Дева', callback_data='Дева')
        item7 = telebot.types.InlineKeyboardButton('Весы', callback_data='Весы')
        item8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='Скорпион')
        item9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='Стрелец')
        item10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='Козерог')
        item11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='Водолей')
        item12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='Рыбы')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        bot.send_message(message.chat.id, 'Выберите знак зодиака', reply_markup=markup)

    elif message.text == 'Угадай число':
        text = bot.send_message(message.chat.id, 'Введите число от 1 до 5')
        bot.register_next_step_handler(text, guess)

    else:
        bot.send_message(message.chat.id, 'Этот функционал находится в разработке ☝')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHAQZjqK3EnNHMTLYG16keCV6k93qfWAACEgADwDZPEzO8ngEulQc3LAQ')
        

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'He очень':
        bot.send_message(call.message.chat.id, 'Держись, всё наладится 💪')
    elif call.data == 'Супер':
        bot.send_message(call.message.chat.id, 'Так держать, отличный настрой 😎')
    elif call.data == 'Овен':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Телец':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Близнецы':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Рак':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Лев':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Дева':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Весы':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Скорпион':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Стрелец':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Козерог':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Водолей':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Рыбы':
        bot.send_message(call.message.chat.id, f'{call.data}:\n{zodiac_signs(call.data)}')
    elif call.data == 'Одну':
        bot.send_message(call.message.chat.id, f'{throw_kosti2(call.data)}')
    elif call.data == 'Две':
        bot.send_message(call.message.chat.id, f'{throw_kosti2(call.data)}')


bot.polling(none_stop=True)
