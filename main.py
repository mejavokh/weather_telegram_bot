import telebot
import requests
from .configs import *


bot = telebot.TeleBot(TOKEN)
API = API
URL = URL


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Здравствуйте {message.chat.first_name} 😊. '
                                      f'Напишите название города ⬇️⬇️⬇️')


@bot.message_handler(content_types=['text'])
def weather(message):
    city = message.text.strip().lower()

    parametres = {
        'q': city,
        'appid': API,
        'units': 'metric',
        'lang': 'ru'
    }

    req = requests.get(URL, params=parametres)
    req_j = req.json()

    if req.status_code == 200:
        city_name = req_j['name']
        desc = req_j['weather'][0]['description']
        temp = req_j['main']['temp']
        feels = req_j['main']['feels_like']
        wind = req_j['wind']['speed']
        hum = req_j['main']['humidity']
        press = req_j['main']['pressure']

        bot.reply_to(message, f'Локация, где природа раскрывает свои тайны: {city_name}\n'
                              f'Танец природы в симфонии времени: {desc} \n'
                              f'Температурный ритм местности: {temp} °C.\n'
                              f'Сенсорный опыт атмосферы: {feels} °C\n'
                              f'Дыхание ветра, ласкающее город: {wind} м/с \n'
                              f'Влага, которая танцует в воздухе: {hum} г/м3 \n'
                              f'Давление атмосферы, как пульс Земли: {press} Pa\n'
                              f'Рад был помочь вам 😊')
    else:
        bot.reply_to(message, 'Ошибка ввода 🤨! Давайте посмотрим на наши клавиши с другой стороны и попробуем еще раз 🫡.'
                              'Клавиатурный калейдоскоп готов следовать вашим указаниям 😊 !!')


bot.polling(none_stop=True)















