import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Токен вашего бота
TOKEN = '8474791343:AAFPXCqWDWfbixSc2DiGookvWi6fJcZyNx0'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Задайте мне вопрос.')

def reply_to_message(update: Update, context: CallbackContext) -> None:
    if '?' in update.message.text:
        response = random.choice(['Да', 'Нет'])
        update.message.reply_text(response)

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
