#!/usr/bin/python
# -*- coding: utf8 -*-


from os import pathconf, pathconf_names
from config import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import markups as nav

korzina: int = 0


class Pozicia:
    type: int
    quantity: int
    vkus: int

    def __init__(self, type, quantity, vkus):
        self.type = type
        self.quantity = quantity
        self.vkus = vkus

    def ReturnPozicia(self):
        self.pozicia = self.vkus + " " + str(self.type) + " " + str(self.quantity)
        return self.pozicia


class Zakaz:
    zakaz: list
    def __init__(self, zakaz):
        self.zakaz = zakaz

class Client:
    Name: str
    phone: str
    address: str
    Tov: Zakaz
    def __init__(self, Name, phone, addres, Tov) -> None:
        self.Name = Name
        self.phone = phone
        self.address = addres
        self.Tov = Tov

    def SendToDB(self):
        pass

# Фотографии из корневой папки
AllElfBar = open("AllElfBar.jpg", 'rb')
ElfMint = open("Mint.jpg", 'rb')
ElfMango = open("MangoBar.jpg", 'rb')
ElfStraw = open("StrawBerryIce.jpg", 'rb')

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Команда /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Привет, {0.first_name}!\nЭтот телеграм бот для заказа электронных сигарет Elf Bar. Ниже вы найдете каталог товаров которые есть в наличии. Спасибо что выбираете нас.\nПриятных покупок!".format(
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


# Каталог
# Отправка фотографии и описания при нажатии
@dp.message_handler(text="ElfBar (Lux) на 800 затяжек")
async def cmd_random(message: types.Message):
    await bot.send_photo(message.from_user.id, AllElfBar,
                         caption="Цена: 2100 \nОписание: Elf Bar 800 обеспечивает яркий и насыщенный вкус благодаря специальной системе нагрева. Аккумулятор ёмкостью 550мАч обеспечивает стабильность работы на протяжении 800 затяжек. Это позволяет получить максимальное удовольствие от использования.",
                         reply_markup=nav.MainVkusMenu)
    global pozicia
    pozicia=Pozicia(800, 0, "default") # Перепроверить


@dp.message_handler(text="ElfBar (Lux) на 1500 затяжек")
async def cmd_random(message: types.Message):
    await bot.send_photo(message.from_user.id, AllElfBar,
                         caption="Цена: *цена* \nОписание: Elf Bar 1500 обеспечивает яркий и насыщенный вкус благодаря специальной системе нагрева. Аккумулятор ёмкостью 850мАч обеспечивает стабильность работы на протяжении 1500 затяжек. Это позволяет получить максимальное удовольствие от использования.",
                         reply_markup=nav.MainVkusMenu)
    global pozicia
    pozicia = Pozicia(1500, 0, "default") # Перепроверить


# Вкусы
@dp.message_handler(text="Перейти к вкусам")
async def cmd_random(message: types.Message):
    await message.reply("Все вкусы представлены ниже", reply_markup=nav.VkusMenu)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, ElfStraw, caption="Выбран вкус Strawberry ice", reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia.vkus = "Strawberry ice"


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, ElfMint, caption="Выбран вкус Mint", reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia.vkus = "Mint"


@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, ElfMango, caption="Выбран вкус Mango", reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia.vkus = "Mango"


# Выбор количества
@dp.message_handler(text="Перейти к выбору количества")
async def cmd_random(message: types.Message, quantity = 2):
    await message.reply("Введите какое количество данной электронной сигареты вы хотите (макс. 15): ", quantity)
    global pozicia
    pozicia.quantity = quantity
    print(pozicia.ReturnPozicia()) # Перепроверить

# Корзина
@dp.message_handler(text="Оформить заказ")
async def cmd_random(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите Ваш номер телефона (с +7)')

    @dp.message_handler(lambda message: message.text.startswith("+7"), Client.phone) # Перепроверить дважды
    async def cmd_random(message: types.Message):
        await bot.send_message(message.from_user.id, 'Введите ваш адрес')

        @dp.message_handler(Client.address)
        async def cmd_random(message: types.Message):
            await bot.send_message(message.from_user.id, 'Введите ваше Имя')

            @dp.message_handler(Client.Name)
            async def cmd_random(message: types.Message):
                await bot.send_message(message.from_user.id, 'Готово!')


# Логика удаления и очищения корзины
# @dp.message_handler(text="Удалить товар")
# async def cmd_random(message: types.Message):
# ...
# if korzina = 0, nav.mainMenu
# if korzina != 0, korzina--

# @dp.message_handler(text="Очистить корзину")
# async def cmd_random(message: types.Message):


if __name__ == '__main__':
    executor.start_polling(dp)
