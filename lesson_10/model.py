# # создать телеграмм бота желательно сложнее чем калькулятор. проявите свою фантазию и сделайте что то интересное
from aiogram import Bot, Dispatcher, executor, types
from translater import*
 
API_TOKEN = '5960569233:AAFqo_S-gJNVFJJOgQouB_41JQ9cl57CkQA'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
print('start server')
@dp.message_handler()
async def echo(message: types.Message):
   a = TranslateLang(message.text) 
   await message.answer(a)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)