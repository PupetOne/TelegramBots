import telebot
from telebot import types

bot = telebot.TeleBot("1686756740:AAGwTrm-o91o17n3-DwkTUxJ2Mnrvwy1kCE")

name = ""
surname = ""
age = 0


@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, "Welcome, I'm Golem Bot for Telegram.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "Hi":
        bot.reply_to(message, "Hi... What do you need?")
    elif message.text == "Hello":
        bot.reply_to(message, "Hi... What do you need?")
    elif message.text == "/reg":
        bot.send_message(message.from_user.id, "What is your name?..")
        bot.register_next_step_handler(message, reg_name)
    elif message.text == "/infome":
        bot.reply_to(message, "Did you forget who you are?.. " + name + " " + surname + ". Now everything is on its places?")
    #else:
    #   bot.reply_to(message, message.text)
    #

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "What is your... surname?")
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Here you go... I'll remember you... But let's repeat.")
#    bot.register_next_step_handler(message, reg_fin)

    question = "So... Your name: " + name + ". Surname: " + surname + ". I'm right?"
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Yes", callback_data="yes")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="No", callback_data="no")
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

#def reg_age(message):
#global age
#age = message.text
#while age == 0:
#    try:
#        age = int(message.text)
#    except Exception:
#        bot.send_message(message.from_user.id, "... Numbers, please!")


@bot.callback_query_handler(func = lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Now I'll never forget you...")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "My memory is perfect... I think, you better to present yourself one more time...")
        bot.send_message(call.message.chat.id, "What is your name?..")
        bot.register_next_step_handler(call.message, reg_name)



bot.polling()