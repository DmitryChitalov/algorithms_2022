# import mysql.connector
# from mysql.connector import Error
#
#
# def create_connection(host_name, user_name, user_password, db_name):
#     connect = None
#     try:
#         connect = mysql.connector.connect(
#             host=host_name,
#             user=user_name,
#             passwd=user_password,
#             database=db_name
#         )
#         print("Connection to MySQL DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#     return connect
#
#
# # def create_database(connection, query):
# #     cursor = connection.cursor()
# #     try:
# #         cursor.execute(query)
# #         print("Database created successfully")
# #     except Error as e:
# #         print(f"The error '{e}' occurred")
#
#
# # create_movies_table_query = """
# # CREATE TABLE info_password(
# #     id INT AUTO_INCREMENT PRIMARY KEY,
# #     login VARCHAR(100),
# #     salt VARCHAR(100),
# #     hash VARCHAR(200)
# # )
# # """
#
# insert_movies_query = f"""
# INSERT INTO info_password(login, salt, hash) VALUES
#     ("kir", "my_name", "dfdf")
# """
#
# connection = create_connection("localhost", "root", "12345678", 'sm_app')
# select_movies_query = "SELECT * FROM info_password LIMIT 5"
# with connection.cursor() as cursor:
#     cursor.execute(insert_movies_query)
#     result = cursor.fetchall()
#     for row in result:
#         print(row)
#
# with connection.cursor() as cursor:
#     cursor.execute(select_movies_query)
#     result = cursor.fetchall()
#     for row in result:
#         print(row)
# #create_database_query = "CREATE DATABASE sm_app"
# #create_database(connection, create_database_query)
from binascii import hexlify
import hashlib
import random
import string

def create_hash(passwd, slt):
    hash_ob = hashlib.pbkdf2_hmac(hash_name='sha256', password=passwd.encode(),
                                  salt=b'slt', iterations=1000)
    print(hash_ob)
    return hash_ob

