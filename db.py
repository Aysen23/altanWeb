import sqlite3 as sql

# декоратор try-except
def except_decorator(func):
    def wrapper(*arg):
        try:
            return func(*arg)
        except sql.Error as e:
            print(f"Ошибка БД: {e}")
        except Exception as e:
            print(f"Ошибка сервера: {e}")
    return wrapper

# создание БД
@except_decorator
def create_db(path):
    with sql.connect(path) as db:
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS log_table
            (form TEXT, result TEXT)
            """
        )
        db.commit()

# запись данных в БД
@except_decorator
def write_db(path, form, res):
    with sql.connect(path) as db:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO log_table VALUES (?, ?)",
            (form, res)
        )
        db.commit()

# чтение данных из БД
@except_decorator
def read_db(path):
     with sql.connect(path) as db:
         cursor = db.cursor()
         cursor.execute(
             "SELECT * FROM log_table"
         )
         return cursor.fetchall()