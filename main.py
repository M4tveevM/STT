# Please, work!
import time as t


def main():
    for i in range(10):
        try:
            import tg_bot
            tg_bot.tgbot.polling(none_stop=True)
        except Exception as ex:
            print(f'Attention: There is a problem: \n {ex}')
            t.sleep(1)
    print(f'Program has crashed')



if __name__ == '__main__':
    main()
