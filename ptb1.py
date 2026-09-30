from telegram.ext import Updater, CommandHandler

def start_func(update, context):
    update.message.reply_text(text='hi!')
    print(update.message.text)
    print(context.bot)

    show = update.message.from_user.id = f'user-id: {update.message.from_user.id}'
    show = update.message.from_user.first_name = f'name: {update.message.from_user.first_name}'
    show = update.message.from_user.last_name = f'last-name: {update.message.from_user.last_name}'
    show = update.message.from_user.username = f'username: @{update.message.from_user.username}\n'


    show = update.message.from_user.id,update.message.from_user.first_name, update.message.from_user.last_name, update.message.from_user.username
    for i in show:
        print(i)

updater = Updater(token='')
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_func))

updater.start_polling()
updater.idle()
