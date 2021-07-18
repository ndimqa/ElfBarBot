# import sqlalchemy
# import pandas as pd
# 
# engine = sqlalchemy.create_engine('sqlite://Users/baimu/PycharmProjects/elfbarBot/Shop.db')  # Путь к бд
# df = pd.read_excel('Tovary(800).xlsx')
# df.rename(columns={
#     'ID вкуса': 'vkus',
#     'Количество': 'quantity'
# })
# 
# df.to_sql (
#     name='tovary(800)',
#     con=engine,
#     index=False,
#     if_exists='append'
# )


# Скрипт для парсинга данных из эксель таблиц в SQL DB. Нужно переделать SQL таблицы, и сделать два файла на 800 и 1500 типов. Оттуда можно доставать переменную для проверки наличия товара, менять значения
