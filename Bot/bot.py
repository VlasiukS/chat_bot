from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='581261705:AAHc7mm3Ilm_fJRa23LytXXpl6VH1CQjD7I') # Токен API к Telegram
dispatcher = updater.dispatcher


def start_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, как дела?')


def text_message(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


# Хендлеры
start_command_handler = CommandHandler('start', start_command)
text_message_handler = MessageHandler(Filters.text, text_message)

# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()