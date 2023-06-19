import telebot
from config2 import token#из файла импортируем токен бота
from telebot import types#для работы с кнопками
import emoji
from emoji import emojize#для работы с эмоджи

bot = telebot.TeleBot(token)#создаем экземпляр бота


@bot.message_handler(commands=["start"])#создаем функцию, которая будет начинать работу бота
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)#создаем клавиатуру
    keyboard = types.KeyboardButton(text='да')#кнопка
    keyboard2 = types.KeyboardButton(text='нет')#кнопка
    markup.add(keyboard, keyboard2)
    bot.send_message(chat_id, f'Привет!, {first_name}, узнаем насколько ты знаешь страны?'+ emoji.emojize('\U0001F30F') , reply_markup=markup)


@bot.message_handler(content_types=['text'])#получение сообщений от пользователя
def text(message):
    chat_id = message.chat.id

    if message.chat.type == 'private':
        if message.text.lower() == 'да':
            bot.send_message(chat_id, 'Отлично! Начинаем!'+ emoji.emojize('\U0001F609'))
            bot.send_message(chat_id, 'Какая это страна?')
            inline_markup = telebot.types.InlineKeyboardMarkup()
            inline_keyboard = types.InlineKeyboardButton('Египет' + emoji.emojize('\U0001F1EA\U0001F1F8'), callback_data='1')
            inline_keyboard2 = types.InlineKeyboardButton('Тунис'+ emoji.emojize('\U0001F1F9\U0001F1F3'), callback_data='2')
            inline_markup.row(inline_keyboard, inline_keyboard2)
            bot.send_photo(message.chat.id,
                           photo="https://funart.pro/uploads/posts/2019-11/1573817984_piramidy-v-gize-egipet-50.jpg",
                           reply_markup=inline_markup)

        elif message.text.lower() == 'нет':
            bot.send_message(chat_id, 'Жаль,пока!')


@bot.message_handler(content_types=["text"])
def text_2(message):
    chat_id_2 = message.chat.id
    if message.chat.type == 'private':
        if message.text.lower() == 'да':
            inline_markup = telebot.types.InlineKeyboardMarkup()
            inline_keyboard_3 = types.InlineKeyboardButton('Испания'+ emoji.emojize('\U0001F1EA\U0001F1F8'), callback_data='3')
            inline_keyboard_4 = types.InlineKeyboardButton('Франция'+ emoji.emojize('\U0001F1EB\U0001F1F7'), callback_data='4')
            inline_markup.row(inline_keyboard_3, inline_keyboard_4)
            bot.send_photo(message.chat.id,
                    photo="http://voltagerider.com/wp-content/uploads/2020/05/electric_scooter_types.jpg",
                    reply_markup=inline_markup)

        elif message.text.lower() == 'нет':
            bot.send_message(chat_id_2, 'Жаль,пока!')


@bot.callback_query_handler(func=lambda callback: callback.data)#функция,которая обрабатывает нажатие на инлайн кнопки
def chek_callback_data(callback):
    if callback.data in ('1'):
        bot.send_message(callback.message.chat.id, 'Все верно!')
        bot.send_message(callback.message.chat.id,
                         'Интересный факт: Египетские пирамиды — каменные сооружения, используемые древними царями '
                         'как усыпальницы, храмы и казнохранилища. '
                         'Сохранилось 118 пирамид, которые расположены у берегов реки Нил, на севере Египта.')
        msg = bot.send_message(callback.message.chat.id, 'Продолжим?')
        bot.register_next_step_handler(msg, text_2)#указываем порядок отправки
    elif callback.data == '2':
        bot.send_message(callback.message.chat.id, 'Не верно(')
        msg = bot.send_message(callback.message.chat.id, 'Продолжим?')
        bot.register_next_step_handler(msg, text_2)

    if callback.data in ('4'):
        bot.send_message(callback.message.chat.id, 'Умничка!')
        bot.send_message(callback.message.chat.id,
                     'Интересный факт: Эта страна - лидер по посещаемости.'
                     'Каждый год количество туристов превышает население страны')
        msg = bot.send_message(callback.message.chat.id, 'Еще?')
        bot.register_next_step_handler(msg, text_3)
    elif callback.data == '3':
        bot.send_message(callback.message.chat.id, 'Не верно( ')
        msg = bot.send_message(callback.message.chat.id, 'Еще?')
        bot.register_next_step_handler(msg, text_3)

    if callback.data in ('5'):
        bot.send_message(callback.message.chat.id, 'Молодец!')
        bot.send_message(callback.message.chat.id,
                     'На территории Италии расположены два '
                     'мини-государства - Сан-Марино и Ватикан.')
        msg = bot.send_message(callback.message.chat.id, 'Идем дальше?')
        bot.register_next_step_handler(msg, text_4)
    elif callback.data == '6':
        bot.send_message(callback.message.chat.id, 'Не верно( ')
        msg = bot.send_message(callback.message.chat.id, 'Идем дальше?')
        bot.register_next_step_handler(msg, text_4)

    if callback.data in ('7'):
        bot.send_message(callback.message.chat.id, 'Так держать!')
        bot.send_message(callback.message.chat.id,
                     'Россия – самая большая страна мира, '
                     'её площадь 17 075 400 квадратных километров. '
                     'Она больше США в 1,8 раз. Площадь России приблизительно'
                     'равна площади поверхности планеты Плутон.')
        msg = bot.send_message(callback.message.chat.id, 'Еще?')
        bot.register_next_step_handler(msg, text_5)
    elif callback.data == '8':
        bot.send_message(callback.message.chat.id, 'Не верно( ')
        msg = bot.send_message(callback.message.chat.id, 'Еще?')
        bot.register_next_step_handler(msg, text_5)

    if callback.data in ('9'):
        bot.send_message(callback.message.chat.id, 'Отлично!')
        bot.send_message(callback.message.chat.id,
                     'Беларусь занимает 13-ое место в Европе '
                     'по площади и 17-ое место по численности населения.'
                     'Уровень грамотности, по оценкам ЮНЕСКО, составляет 99,7%. '
                     'Этот показатель не только один из самых высоких в Европе,'
                     ' но и является одним из лучших показателей мира')
        msg = bot.send_message(callback.message.chat.id, 'Это все мои вопросы для тебя'+ emoji.emojize('\U0000263A') )
    elif callback.data == '10':
        bot.send_message(callback.message.chat.id, 'Не верно( ')
        msg = bot.send_message(callback.message.chat.id, 'Это все мои вопросы для тебя'+ emoji.emojize('\U0000263A'))


