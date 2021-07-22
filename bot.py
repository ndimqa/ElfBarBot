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

allKorz: list = []


def listToString(s):
    str1 = " "
    return (str1.join(s))


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

    def __init__(self, phone, addres, zakaz) -> None:
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


def IfAvaliable():
    pass  # смотреть есть ли в наличии товар если нет то он должен отправлять сообщение


def create_client(conn, task):
    sql = ''' INSERT INTO client (tg_user, phone, address, zakaz)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def delete_record(conn, task):
    sql = ''' DELETE FROM client WHERE zakaz = ? '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


database = r"Shop.db"  # твой путь к бд
conn = create_connection(database)


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
    await bot.send_message(message.from_user.id, 'Вы в корзине', reply_markup=nav.KorzMenu)
        if not allKorz:
        await bot.send_message(message.from_user.id, 'В корзине пусто')
    else:
        await bot.send_message(message.from_user.id, "Ваша корзина: " + listToString(allKorz))


# Каталог
# Отправка фотографии и описания при нажатии
@dp.message_handler(text="ElfBar (Lux) на 800 затяжек")
async def send_800(message: types.Message):
    global AllElfBar
    AllElfBar = open("AllElfBar.jpg", 'rb')
    await bot.send_photo(message.from_user.id, AllElfBar,
                         caption="Цена: 2100 \nОписание: Elf Bar 800 обеспечивает яркий и насыщенный вкус благодаря специальной системе нагрева. Аккумулятор ёмкостью 550мАч обеспечивает стабильность работы на протяжении 800 затяжек. Это позволяет получить максимальное удовольствие от использования.",
                         reply_markup=nav.MainVkusMenu)
    global pozicia
    pozicia = Pozicia(800, 0, "default")


@dp.message_handler(text="ElfBar (Lux) на 1500 затяжек")
async def send_1500(message: types.Message):
    global AllElfBar
    AllElfBar = open("AllElfBar.jpg", 'rb')
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
    global ElfStraw
    ElfStraw = open("StrawBerryIce.jpg", 'rb')
    await bot.send_photo(callback_query.from_user.id, ElfStraw, caption="Выбран вкус Strawberry ice",
                         reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia.vkus = "Strawberry ice"


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    global ElfMint
    ElfMint = open("Mint.jpg", 'rb')
    await bot.send_photo(callback_query.from_user.id, ElfMint, caption="Выбран вкус Mint", reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia.vkus = "Mint"


@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    global ElfMango
    ElfMango = open("MangoBar.jpg", 'rb')
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
        global allKorz
        pozicia.quantity = int(message.text)
        await message.reply(
            "Если вы хотите продолжить заказ, нажмите кнопку 'Продолжить заказ' \n Для добавления заказа в корзину нажмите 'Добавить в корзину'",
            reply_markup=nav.DecMenu)


# Навигация
@dp.message_handler(text="Продолжить покупку")
async def cmd_random(message: types.Message):
    allKorz.clear()
    await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)


@dp.message_handler(text="Добавить в корзину")
async def cmd_random(message: types.Message):
    global allKorz
    global pozicia
    allKorz.append(pozicia.ReturnPozicia())
    await bot.send_message(message.from_user.id,
                           f"Ваш заказ: " + listToString(allKorz),
                           reply_markup=nav.DecMenu1)


@dp.message_handler(text="Нет")
async def cmd_random(message: types.Message):
    allKorz.clear()
    await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)


# Формирование клиента
@dp.message_handler(text="Да")
async def take_phone(message: types.Message):
    await bot.send_message(message.from_user.id, 'Товар добавлен в корзину! Для оформления заказа перейдите в корзину. Можете продолжать покупку', reply_markup=nav.mainMenu)


# Корзина
@dp.message_handler(text="Очистить корзину")
async def clean(message: types.Message):
    global allKorz
    allKorz.clear()
    await bot.send_message(message.from_user.id, "Корзина очищена")


@dp.message_handler(text="Оформить заказ")
async def take_phone(message: types.Message):
    global clien
    zakaz = pozicia.ReturnPozicia()
    clien = Client('none', 'none', zakaz)
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
            tg_user: str = message.from_user.first_name
            clien.address = message.text
            print(clien.ReturnAll())
            with conn:
                task_2 = (tg_user, clien.phone, clien.address, listToString(allKorz))
                create_client(conn, task_2)
            await bot.send_message(message.from_user.id, 'Готово! Ваш заказ принят и уже готовится к сборке. Пожалуйста, закажите доставку или заберите товар сами с адреса: *адрес*', reply_markup=nav.mainMenu)


if __name__ == '__main__':
    executor.start_polling(dp)
