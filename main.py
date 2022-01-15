import telebot
from telebot import types
import random
import requests

socks4 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt").text
socks5 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt").text
http = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt").text

http = http.split()
socks5 = socks5.split()
socks4 = socks4.split()

bot = telebot.TeleBot('5046157281:AAH8sSGxFks6nVVypLyGNpmGLs2W8msSuZA')

@bot.message_handler(commands=['start'])
def start(message):
	keyboard = types.InlineKeyboardMarkup()
	http = types.InlineKeyboardButton(text='HTTP', callback_data='HTTP')
	socks5 = types.InlineKeyboardButton(text='SOCKS5', callback_data='SOCKS5')
	socks4 = types.InlineKeyboardButton(text='SOCKS4', callback_data='SOCKS4')
	keyboard.add(http, socks5, socks4)
	bot.send_message(message.chat.id, f"Здравствуйте, {message.chat.first_name}. Я - FoxyProxy, бот который выдает прокси бесплатно. Прокси обновляются каждые 15 минут. Какого типа вам нужен прокси?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda c:True)
def send_proxy(c):
	if c.data == "HTTP":
		proxy_choice = random.randrange(0, len(http))
		bot.send_message(c.message.chat.id, f'Тип прокси: {c.data}.\nПрокси: {http[proxy_choice]}\nЕсли понадоблюсь снова, напишите /start.')
	if c.data == "SOCKS5":
		proxy_choice = random.randrange(0, len(socks5))
		bot.send_message(c.message.chat.id, f'Тип прокси: {c.data}.\nПрокси: {socks5[proxy_choice]}\nЕсли понадоблюсь снова, напишите /start.')
	if c.data == "SOCKS4":
		proxy_choice = random.randrange(0, len(socks4))
		bot.send_message(c.message.chat.id, f'Тип прокси: {c.data}.\nПрокси: {socks4[proxy_choice]}\nЕсли понадоблюсь снова, напишите /start.')

@bot.message_handler(commands = ['creator'])
def creator(message):
	markup = types.InlineKeyboardMarkup()
	creator_button = types.InlineKeyboardButton(text='Создатель бота', url='https://t.me/foxuserbot_000')
	markup.add(creator_button)
	bot.send_message(message.chat.id, "Если хотите поблагодарить создателя бота или задать вопрос нажимайте на кнопку!", reply_markup = markup)
		
bot.polling(none_stop=True)