#импортируем TOKEN  с папки config
from config import TOKEN  

import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor

#инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЭтот телеграм бот нужен для заказа электронных сигарет(Elf Bar), ниже вы найдете каталоги товаров которые есть в нашем магазине. Спасибо что выбираете нас.\n приятных покупок.")

if __name__ == '__main__':
    executor.start_polling(dp)