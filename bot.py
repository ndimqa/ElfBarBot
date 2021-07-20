#!/usr/bin/python
# -*- coding: utf8 -*-


from config import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from sqlite3 import Error

import re
import markups as nav
import sqlite3


korzina: str = ''
KolvoTovara = 0



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


class Client:
    phone: str
    address: str
    zakaz: str

    def __init__(self, Name, phone, addres, zakaz) -> None:
        self.phone = phone
        self.address = addres
        self.zakaz = zakaz

    def SendToDB(self):
        pass

    def ReturnAll(self):
        return self.phone + " " + self.address + " " + self.zakaz


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_zakaz(conn, task):
    sql = ''' INSERT INTO zakaz (type, vkus, quantity)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def create_client(conn, task):
    sql = ''' INSERT INTO client (id, phone, address, zakaz_type, zakaz_vkus, zakaz_quantity)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


database = r"C:\Users\baimu\PycharmProjects\elfbarBot\Shop.db"   # твой путь к бд
conn = create_connection(database)


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
    pozicia = Pozicia(800, 0, "default")


@dp.message_handler(text="ElfBar (Lux) на 1500 затяжек")
async def send_1500(message: types.Message):
    await bot.send_photo(message.from_user.id, AllElfBar,
                         caption="Цена: *цена* \nОписание: Elf Bar 1500 обеспечивает яркий и насыщенный вкус благодаря специальной системе нагрева. Аккумулятор ёмкостью 850мАч обеспечивает стабильность работы на протяжении 1500 затяжек. Это позволяет получить максимальное удовольствие от использования.",
                         reply_markup=nav.MainVkusMenu)
    global pozicia
    pozicia = Pozicia(1500, 0, "default")


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


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, ElfMint, caption="Выбран вкус Mint", reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia.vkus = "Mint"


@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, ElfMango, caption="Выбран вкус Mango",
                         reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia.vkus = "Mango"


# Выбор количества
@dp.message_handler(text="Перейти к выбору количества")
async def cmd_random(message: types.Message):
    await message.reply("Введите какое количество данной электронной сигареты вы хотите (макс. 15):")

    @dp.message_handler(regexp='^([1-9][0-9]{0,2}|1000)$')
    async def take_quantity(message: types.Message):
        global pozicia
        global KolvoTovara
        global korzina
        pozicia.quantity = int(message.text)
        KolvoTovara += pozicia.quantity
        korzina += pozicia.ReturnPozicia() + ","
        with conn: # я думаю это не нужно потому что если человек захочет очистить корзину то все данные все равно остануться в этой таблице
            task_1 = (pozicia.type, pozicia.vkus, pozicia.quantity)
            create_zakaz(conn, task_1)
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
                           f"Ваш заказ: "+ korzina,
                           reply_markup=nav.DecMenu1)


@dp.message_handler(text="Нет")
async def cmd_random(message: types.Message):
    await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)


# Формирование клиента
@dp.message_handler(text="Да")
async def take_phone(message: types.Message):
    global clien
    zakaz = pozicia.ReturnPozicia()
    clien = Client('none', 0, 'none', zakaz)
    await bot.send_message(message.from_user.id,
                           "Введите ваш номер телефона, начиная с цифры 8")

    @dp.message_handler(regexp='^[8][0-9]{10}$')
    async def take_phone(message: types.Message):
        global clien
        clien.phone = message.text
        print(clien.ReturnAll())
        await bot.send_message(message.from_user.id, "Введите ваш адрес")

        @dp.message_handler()
        async def take_address(message: types.Message):
            clien.address = message.text
            print(clien.ReturnAll())
            with conn:
                task_2 = (1, clien.phone, clien.address, pozicia.type, pozicia.vkus, pozicia.quantity)
                create_client(conn, task_2)
            await bot.send_message(message.from_user.id, 'Готово')


# Корзина
@dp.message_handler(text="Удалить товар")
async def cmd_random(message: types.Message):
    await bot.send_message(message.from_user.id, "Какой товар вы хотите удалить?" + korzina)
    #не доделано


@dp.message_handler(text="Очистить корзину")
async def take_address(message: types.Message):
    global korzina
    korzina = ''


if __name__ == '__main__':
    executor.start_polling(dp)

