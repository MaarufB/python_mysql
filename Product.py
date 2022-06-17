import mysql.connector
from mysql.connector import Error
import argparse

class ProductClass(object):
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect_to_db(self):
        try:
            con = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user = self.user,
                password = self.password
            )
        except Error as error:
            print(f"Cannot connect to the database! {error}")
        finally:
            print(f"Successfully connected to the database!!")
        
        return con

    def close_connection(self):
        pass

    def insert_to_db(self, query):
        try:
            con = self.connect_to_db()
            cur = con.cursor()
            cur.execute(query)
            con.commit()
            cur.close()

        except Error as error:
            print(f"Cannot insert to the database!! {error}")
        finally:
            print(f"Successfully added to the database")
            con.close()
        # pass

    def update(self):
        pass

    def delete(self):
        pass

    def get_product(self):
        pass


if __name__ == "__main__":
    par = argparse.ArgumentParser()
    par.add_argument('--name', default="Test2")
    par.add_argument('--desc', default="Desc test")
    par.add_argument('--price', default=10.2, type=float)
    par.add_argument('--qty', default=10, type=int)

    params = par.parse_args()
    
    name = params.name
    desc = params.desc
    price = params.price
    qty = params.qty


    product = ProductClass(
                            host="localhost", 
                            database="db_products", 
                            user="root",
                            password="")

    query =  f"INSERT INTO tbl_products(NAME, DESCRIPTION, PRICE, QUANTITY) VALUES('"+ name +"', '"+ desc \
        +"', '"+ str(price) +"', '"+ str(qty) +"')"

    product.insert_to_db(query)

