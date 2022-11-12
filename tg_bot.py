# <imports>
import telebot  # Library that allows to control telegram bot

# tg config files
import tg_const  # file with constants
import tg_answers  # answers for user's questions

telebot.apihelper.ENABLE_MIDDLEWARE = True
telebot.apihelper.SESSION_TIME_TO_LIVE = 5 * 60
tgbot = telebot.TeleBot(tg_const.TOKEN)


@tgbot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.from_user.id
    tg_answers.check_userdata(user_id)
    tgbot.send_message(message.chat.id, tg_answers.answ('greetings',
                                                        tg_answers.check_userdata(
                                                            user_id, 'get_lang')).format(
        message.from_user, tgbot.get_me()), parse_mode='html')


@tgbot.message_handler(commands=['admin'])
def test(message):
    user_id = message.from_user.id
    tg_answers.check_userdata(user_id, task='change_lang')
    tgbot.send_message(message.chat.id,
                       "Your language has been chanhed".format(message.from_user,
                                                               tgbot.get_me()),
                       parse_mode='html')


@tgbot.message_handler(content_types=['text'])
def text(message):
    pass

# # looping tgBot
