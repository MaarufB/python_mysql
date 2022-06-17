from Database import Database, Student
import json
import time

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
    name = "Ma-aruf"
    roll = 505
    address = "Pagadian City"
    data = (name,roll, address)

    for idx in range(0, 5):
        st.insert(name, roll, address)
        time.sleep(0.6)

    students_list = st.all_students()
    print(students_list)
    # st.update(1,data)
    print(f"test")

if __name__ == "__main__":
    main()