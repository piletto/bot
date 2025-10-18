import telebot
import os
import random

bot = telebot.TeleBot('8278808585:AAFF6_-QISvPoeu60lcQfbHnIdfOVfnVeec')

files = ['cat1.jpg', 'cat2.jpg', 'cat3.jpg', 'dog1.jpg', 'dog2.jpg', 'dog3.jpg']
rarity = [3, 2, 1, 3, 2, 1]  

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! /mem - случайный мем")

@bot.message_handler(commands=['mem'])
def send_mem(message):

    all_files = []
    for i in range(len(files)):
        for j in range(rarity[i]):
            all_files.append(files[i])
    
    img_name = random.choice(all_files)

    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

bot.polling()
