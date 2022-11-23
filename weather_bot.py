import os
import datetime
import requests
import random
import pathlib
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from add_secrets import add_secrets

add_secrets()

def get_weather(city_name):

    api_key = os.getenv("WEATHER_API_KEY")
    geocoding_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={api_key}'


    geo_r = requests.get(geocoding_url)
    # print(geo_r.text)
    geo_data = geo_r.json()
    # print(geo_data)
    latitude = geo_data[0]["lat"]
    longitude = geo_data[0]["lon"]

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    
    weather_r = requests.get(weather_url)
    weather_data = weather_r.json()
    text_weather = str(weather_data["main"])
    return text_weather


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    htext = '''
Welcome
There's not much here yet
'''
    await update.message.reply_text(htext)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_message_text = f'Hello {update.effective_user.first_name}'
    await update.message.reply_text(reply_message_text)


async def get_weather_in_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    full_message_text = update.message.text
    city_name = full_message_text.split(maxsplit=1)[1]
    weather_text = get_weather(city_name)

    await update.message.reply_text(weather_text)




def main():
    my_token = os.getenv("TOKEN")

    app = ApplicationBuilder().token(my_token).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("weather", get_weather_in_city))

    app.run_polling()



if __name__ == '__main__':
    main()
