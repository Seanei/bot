#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import telegram;
import time
import pickle
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter
from telegram import Location
import datetime
# Enable logging
import random as rand
import list_events as calen
from random import randint
global pollid
pollid = {}

pickle.dump(datetime.datetime.today() - datetime.timedelta(days=5),open('dat.bin', 'wb'))
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
    if '?' in update.message.text.lower():
        if str(update.message.from_user.id) == '629888988' and str(update.message.chat.id) == '-297571955':
            updater.bot.send_message(update.message.chat.id, 'ну хуй знает, зуфар')
        elif (rand.random() > 0.9 and ((str(update.message.chat.id) == '-388998239' or str(update.message.chat.id) == '-318580374'or str(update.message.chat.id) == '-297571955'))) or str(update.message.from_user.id) == "384580876":
            updater.bot.send_message(update.message.chat.id, 'ну хуй знает, ' + update.message.from_user.first_name)
    elif len(update.message.text)>=30 and (str(update.message.chat.id)=='-388998239' or str(update.message.chat.id) == '-318580374'):
        date = datetime.datetime.today()
        date1 = pickle.load(open('dat.bin', 'rb'))
        if date-date1 >= datetime.timedelta(days=3) and rand.random() > 0.85:

            updater.bot.send_message(update.message.chat.id, 'ну такое себе')
            pickle.dump(date,open('dat.bin', 'wb'))



def ansno(update, context):
    updater.bot.send_sticker(update.message.chat.id, open('photo-2019-10-29-21-37-37.jpg','rb'))
def motiv(update, context):
    i = randint(1,2)
    updater.bot.send_video(update.message.chat.id, video=open('video'+str(i)+'.mp4', 'rb'))
def week(update, context):
    if str(update.message.chat.id) =='-297571955' or update.message.chat.id > 0:
        m=calen.week()
        updater.bot.send_message(update.message.chat.id, m)

def nextweek(update, context):
    if str(update.message.chat.id) =='-297571955' or update.message.chat.id > 0:
        m=calen.nextweek()
        updater.bot.send_message(update.message.chat.id, m)

def today(update, context):
    if str(update.message.chat.id) == '-297571955' or update.message.chat.id > 0:
        schedule = calen.today()
        updater.bot.send_message(update.message.chat.id, schedule)
def tomorrow(update, context):
    if str(update.message.chat.id) =='-297571955' or update.message.chat.id > 0:

        schedule = calen.tomorrow()
        updater.bot.send_message(update.message.chat.id, schedule)
def clear(update, context):
    pickle.dump(datetime.datetime.today() - datetime.timedelta(days=5), open('dat.bin', 'wb'))
    updater.bot.send_message(update.message.chat.id, 'ок')
#def loc(update,context):
    #coord = (float(update.message.location.latitude), float(update.message.location.longitude))

class nche(BaseFilter):
    def filter(self, message):
        return message.text.lower() =='ну че'

class ans(BaseFilter):
    def filter(self, message):

        return len(message.text)>10

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
    dp.add_handler(CommandHandler("motivation", motiv))
    dp.add_handler(MessageHandler(nuche, start))
    dp.add_handler(MessageHandler(answ, answer))
    dp.add_handler(CommandHandler("net", ansno))
    dp.add_handler(CommandHandler("today", today))
    dp.add_handler(CommandHandler("tomorrow", tomorrow))
    dp.add_handler(CommandHandler("week", week))
    dp.add_handler(CommandHandler("nextweek", nextweek))
    dp.add_handler(CommandHandler("clear", clear))
    #dp.add_handler(MessageHandler(Filters.location, loc))
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


