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
    if tg_answers.is_user_in_main_db(user_id):
        tg_answers.clean_user(user_id)
        tgbot.send_message(message.chat.id, tg_answers.answ('user_cleared').format(
            message.from_user, tgbot.get_me()), parse_mode='html')
    else:
        if not tg_answers.is_user_in_auth_tg(user_id):
            tg_answers.create_user(user_id)
        tgbot.send_message(message.chat.id, tg_answers.answ('greetings').format(
            message.from_user, tgbot.get_me()), parse_mode='html')
        tgbot.send_message(message.chat.id, tg_answers.answ('login').format(
            message.from_user, tgbot.get_me()), parse_mode='html')


@tgbot.message_handler(commands=['flights'])
def test(message):
    user_id = message.from_user.id
    if tg_answers.is_user_in_main_db(user_id):
        tgbot.send_message(message.chat.id,
                           tg_answers.get_flights(user_id).format(
                               message.from_user, tgbot.get_me()), parse_mode='html')


@tgbot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    if not tg_answers.user_phase(user_id):
        tgbot.send_message(message.chat.id,
                           tg_answers.try_auth(user_id, message.text).format(
                               message.from_user, tgbot.get_me()), parse_mode='html')
    else:
        pass


def main():
    tgbot.polling(none_stop=True)


if __name__ == '__main__':
    main()
