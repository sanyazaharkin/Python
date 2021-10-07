import telebot

bot = telebot.TeleBot("2093362951:AAFuxsWHIXyzRWz9NTa1jHtfGTiyZ8xbsUU")






@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  print(message.text)
  if message.text == "Привет":
      answer = "Привет, твой id:" + str(message.from_user.id)
      bot.send_message(message.from_user.id, answer)
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Напиши Привет")
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


if __name__ == '__main__':
    bot.polling(none_stop=True)