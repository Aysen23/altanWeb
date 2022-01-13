# Система управления базами данных (СУБД) SQlite3

import sqlite3 as sql

path = "data/test.db"

# соединение с БД
db = sql.connect(path)
# объект курсора ("панель управления")
cursor = db.cursor()

# Создание БД "test" таблицей "test_1"

# передача команд на языке SQL ("управление БД")
# command = """
#     create table test_1 
#     (id integer, login text, weight real)"""
# cursor.execute(command)
# # закрепление изменений
# db.commit()

# создание таблицы с проверкой на наличие
command = """
    create table if not exists test_1 
    (id integer, login text, weight real)"""
cursor.execute(command)
# закрепление изменений
db.commit()

# создание второй таблицы "test_2"
command = "CREATE TABLE IF NOT EXISTS test_2 (num INTEGER, f_name TEXT, l_name TEXT)"
cursor.execute(command)
# закрепление изменений
db.commit()

# запись в БД

# command_w = "INSERT INTO test_1 VALUES (?, ?, ?)"
# data_0 = (0, "ivan", 3.14)
# cursor.execute(command_w, data_0)

# data_1 = (1, "peter", 100.23)
# command_w = f"INSERT INTO test_1 VALUES {data_1}"
# cursor.execute(command_w)

data_2 = (1, "peter", "ivanov")
command_w = f"INSERT INTO test_2 VALUES {data_2}"
cursor.execute(command_w)

data_3 = (2, "ivan", "ivanov")
command_w = f"INSERT INTO test_2 VALUES {data_3}"
cursor.execute(command_w)

db.commit()

# чтение из БД

command_1 = "SELECT * FROM test_1"
cursor.execute(command_1)

# все строки таблицы
# data = cursor.fetchall()
# print(data)
# значения по одному
# raw_0 = cursor.fetchone()
# print(raw_0)
# raw_1 = cursor.fetchone()
# print(raw_1)
# raw_2 = cursor.fetchone()
# print(raw_2)
# raw_3 = cursor.fetchone()
# print(raw_3)
# for _ in range(5):
#     print(cursor.fetchone())

# определённое кол-во значений
# print(cursor.fetchmany())
# print(cursor.fetchmany())
print(cursor.fetchmany(15))

# чтение из второй таблицы
command_2 = "SELECT l_name, f_name FROM test_2"
cursor.execute(command_2)
print(cursor.fetchmany(15))

# закрытие БД
db.close()