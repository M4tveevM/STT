# <imports>
import telebot
import tg_const # constants & config file
import tg_answers # answers for user's questions

# from questions import *
# from tgconfig import *


telebot.apihelper.ENABLE_MIDDLEWARE = True
telebot.apihelper.SESSION_TIME_TO_LIVE = 5 * 60
tgbot = telebot.TeleBot(tg_const.TOKEN)


@tgbot.message_handler(commands=['start'])

def welcome(message):
    user_id = message.chat.id
    tgbot.send_message(message.chat.id, (tg_answers.answ('greetings', 'en')).format(message.from_user, tgbot.get_me()),
                       parse_mode='html')


@tgbot.message_handler(commands=['admin'])
def test(message):
    pass


@tgbot.message_handler(content_types=['text'])
def text(message):
    pass


# # looping tgBot
# while True:
#     try:
#         tgbot.polling(none_stop=True)
#     except Exception as e:
#         t.sleep(15)

tgbot.polling(none_stop=True)
