import ollama
import asyncio
import telebot;
token = "7245668785:AAGuzceEEbNOBSXjrxeNSYSngoQF9tPQYhM"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет")
  print("meow")
def responsefunc(text, fromid):
    response = ollama.chat(model='command-r', messages=[
      {
        'role': 'user',
        'content': text,
      },
    ])
    bot.send_message(fromid, response['message']['content'])
    print(text, response['message']['content'])

@bot.message_handler(content_types='text')
def message_reply(message):
  if message.text == "debug":
    bot.send_message(message.from_user.id, "debug mode entered")
  else:
    responsefunc(message.text, message.from_user.id)
  
bot.infinity_polling()