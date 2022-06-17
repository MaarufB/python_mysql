from mysql.connector import (connection)

cnx = connection.MySQLConnection(host="localhost", 
                                    database="db_products", 
                                    user="root",
                                    password="")
cnx.close()