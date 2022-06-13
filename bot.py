import config
import telebot
from pycbrf import ExchangeRates
from datetime import date

today = date.today()
rates = ExchangeRates(today)
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, "Привет! Я бот")
@bot.message_handler(commands=["help"])
def help(message):
	bot.send_message(message.chat.id, "Не чем не могу помочь")
@bot.message_handler(commands=["cny"])
def cny(message):
	text = "1 Юань ="+str(rates['CNY'].rate)+"руб."
	bot.send_message(message.chat.id, text)
@bot.message_handler(commands=["usd"])
def usd(message):
	text = "1 Доллар США ="+str(rates['USD'].rate)+"руб."
	bot.send_message(message.chat.id, text)
@bot.message_handler(commands=["eur"])
def eur(message):
	text = "1 евро ="+str(rates['EUR'].rate)+"руб."
	bot.send_message(message.chat.id, text)	
@bot.message_handler(commands=["czk"])
def czk(message):
	text = "1 Чешская крона ="+str(rates['CZK'].rate)+"руб."
	bot.send_message(message.chat.id, text)		
if __name__ == '__main__':
	bot.infinity_polling()