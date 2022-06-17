from Database import Database, Student

DB_NAME = "python_mysql"

db_config = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": DB_NAME,
}

def main():
    # db = Database(db_config)
    st = Student(db_config)

    insert_sql = ("INSERT INTO students(`name`, `roll`, `address`) VALUES(`Ma-aaruf`, 505, 'india')")

    st.insert(insert_sql)
    print(f"test")

if __name__ == "__main__":
    main()