#!/usr/bin/python
# -*- coding: utf8 -*-


from config import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from sqliter import SQLighter

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


pozicia: Pozicia


class Zakaz:
    zakaz: list

    def __init__(self, zakaz):
        self.zakaz = zakaz


class Client:
    Name: str
    phone: str
    address: str
    Tov: Pozicia

    def __init__(self, Name, phone, addres, Tov) -> None:
        self.Name = Name
        self.phone = phone
        self.address = addres
        self.Tov = Tov

    def SendToDB(self):
        pass


db = SQLighter('Shop.db')

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
async def send_800(message: types.Message):
    await bot.send_photo(message.from_user.id, AllElfBar,
                         caption="Цена: 2100 \nОписание: Elf Bar 800 обеспечивает яркий и насыщенный вкус благодаря специальной системе нагрева. Аккумулятор ёмкостью 550мАч обеспечивает стабильность работы на протяжении 800 затяжек. Это позволяет получить максимальное удовольствие от использования.",
                         reply_markup=nav.MainVkusMenu)
    global pozicia
    pozicia = Pozicia(800, 0, "default")  # Перепроверить
    Client.Tov = Pozicia(800, 0, "default")


@dp.message_handler(text="ElfBar (Lux) на 1500 затяжек")
async def send_1500(message: types.Message):
    await bot.send_photo(message.from_user.id, AllElfBar,
                         caption="Цена: *цена* \nОписание: Elf Bar 1500 обеспечивает яркий и насыщенный вкус благодаря специальной системе нагрева. Аккумулятор ёмкостью 850мАч обеспечивает стабильность работы на протяжении 1500 затяжек. Это позволяет получить максимальное удовольствие от использования.",
                         reply_markup=nav.MainVkusMenu)
    global pozicia
    pozicia = Pozicia(1500, 0, "default")  # Перепроверить
    Client.Tov = Pozicia(1500, 0, "default")


# Вкусы
@dp.message_handler(text="Перейти к вкусам")
async def cmd_random(message: types.Message):
    await message.reply("Все вкусы представлены ниже", reply_markup=nav.VkusMenu)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, ElfStraw, caption="Выбран вкус Strawberry ice",
                         reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia.vkus = "Strawberry ice"
    Client.Tov.vkus = "Strawberry ice"


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, ElfMint, caption="Выбран вкус Mint", reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia.vkus = "Mint"
    Client.Tov.vkus = "Mint"


@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, ElfMango, caption="Выбран вкус Mango",
                         reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia.vkus = "Mango"
    Client.Tov.vkus = "Mango"


# Выбор количества
@dp.message_handler(text="Перейти к выбору количества")
async def cmd_random(message: types.Message):
    await message.reply("Введите какое количество данной электронной сигареты вы хотите (макс. 15): ")

    @dp.message_handler()
    async def take_quantity(message: types.Message):
        global pozicia
        pozicia.quantity = message.text
        print(pozicia.ReturnPozicia())  # Перепроверить
        Client.Tov.quantity = message.text
        await message.reply(
            "Если вы хотите продолжить заказ, нажмите кнопку 'Продолжить заказ' \n Для оформления закзаза намите кнопку 'Оформить заказ'",
            reply_markup=nav.DecMenu)


# Навигация
@dp.message_handler(text="Продолжить заказ")
async def cmd_random(message: types.Message):
    await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)


@dp.message_handler(text="Оформить заказ")
async def cmd_random(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Ваш заказ: \nElf Bar {pozicia.type} затяжек \nВкус: {pozicia.vkus} \nКоличество: {pozicia.quantity}. Все правильно?",
                           reply_markup=nav.DecMenu1)


@dp.message_handler(text="Нет")
async def cmd_random(message: types.Message):
    await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)


# Формирование клиента
@dp.message_handler(text="Да")
async def take_phone(message: types.Message):
    await bot.send_message(message.from_user.id, "Введите ваш номер телефона")  # Перепроверить дважды

    @dp.message_handler()
    async def take_quantity(message: types.Message):
        Client.phone = message.text
        await bot.send_message(message.from_user.id, "Введите ваш адрес")

        @dp.message_handler()
        async def take_address(message: types.Message):
            Client.address = message.text
            await bot.send_message(message.from_user.id, 'Введите ваше Имя')

            @dp.message_handler()
            async def take_name(message: types.Message):
                Client.Name = message.text
                await bot.send_message(message.from_user.id, 'Готово!')


# Корзина
# @dp.message_handler(text="Удалить товар")
# async def cmd_random(message: types.Message):
# ...
# if korzina = 0, nav.mainMenu
# if korzina != 0, korzina--

# @dp.message_handler(text="Очистить корзину")
# async def cmd_random(message: types.Message):


if __name__ == '__main__':
    executor.start_polling(dp)

