from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('⬅️ Главное меню')
btnKorz = KeyboardButton('Корзина')

#Главное меню
btnKat = KeyboardButton('Каталог')
btnKorzina = KeyboardButton('Корзина')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnKat, btnKorzina)

#Каталог
Zat_800 = KeyboardButton('ElfBar (800 Затяжек)')
Zat_1500 = KeyboardButton('ElfBar (1500 Затяжек)')
Lux_800 = KeyboardButton('Lux ElfBar (800 затяжек)')
Lux_1500 = KeyboardButton('Lux ElfBar (1500 затяжек)')
KatMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(Zat_800, Zat_1500, Lux_800, Lux_1500, btnMain)

#Вкусы
Vkus_1 = KeyboardButton('Вкус 1')
Vkus_2 = KeyboardButton('Вкус 2')
Vkus_3 = KeyboardButton('Вкус 3')
Vkus_4 = KeyboardButton('Вкус 4')
VkusMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(Vkus_1, Vkus_2, Vkus_3, Vkus_4, btnKat)

#Корзина
btnBuy = KeyboardButton('Продолжить покупку')
btnDelete = KeyboardButton('Удалить товар')
btnClear = KeyboardButton('Очистить корзину')
KorzMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnBuy, btnDelete, btnClear, btnMain)


