import os
import datetime
import random
import pathlib
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from add_secrets import add_secrets

add_secrets()



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    htext = '''
Welcome
There's not much here yet
'''
    await update.message.reply_text(htext)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_message_text = f'Hello {update.effective_user.first_name}'
    await update.message.reply_text(reply_message_text)



def main():
    my_token = os.getenv("TOKEN")

    app = ApplicationBuilder().token(my_token).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()



if __name__ == '__main__':
    main()
