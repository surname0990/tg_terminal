from subprocess import check_output
import telebot
from telebot import types
import time

bot = telebot.TeleBot("")
user_id = "", ""

@bot.message_handler(content_types=["text"])
def main(message):
    for id in user_id:
        if id == message.chat.id: 
            comand = message.text  
            markup = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text="Повторить", callback_data=comand)
            markup.add(button) 
            try:
                bot.send_message(user_id, check_output(comand, shell = True,  reply_markup = markup)) 
            except:
                bot.send_message(user_id, "Invalid input") 
        else:
            bot.send_message(user_id, "Не пущу")
            

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
  comand = call.data 
  try:
     markup = types.InlineKeyboardMarkup() 
     button = types.InlineKeyboardButton(text="Повторить", callback_data=comand) 
     markup.add(button)
     bot.send_message(user_id, check_output(comand, shell = True), reply_markup = markup) 
  except:
     bot.send_message(user_id, "Invalid input") 

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            bot.send_message(user_id, "Упал")
            time.sleep(3)