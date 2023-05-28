from subprocess import check_output
import telebot
from telebot import types
import time

bot = telebot.TeleBot("5876606347:AAEgiavRHbgSZsmXPtreJFH9mAWK_QMilMo")
user_id = 799654981, 332773833, 1285502212

@bot.message_handler(content_types=["text"])
def main(message):
    for id in user_id:
        if id == message.chat.id: 
            comand = message.text  
            markup = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text="Повторить", callback_data=comand) #создаем кнопку
            markup.add(button) 
            try:
                bot.send_message(user_id, check_output(comand, shell = True,  reply_markup = markup)) #вызываем команду и отправляем сообщение с результатом
            except:
                bot.send_message(user_id, "Invalid input") 
        else:
            bot.send_message(user_id, "Не пущу")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
  comand = call.data 
  try:
     markup = types.InlineKeyboardMarkup() 
     button = types.InlineKeyboardButton(text="Повторить", callback_data=comand) #создаем кнопку и в data передаём команду
     markup.add(button)
     bot.send_message(user_id, check_output(comand, shell = True), reply_markup = markup) #вызываем команду и отправляем сообщение с результатом
  except:
     bot.send_message(user_id, "Invalid input") 

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            bot.send_message(user_id, "Упал")
            time.sleep(3)