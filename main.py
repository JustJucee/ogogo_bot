from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CommandHandler
)
from cred import TOKEN
from menu import main_menu_keyboard, course_menu_keyboard
from key_buttons import tele_button, back_menu, button

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Добро пожаловать, {update.effective_user.username}',
        reply_markup = main_menu_keyboard()
    )


def enroll(update: Update, context: CallbackContext):
    text = update.message.text
    if text[:6] == 'Запись':
        text = text + f'\nОтправитель: @{update.effective_chat.id}'
        context.bot.send_message(
            chat_id = '@helloogogo',
            text=text
        )


def how_to_enroll(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgEAAxkBAAEH2rlj9hLIgqapb6bd0HI6xfi8WsqX6AACVTMAAtpxZgdUSKRTBteYgS4E'
    )
    update.message.reply_text(
        text='''
1. Напишите сообщение с "Запись:" и ваше имя
2. Ваш номер
3. Выберите расписание
Мы вам перезвоним позже
        '''
    )


def resive_course_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите курс',
        reply_markup = course_menu_keyboard()
    )


def back(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Назад',
        reply_markup = main_menu_keyboard()
    )


def resive_location(update: Update, context: CallbackContext):        
    context.bot.send_sticker(                                          #update и context - одно и то же
        chat_id = update.effective_chat.id,                            #для update используем reply, а для context - send
        sticker = 'CAACAgEAAxkBAAEH2rlj9hLIgqapb6bd0HI6xfi8WsqX6AACVTMAAtpxZgdUSKRTBteYgS4E'
    )
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Location of OGOGO'
    )
    update.message.reply_location(
        longitude=74.619994732974,
        latitude=42.8736327866835,
        reply_to_message_id=msg.message_id
    )


def resive_info(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''Добро Пожаловать в OGOGO Академию! 
У нас вы сможете обучиться с самыми крутыми менторами и открыть для себя двери в программирование'''
    )
    context.bot.send_video(
        update.effective_chat.id,
        video = open('videos/ogogo.mp4', 'rb')
    )


def python_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Mentor', callback_data='python_mentor'),
            InlineKeyboardButton('Lesson', callback_data='python_lesson')
        ],
        [InlineKeyboardButton('Price', callback_data='python_Price')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup = reply_markup
    )

def javascript_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Mentor', callback_data='js_mentor'),
            InlineKeyboardButton('Lesson', callback_data='js_lesson')
        ],
        [InlineKeyboardButton('Price', callback_data='js_Price')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup = reply_markup
    )

def uxui_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Mentor', callback_data='uxui_mentor'),
            InlineKeyboardButton('Lesson', callback_data='uxui_lesson')
        ],
        [InlineKeyboardButton('Price', callback_data='uxui_Price')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup = reply_markup
    )


def inline_button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'python_mentor':
        context.bot.send_photo(
            update.effective_chat.id,
            photo = open('images/python_mentor.jpeg', 'rb')
        )
    if query.data == 'python_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
Расписание:
sdgethbvsergheyjnewrhwert
            '''
        )
    if query.data == 'python_Price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
Цена - 16000 сом в месяц.
            '''
        )
    if query.data == 'js_mentor':
        context.bot.send_photo(
            update.effective_chat.id,
            photo = open('images/javascript_mentor.jpeg', 'rb')
        )
    if query.data == 'js_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
Расписание:
sdgethbvsergheyj
            '''
        )
    if query.data == 'js_Price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
Цена - 16000 сом в месяц.
            '''
        )
    if query.data == 'uxui_mentor':
        context.bot.send_photo(
            update.effective_chat.id,
            photo = open('images/uxui_mentor.jpeg', 'rb')
        )
    if query.data == 'uxui_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
Расписание:
sdgethbvsergheyj
            '''
        )
    if query.data == 'uxui_Price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
Цена - 8000 сом в месяц.
            '''
        )


INFO = tele_button[0]
COURSE = tele_button[1]
LOCATION = tele_button[2]
ENROLL = tele_button[3]
BACK = back_menu[0]
PYTHON = button[0]
JS = button[1]
UXUI = button[2]

updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE),
    resive_course_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(INFO),
    resive_info
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATION),
    resive_location
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    back
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    javascript_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(UXUI),
    uxui_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ENROLL),
    how_to_enroll
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    enroll
))

updater.dispatcher.add_handler(CallbackQueryHandler(inline_button))
updater.start_polling()
updater.idle()                                          #Работает как file.close()