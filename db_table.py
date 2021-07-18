import sqlite3

with sqlite3.connect('Shop.db') as db:
    cursor = db.cursor()
    type_query1 = """ INSERT INTO type (id, type) VALUES (1, 800) """
    type_query2 = """ INSERT INTO type (id, type) VALUES (2, 1500) """
    vkusy_query1 = """ INSERT INTO vkusy (id, vkus) VALUES (1, "Strawberry ice") """
    vkusy_query2 = """ INSERT INTO vkusy (id, vkus) VALUES (2, "Mint") """
    vkusy_query3 = """ INSERT INTO vkusy (id, vkus) VALUES (2, "Mango") """
    cursor.execute(type_query1)
    cursor.execute(type_query2)
    cursor.execute(vkusy_query1)
    cursor.execute(vkusy_query2)
    cursor.execute(vkusy_query3)
