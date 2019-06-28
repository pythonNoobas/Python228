import telebot

bot = telebot.TeleBot("879497357:AAHxUAZR2ZMy7q1dsC12NoFOmvBnKo9a3FA")

@bot.message_handler(content_types=['text'])
def echo_all(message):
	bot.send_message(message.chat.id, message.text)


bot.polling( none_stop = True )