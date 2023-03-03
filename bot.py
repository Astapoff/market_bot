import os
import telebot

from dotenv import load_dotenv 

load_dotenv()

secret_token = os.getenv('TOKEN')

bot = telebot.TeleBot(secret_token)


def is_valid(n):
    if n.isnumeric() and '.' not in n and ',' not in n:
        if int(n) >= 0:
            return True
    else:
        return False

def for_fool(message):
    bot.send_message(message.chat.id, 'Число должно быть: положительное, целое, без пробелов, букв и других символов.', parse_mode='html')
    return

@bot.message_handler(func=lambda message: message.text == "/start")
def start(message):
    global NAME
    NAME = message.from_user.first_name
    bot.send_message(message.chat.id, 'Привет, я всё посчитаю!', parse_mode='html')
    bot.send_message(message.chat.id, f'Сейчас я попрошу тебя сообщить некоторые вводные данные. '
                     f'Требуется ввести положительное, целое число, без пробелов и букв.',
                     parse_mode='html')
    bot.send_message(message.chat.id, 'Первое - введи размер бюджета на маркетинг: ', parse_mode='html')
    bot.register_next_step_handler(message, get_num1)

@bot.message_handler(content_types=['text'])
def get_num1(message):
    global num1
    num1 = message.text
    if message.text == '/start':
        start(message)
    else:
        if is_valid(num1):
            num1 = int(num1)
            bot.send_message(message.chat.id, f'Так, бюджет {num1} рублей. Теперь введи количество платных регистраций:', parse_mode='html')
            bot.register_next_step_handler(message, get_num2)
        else:
            for_fool(message)
            bot.register_next_step_handler(message, get_num1)

@bot.message_handler(content_types=['text'])
def get_num2(message):
    global num2
    num2 = message.text
    if message.text == '/start':
        start(message)
    else:
        if is_valid(num2):
            num2 = int(num2)
            bot.send_message(message.chat.id, f'Платных регистраций - {num2}. Теперь введи количество регистраций от партнеров:', parse_mode='html')
            bot.register_next_step_handler(message, get_num3)
        else:
            for_fool(message)
            bot.register_next_step_handler(message, get_num2)

@bot.message_handler(content_types=['text'])
def get_num3(message):
    global num3
    num3 = message.text
    if message.text == '/start':
        start(message)
    else:
        if is_valid(num3):
            num3 = int(num3)
            bot.send_message(message.chat.id, f'Регистраций от партнеров - {num3}. Теперь введи количество просмотров вебинара:', parse_mode='html')
            bot.register_next_step_handler(message, get_num4)
        else:
            for_fool(message)
            bot.register_next_step_handler(message, get_num3)

@bot.message_handler(content_types=['text'])
def get_num4(message):
    global num4
    num4 = message.text
    if message.text == '/start':
        start(message)
    else:
        if is_valid(num4):
            num4 = int(num4)
            bot.send_message(message.chat.id, f'Количество просмотров вебинара - {num4}. Теперь введи количество заявок:', parse_mode='html')
            bot.register_next_step_handler(message, get_num5)
        else:
            for_fool(message)
            bot.register_next_step_handler(message, get_num4)

@bot.message_handler(content_types=['text'])
def get_num5(message):
    global num5
    num5 = message.text
    if message.text == '/start':
        start(message)
    else:
        if is_valid(num5):
            num5 = int(num5)
            bot.send_message(message.chat.id, f'Количество заявок - {num5}. Теперь введи количество оплат:', parse_mode='html')
            bot.register_next_step_handler(message, get_num6)
        else:
            for_fool(message)
            bot.register_next_step_handler(message, get_num5)

@bot.message_handler(content_types=['text'])
def get_num6(message):
    global num6
    num6 = message.text
    if message.text == '/start':
        start(message)
    else:
        if is_valid(num6):
            num6 = int(num6)
            bot.send_message(message.chat.id, f'Количество оплат - {num6}. Теперь введи размер среднего чека:', parse_mode='html')
            bot.register_next_step_handler(message, get_num7_and_res)
        else:
            for_fool(message)
            bot.register_next_step_handler(message, get_num6)

def get_answer(result):
    res_dict = {
        'Рекламного бюджета: ': round(result[0]),
        'Регистраций: ': round(result[1]),
        'Просмотров вебинара: ': round(result[2]),
        'Заявок: ': round(result[3]),
        'Оплат: ': round(result[4]),
        'ВЫРУЧКИ: ': round(result[5]),
    }
    res_key = []
    res_value =[]
    for k, v in res_dict.items():
        if v > 0:
            res_key.append(k)
            res_value.append(v)
    s = 'НЕДОПОЛУЧЕНО\n'
    for i in range(len(res_value)):
        s += str(res_key[i])
        s += str(res_value[i])
        s += '\n'

    return s

@bot.message_handler(content_types=['text'])
def get_num7_and_res(message):
    global num7
    num7 = message.text
    if message.text == '/start':
        start(message)
    else:
        if is_valid(num7):
            num7 = int(num7)
            # bot.send_message(message.chat.id, f'Средний чек - {num7} руб.')
            result = get_result()
            bot.send_message(message.chat.id, get_answer(result))
            bot.send_message(message.chat.id,
                             f'Оставить заявку: https://norm-agency.ru/#contact\n'
                             f'Подписывайся на наш канал https://t.me/norm_agency',
                             parse_mode='html')
            bot.send_message(message.chat.id, f'Если хочешь начать сначала, введи /start', parse_mode='html')
        else:
            for_fool(message)
            bot.register_next_step_handler(message, get_num7_and_res)

@bot.message_handler(content_types=['text'])
def get_result():
    result = []
    res1 = (((num1 / num2) - 450) * num2)
    result.append(res1)
    res2 = (500 - num3)
    result.append(res2)
    res3 = ((num1 / 450 + 500) * 0.5 - num4)
    result.append(res3)
    res4 = ((num1 / 450 + 500) * 0.5 * 0.08 - num5)
    result.append(res4)
    res5 = ((num1 / 450 + 500) * 0.5 * 0.08 * 0.15 - num6)
    result.append(res5)
    res6 = (res5 * num7 - num6 * num7)
    result.append(res6)
    return result

bot.polling(non_stop=True)
