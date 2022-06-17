import mysql.connector
from mysql.connector import Error
from mysql.connector import (connection)


name = input("Enter Product Name: ")
desc = input("Enter Product Description: ")
price = input("Enter Product Price: ")
qty = input("Enter Product Quantity: ")

try:
    con = mysql.connector.connect(
                                    host="localhost", 
                                    database="db_products", 
                                    user="root",
                                    password="")

    query = f"INSERT INTO tbl_products(NAME, DESCRIPTION, PRICE, QUANTITY) VALUES('"+ name +"', '"+ desc \
        +"', '"+ price +"', '"+ qty +"')"

    cur = con.cursor()
    cur.execute(query)
    con.commit()
    cur.close()

except Error as error:
    print(f"Insert data failed {error}")
finally:
    if con.is_connected():
        con.close()
        print(f"MySQL Connection is now CLOSED!")
