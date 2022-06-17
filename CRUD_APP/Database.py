import mysql.connector
from mysql import connector

class Database:

    my_db = my_cursor = None

    def __init__(self, config):
        global my_db, my_cursor

        my_db = mysql.connector.connect(
            **config
            # host = config["host"],
            # user = config["user"],
            # password = config["password"],
            # database = config["database"]            
        )

        my_cursor = my_db.cursor()

    def __del__(self):
        my_db.commit()

class Student(Database):
    def __init__(self, config):
        super().__init__(config)

    def all_students(self, mode="DESC"):
        sql = "SELECT * FROM students ORDER BY id {}".format(mode)

        try:
            my_cursor.execute(sql)
            result = my_cursor.fetchall()
            return result
        except Exception as e:
            return e

    def delete(self, id):
        sql = "DELETE FROM students WHERE id = {}".format(id)
        try:
            my_cursor.execute(sql)
            print(f"DELETED!")
        except Exception as e:
            raise e

    def insert(self, *data):
        sql = ("INSERT INTO students (name, roll, address) VALUES (%s, %s, %s)")
        try:
            my_cursor.execute(sql, (data))
            print(f'Executed!')
        except Exception as e:
            raise e

        return my_cursor.lastrowid

    def update(self, id, data):
        sql = "UPDATE students SET name = %s, roll = %s, address = %s WHERE id = {}".format(id)
        val = (data[0], data[1], data[2])
        try:
            my_cursor.execute(sql, val)
            print(f"UPDATED!!!")
        except Exception as e:
            return e



    def truncate(self):
        sql = "TRUNCATE TABLE students"
        try:
            my_cursor.execute(sql)
        except Exception as e:
            return e

        return True