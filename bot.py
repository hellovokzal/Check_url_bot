import requests as req
import telebot
import threading as t

def check_url():
    global url
    try:
        code = req.get(url)
        bot.send_message(message.chat.id, f"Url: `{url}`\nStatus code: `{code.status_code}`")
    except:
        bot.send_message(message.chat.id, f"Url: `{url}`\nStatus code: `403 Forbidden`")
    
bot = telebot.TeleBot("6506417857:AAGo4jRMB4obCIUgzSZo82n1SsWLyGnqL20")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Пиши команду /check <ссылка>\n/check https://google.com")
@bot.message_handler(commands=['check'])
def check(message):
    url = message.text[7:len(message.text)]
    if url[0:8] == "https://" or url[0:7] == "http://":
        check_host = t.Thread(target=check_url)
        check_host.start()
    else:
        bot.send_message(message.chat.id, f"Url: `{url}`\nStatus code: `Error target url!`")
bot.polling(none_stop=True)