@bot.message_handler(content_types=["text"])
def text_3(message):
    chat_id_3 = message.chat.id
    if message.chat.type == 'private':
        if message.text.lower() == 'да':
            inline_markup = telebot.types.InlineKeyboardMarkup()
            inline_keyboard5 = types.InlineKeyboardButton('Италия'+ emoji.emojize('\U0001F1EE\U0001F1F9'), callback_data='5')
            inline_keyboard6 = types.InlineKeyboardButton('Испания'+ emoji.emojize('\U0001F1EA\U0001F1F8'), callback_data='6')
            inline_markup.row(inline_keyboard5, inline_keyboard6)
            bot.send_photo(message.chat.id,
                       photo="http://topmesta.ru/wp-content/uploads/dostoprimechatelnosti-italii-1.jpg",
                       reply_markup=inline_markup)
        elif message.text.lower() == 'нет':
            bot.send_message(chat_id_3, 'Жаль,пока!')

@bot.message_handler(content_types=["text"])
def text_4(message):
    chat_id_4 = message.chat.id
    if message.chat.type == 'private':
        if message.text.lower() == 'да':
            inline_markup = telebot.types.InlineKeyboardMarkup()
            inline_keyboard7 = types.InlineKeyboardButton('Россия'+ emoji.emojize('\U0001F1F7\U0001F1FA'), callback_data='7')
            inline_keyboard8 = types.InlineKeyboardButton('Сербия'+ emoji.emojize('\U0001F1F7\U0001F1F8'), callback_data='8')
            inline_markup.row(inline_keyboard7, inline_keyboard8)
            bot.send_photo(message.chat.id,
                       photo="https://photoclub.by/images/main99/991919_main.jpg",
                       reply_markup=inline_markup)
        elif message.text.lower() == 'нет':
            bot.send_message(chat_id_4, 'Жаль,пока!')

@bot.message_handler(content_types=["text"])
def text_5(message):
    chat_id_5 = message.chat.id
    if message.chat.type == 'private':
        if message.text.lower() == 'да':
            inline_markup = telebot.types.InlineKeyboardMarkup()
            inline_keyboard9 = types.InlineKeyboardButton('Беларусь'+ emoji.emojize('\U0001F1E7\U0001F1FE'), callback_data='9')
            inline_keyboard10 = types.InlineKeyboardButton('Швеция'+ emoji.emojize('\U0001F1F8\U0001F1EA'), callback_data='10')
            inline_markup.row(inline_keyboard9, inline_keyboard10)
            bot.send_photo(message.chat.id,
                       photo="http://nlb.by/upload/iblock/543/543865144e7c21746ca8cafb916aa710.jpg",
                       reply_markup=inline_markup)
        elif message.text.lower() == 'нет':
            bot.send_message(chat_id_5, 'Жаль,пока!')

bot.polling(none_stop=True, interval=0)#запускаем бот