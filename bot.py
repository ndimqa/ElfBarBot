#!/usr/bin/python
# -*- coding: utf8 -*-

from config import TOKEN  

import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import message
from aiogram.utils import executor


import markups as nav

korzina:int = 0

class Pozicia:
    type:int
    quantity:int
    vkus:int

    def __init__(self, type, quantity, vkus):
        self.type = type
        self.quantity = quantity
        self.vkus = vkus  
    
    def ReturnPozicia(self):
        self.pozicia = self.vkus + " " + self.type + " " + self.quantity
        return self.pozicia 

class Zakaz:
    zakaz: list
    def __init__(self, zakaz) -> None:
        self.zakaz = zakaz
    

class Client:
    Name:str
    phone:str
    address:str
    Tov:Zakaz

#инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет, {0.first_name}!\nЭтот телеграм бот для заказа электронных сигарет Elf Bar. Ниже вы найдете каталог товаров которые есть в наличии. Спасибо что выбираете нас.\nПриятных покупок!".format(
                               message.from_user), reply_markup=nav.mainMenu)

# Навигация
@dp.message_handler(text="⬅️ Главное меню")
async def cmd_random(message: types.Message):
    await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)

@dp.message_handler(text="Каталог")
async def cmd_random(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный товар', reply_markup=nav.KatMenu)

@dp.message_handler(text="Корзина")
async def cmd_random(message: types.Message):
     await bot.send_message(message.from_user.id, 'Корзина', reply_markup=nav.KorzMenu)

#Каталог
@dp.message_handler(text="ElfBar (800 Затяжек), Lux ElfBar (800 затяжек)")
async def cmd_random(message: types.Message):
    await bot.send_photo(message.from_user.id, Elf800, caption="Одноразовая электронная сигарета Elfbar 800 от одноименной компании компании. Поставляется в индивидуальной упаковке с концентрацией 5% никотина. Приятная тугая затяжка и насыщенные вкусы позволят в полной мере насладится данным устройством. Работает при помощи авто-затяжки и позволяет совершать до 800 затяжек.")


@dp.message_handler(text="ElfBar (1500 Затяжек), Lux ElfBar (1500 затяжек)")
async def cmd_random(message: types.Message):
    await bot.send_photo(message.from_user.id, Elf1500, caption="Одноразовая электронная сигарета Elfbar 800 от одноименной компании компании. Поставляется в индивидуальной упаковке с концентрацией 5% никотина. Приятная тугая затяжка и насыщенные вкусы позволят в полной мере насладится данным устройством. Работает при помощи авто-затяжки и позволяет совершать до 800 затяжек.")
#     # и т.д
              #Примерный расчет товара
            # @dp.message_handler(lambda message: not message.text.isdigit(), state=Zakaz.quantity)
            # async def cmd_random(message: types.Message):
            #    await bot.send_message(message.from_user.id, 'Введите нужно количество товара')
            #    korzina += 1
            
#Корзина
@dp.message_handler(text="Продолжить покупку")
async def cmd_random(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите Ваш номер телефона (с +7)')
    
    @dp.message_handler(lambda message:message.text.startswith("+7"), Client.phone)
    async def cmd_random(message: types.Message):
        await bot.send_message(message.from_user.id, 'Введите ваш адрес')
        
        @dp.message_handler(Client.address)
        async def cmd_random(message: types.Message):
            await bot.send_message(message.from_user.id, 'Введите ваше Имя')
            
            @dp.message_handler(Client.name)
            async def cmd_random(message: types.Message):
                await bot.send_message(message.from_user.id, 'Введите ваше Имя')

#Нужно продумать логику удаления и очищения корзины
# @dp.message_handler(text="Удалить товар")
# async def cmd_random(message: types.Message):
# ...
# if korzina = 0, nav.mainMenu
# if korzina != 0, korzina--

# @dp.message_handler(text="Очистить корзину")
# async def cmd_random(message: types.Message):


if __name__ == '__main__':
    executor.start_polling(dp)
