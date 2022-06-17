import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    # 'database': 'maarufdb'
}

DB_NAME = "maarufdb"

TABLES = {} 

TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `text` varchar(250) NOT NULL,"
    " `user` varchar(250) NOT NULL,"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)
# db = mysql.connector.connect(**config)
# cursor = db.cursor()

class Database(object):
    def __init__(self):
        self.db = mysql.connector.connect(**config)
        self.cursor = self.db.cursor()

    def get_cursor(self):
        return self.cursor

    def get_db(self):
        return self.db

    # def connect_to_db(self):
    #     db = mysql.connector.connect(**config)
    #     cur = db.cursor()
    #     return cur

    def create_database(self):
        self.cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME)
        )

        print(f"Database {DB_NAME} created!")

    def create_table(self, db_name):
        self.cursor.execute(f"USE {db_name}")

        for table_name in TABLES:
            table_description = TABLES[table_name]

            try:
                print(f"Creating table {table_name}", end="")
                self.cursor.execute(table_description)

            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print(f"Already Exist!")
                else:
                    print(err.msg)


class CrudApp(object):
    config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'maarufdb'
}
    def __init__(self):
        # self.db_config = Database()
        # self.db = self.db_config.get_db()
        # self.cursor = self.db_config.get_cursor()
        self.db = mysql.connector.connect(**self.config)
        self.cursor = self.db.cursor()

    def add_logs(self, text, user):
        sql = ("INSERT INTO logs(text, user) VALUES(%s, %s)")
        self.cursor.execute(sql, (text, user))
        self.db.commit()
        log_id = self.cursor.lastrowid
        print(f"New added logs ({log_id})")

    def get_logs(self):
        sql = ("SELECT * FROM logs ORDER BY created DESC")
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print(f"RESULTS: {len(result)}")
        for row in result:
            print(row[1])

    def get_log(self, id):
        sql = ("SELECT * FROM logs WHERE id = %s")
        self.cursor.execute(sql, (id,))
        result = self.cursor.fetchone()
        # print(f"Results: {len(result)}")
        for row in result:
            print(row)

    def update_logs(self, text, id):
        sql = ("UPDATE logs SET text = %s WHERE id = %s")
        self.cursor.execute(sql, (text, id))
        self.db.commit()
        print("Log updated")

    def delete_logs(self, id):
        sql = ("DELETE FROM logs WHERE id = %s")
        self.cursor.execute(sql, (id,))
        self.db.commit()
        print("Log removed")


if __name__ == '__main__':
    # pass
    # db = Database()
    # db.create_table(DB_NAME)
    app = CrudApp()
    app.get_logs()
    
    # app.create_database()