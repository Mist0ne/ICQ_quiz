from bot.bot import Bot
from bot.handler import MessageHandler, CommandHandler, Filter
import random

tasks = {'Назовите первую букву алфавита': ['А', 'a'], 'Назовите последнюю букву алфавита': ['Я', 'я']}
value = []

TOKEN = "" # it's a secret

bot = Bot(token=TOKEN)


def task_cb(bot, event):
    global value
    key, value = random.choice(list(tasks.items()))
    print(event.from_chat)
    bot.send_text(chat_id=event.from_chat, text=key)


def answer_cb(bot, event):
    global value
    if event.text in value:
        bot.send_text(chat_id=event.from_chat, text='Congratulations!')
    else:
        bot.send_text(chat_id=event.from_chat, text='Try again')


bot.dispatcher.add_handler(CommandHandler(command="new_question", callback=task_cb))
bot.dispatcher.add_handler(MessageHandler(filters=Filter.reply, callback=answer_cb))
bot.start_polling()
bot.idle()
