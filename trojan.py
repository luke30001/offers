import telebot
from telebot import types
bot=telebot.TeleBot("1066207372:AAH5nci3ekQGyN408w_5J1qIW2oWcMzoaWs")
@bot.channel_post_handler()
def hello(message):
    bot.reply_to(message,message.chat.id)
    #markup = types.InlineKeyboardMarkup()
    #itembtna = types.InlineKeyboardButton('Vai!',url="https://github.com/eternnoir/pyTelegramBotAPI#reply-markup")
    #markup.row(itembtna)
    #bot.send_message(-1001277502965,"ciao", reply_markup=markup)
    print(message.chat.id)
bot.polling()
#-1001503051596