#!/usr/bin/python
# -*- coding: utf8 -*-


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
        self.pozicia = self.vkus + " " + self.type + " " + self.quantity
        return self.pozicia


pozicia: Pozicia


class Zakaz:
    zakaz: list

    def __init__(self, zakaz) -> None:
        self.zakaz = zakaz


class Client:
    Name: str
    phone: str
    address: str
    Tov: Zakaz


# Фотографии из корневой папки
Elf800 = open("ElfBar800.jpg", 'rb')
Elf1500 = open("ElfBar1500.jpg", 'rb')

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
@dp.message_handler(text="ElfBar (800 Затяжек) \n Lux ElfBar (800 затяжек)")
async def cmd_random(message: types.Message):
    await bot.send_photo(message.from_user.id, Elf800,
                         caption="Одноразовая электронная сигарета Elfbar 800 от одноименной компании компании. Поставляется в индивидуальной упаковке с концентрацией 5% никотина. Приятная тугая затяжка и насыщенные вкусы позволят в полной мере насладится данным устройством. Работает при помощи авто-затяжки и позволяет совершать до 800 затяжек.",
                         reply_markup=nav.MainVkusMenu)
    global pozicia
    pozicia=Pozicia(800, 0, "default")

@dp.message_handler(text="ElfBar (1500 Затяжек) \n Lux ElfBar (1500 затяжек)")
async def cmd_random(message: types.Message):
    await bot.send_photo(message.from_user.id, Elf1500,
                         caption="Elf Bar 1500 – удобная и вкусная одноразка на 1500 затяжек от компании Elf. Одноразовая Pod система не требует абсолютно никакой подзарядки и дозаправки жидкости, все что требуется это распаковать под-систему с защитного блистера и насладиться сочным и насыщенным вкусом. Картридж вмещает в себя 4.8 мл жидкости с содержанием 50 мг никотина, что примерно равно 1500 затяжкам. Электронки должно хватить на 4-8 дней парения, все зависит от частоты использования.",
                         reply_markup=nav.MainVkusMenu)
    global pozicia
    pozicia = Pozicia(1500, 0, "default")


# Вкусы
@dp.message_handler(text="Перейти к вкусам")
async def cmd_random(message: types.Message):
    await message.reply("Все вкусы представлены ниже", reply_markup=nav.VkusMenu)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Выбран вкус Strawberry ice', reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia = Pozicia(0, 0, "Strawberry ice")


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Выбран вкус Mint', reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia = Pozicia(0, 0, "Mint")


@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Выбран вкус Mango', reply_markup=nav.MainKolMenu)
    global pozicia
    pozicia = Pozicia(0, 0, "Mango")


# Выбор количества
@dp.message_handler(text="Перейти к выбору количества")
async def cmd_random(message: types.Message, quantity=None):
    await message.reply("Введите какое количество данной электронной сигареты вы хотите (макс. 15): ", quantity)
    global pozicia
    pozicia = Pozicia(0, quantity, "Strawberry ice")


# Корзина
@dp.message_handler(text="Оформить заказ")
async def cmd_random(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите Ваш номер телефона (с +7)')

    @dp.message_handler(lambda message: message.text.startswith("+7"), Client.phone)
    async def cmd_random(message: types.Message):
        await bot.send_message(message.from_user.id, 'Введите ваш адрес')

        @dp.message_handler(Client.address)
        async def cmd_random(message: types.Message):
            await bot.send_message(message.from_user.id, 'Введите ваше Имя')

            @dp.message_handler(Client.Name)
            async def cmd_random(message: types.Message):
                await bot.send_message(message.from_user.id, 'Готово!')
                # На данном этапе класс клиента должен быть готов


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
