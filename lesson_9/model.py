# Создайте любую программу.py при помощи виртуального окружения и PIP. 
# отправте репозиторий где будет этот файл и файл requirements.txt 
# 2.Создайте любого бота телеграмм(можно самый простой), 
# главное чтобы у вас к след. уроку был свой бот в телеграмме, 
# в нем вы сможете работать над созданием нового бота на 10 семинаре.
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import*


app = ApplicationBuilder().token("5960569233:AAFqo_S-gJNVFJJOgQouB_41JQ9cl57CkQA").build()
print('start server')
app.add_handler(CommandHandler("hello", hello))

app.run_polling()