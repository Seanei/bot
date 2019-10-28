import telebot;
import time

bot = telebot.TeleBot('1008787258:AAE9-_b4wQteEcPfnhBj__orVhf3JDBtGW8');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "ну че":
        bot.send_sticker(message.chat.id, open('photo_2019-10-28_13-40-16.jpg','rb'));
        #bot.send_message(-388998239, 'бухием? /да')
        #time_to_drink = time.time()

bot.polling(none_stop=True, interval=0)
