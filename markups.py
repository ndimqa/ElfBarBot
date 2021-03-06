from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnMain = KeyboardButton('⬅️ Главное меню')
btnKorz = KeyboardButton('Корзина')
btnKat = KeyboardButton('Каталог')

#Главное меню
btnKat = KeyboardButton('Каталог')
btnKorzina = KeyboardButton('Корзина')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnKat, btnKorzina)

#Каталог
Zat_800 = KeyboardButton('ElfBar (Lux) на 800 затяжек')
Zat_1500 = KeyboardButton('ElfBar (Lux) на 1500 затяжек')
KatMenu = ReplyKeyboardMarkup(row_width=1).add(Zat_800, Zat_1500, btnMain)

#Вкусы
MainVkusBt = KeyboardButton('Перейти к вкусам')
MainVkusMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(MainVkusBt, btnKat)


Vkus1 = InlineKeyboardButton('Strawberry ice', callback_data='button1')
Vkus2 = InlineKeyboardButton('Mint', callback_data='button2')
Vkus3 = InlineKeyboardButton('Mango', callback_data='button3')
VkusMenu = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(Vkus1, Vkus2, Vkus3)

# Продолжить заказ
ProdBtn = KeyboardButton('Продолжить заказ')
AddBtn = KeyboardButton('Добавить в корзину')
DecMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(ProdBtn, AddBtn)

# Да/нет
YesBtn = KeyboardButton('Да')
NoBtn = KeyboardButton('Нет')
DecMenu1 = ReplyKeyboardMarkup(resize_keyboard=True).add(YesBtn, NoBtn)

# Выбор количества
MainKolBt = KeyboardButton('Перейти к выбору количества')
MainKolMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(MainKolBt, btnKat)

#Корзина
btnClear = KeyboardButton('Очистить корзину')
btnOform = KeyboardButton('Оформить заказ')
KorzMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnClear, btnOform, btnKat)

#Если нет в наличии
NotAvailableMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnKat)