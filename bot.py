#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import telegram;
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter
import datetime
# Enable logging
import random as rand
import list_events as calen

global pollid
pollid = {}
global sched
sched = {'0': ['9:00-10:30 Adaptive and Array Signal Processing, LdV-Bau \n'
               '13:15-14:45 Sprachkurs, Ernst-Abbe-Zentrum (Lupa) \n'
               '15:00-16:30 Audio Coding, Kirchoffbau (2002B) \n'
               '16:45-18:15 Systems Optimization, Humboldtbau (211/212)\n',
               '13:00-14:30 Systems Optimization, Humboldtbau (211)\n'
               '15:00-16-30 Audio Coding, Humboldtbau (010)\n'
               '19:00-20:30 Adaptive and Array Signal Processing, LdV-Bau\n',
               '9:00-10:30 Measurements in Communications, Humboldtbau (012)\n'
               '13:00-14:30 Sprachkurs, Ernst-Abbe-Zentrum (Lupa)\n',
               '12:45-16:45 Cellular Communication Systems,  Humboldtbau (012) \n',
               '13:00-14:30 Adaptive and Array Signal Processing, Helmholtzbau (1520b)',
               'chill',
               'chill'],
         '1':['9:00-10:30 Adaptive and Array Signal Processing, LdV-Bau \n'
               '13:00-14:30 Sprachkurs \n'
               '15:00-16:30 Audio Coding, Kirchoffbau(2002B) \n'
               '16:45-18:15 Systems Optimization, Humboldtbau (211/212)\n',
               '13:00-14:30 Systems Optimization, Humboldtbau (211)\n'
               '19:00-20:30 Adaptive and Array Signal Processing, LdV-Bau\n',
               '9:00-10:30 Measurements in Communications, Humboldtbau (012)\n'
               '11:00-12:30 Measurements in Communications, Humboldtbau (010)\n'
               '13:00-14:30 Sprachkurs, Ernst-Abbe-Zentrum (Lupa)\n',
              '12:45-16:45 Cellular Communication Systems,  Humboldtbau (012) \n',
               'chill',
               'chill',
               'chill']}
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    updater.bot.sendSticker(update.message.chat.id, open('photo-2019-10-28-13-40-16.jpg','rb'))
    mess=updater.bot.sendPoll(update.message.chat.id, 'по пивку?',['да','нет'])
    pollid[mess.chat.id]=mess.message_id


def end(update,context):
    res = updater.bot.stop_poll(update.message.chat.id, pollid[update.message.chat.id])
    yes = res.options[0].voter_count
    no = res.options[1].voter_count
    if yes > no:
        updater.bot.send_message(update.message.chat.id, 'zbs')
    elif no>=yes :

        updater.bot.send_sticker(update.message.chat.id, open('photo-2019-10-29-21-37-37.jpg','rb'))

def answer(update, context):

    if str(update.message.from_user.id) == '341128154':
        updater.bot.send_message(update.message.chat.id, 'ну хуй знает, вов')
    elif str(update.message.from_user.id) == '629888988' and str(update.message.chat.id) == '-297571955':
        updater.bot.send_message(update.message.chat.id, 'ну хуй знает, зуфар')
    elif rand.random() > 0.49 and str(update.message.chat.id) == '-388998239':
        updater.bot.send_message(update.message.chat.id, 'ну хуй знает, ' + update.message.from_user.first_name)

def ansno(update, context):
    print(update.message.chat.id)
    updater.bot.send_sticker(update.message.chat.id, open('photo-2019-10-29-21-37-37.jpg','rb'))

def week(update, context):
    m=calen.week()
    updater.bot.send_message(update.message.chat.id, m)

def nextweek(update, context):
    m=calen.nextweek()
    updater.bot.send_message(update.message.chat.id, m)

def today(update, context):
    schedule = calen.today()
    updater.bot.send_message(update.message.chat.id, schedule)
    print(update.message.chat.id)
def tomorrow(update, context):
    schedule = calen.tomorrow()
    updater.bot.send_message(update.message.chat.id, schedule)
    print(update.message.chat.id)






class nche(BaseFilter):
    def filter(self, message):
        return message.text.lower() =='ну че'

class ans(BaseFilter):
    def filter(self, message):
        return len(message.text)>10 and '?' in message.text

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    global updater
    updater = Updater("1008787258:AAE9-_b4wQteEcPfnhBj__orVhf3JDBtGW8", use_context=True)

    nuche = nche()
    answ =ans()

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("nuche", start))
    dp.add_handler(CommandHandler("endpoll", end))
    dp.add_handler(MessageHandler(nuche, start))
    dp.add_handler(MessageHandler(answ, answer))
    dp.add_handler(CommandHandler("net", ansno))
    dp.add_handler(CommandHandler("today", today))
    dp.add_handler(CommandHandler("tomorrow", tomorrow))
    dp.add_handler(CommandHandler("week", week))
    dp.add_handler(CommandHandler("nextweek", nextweek))
    time.sleep(1)

    # log all errors
    # Start the Bot

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':

    main()


