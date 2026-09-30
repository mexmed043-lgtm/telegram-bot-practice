from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton

ADMIN_ID = 

def start_command(update, context):
    print(update.message.from_user.id)

    update.message.reply_text(text='''Salom Bo'timizga xush kelibsiz 👍'''),
    update.message.reply_text(text='''Menyuni oching ochish uchun: /menu''')

def show_menu(update, context):
    buttons = [
        [KeyboardButton(text='Send Contact', request_contact=True),
         KeyboardButton(text='Send Location', request_location=True)],

        [KeyboardButton(text="Menyu-3"), KeyboardButton(text='Menyu-4')],
    ]

    update.message.reply_text(
        text='Menyu',
        reply_markup=ReplyKeyboardMarkup(buttons, resize_markup=True, one_time_keyboard=True)
    )


def message_handler(update, context):
    message = update.message.text
    update.message.reply_text(text= f'Sizning xabaringiz: {message} Bunday xabarga bot vazifa bajarmaydi!')

def contact_handler(update, context):
    phone_number = update.message.contact.phone_number
    context.bot.send_message(chat_id=ADMIN_ID, text=f'yangi foydalanuvchi raqami: {phone_number}')

def location_handler(update, context):
    location = update.message.location
    context.bot.send_location(chat_id=ADMIN_ID, text=f'yangi foydalanuvchi lakatsiyasi: {location}')



def main():
    updater = Updater(token='')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('menu', show_menu))

    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))




    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
