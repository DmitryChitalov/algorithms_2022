"""
Задание 2.
Тут я попробывал связать скрип с базой данных, записывать и извлекать данные из БД получилось, но код получился грамозкий.
Для работы с БД MySQL пришлось установить библиотеку "mysql-connector-python" и установить соеденение.
"""
import mysql.connector
from mysql.connector import Error
from hashlib import pbkdf2_hmac
from binascii import hexlify


def create_connection(host_name, user_name, user_password, db_name):  # Функция для подключения к серверу MySQL
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        # print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_read_query(connection, query):  # Функция для выполнения запросов или ввставки БД
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def gen_pass():
    result = []
    password = input('Введите пароль: ')
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=password.encode('utf-8'),
                      salt=b'pass',
                      iterations=100)
    result.append(str(hexlify(obj)))
    connection = create_connection("localhost", "root", "1212", "user_password")
    insert_values = """
    INSERT INTO user_password.password
    (hesh_password)
    VALUES(%s);
    """
    cursor = connection.cursor()
    cursor.execute(insert_values, result)
    connection.commit()
    connection = create_connection("localhost", "root", "1212", "user_password")
    select_users = "SELECT * from password"
    users = execute_read_query(connection, select_users)
    password_2 = input('Введите повтрно пароль для проверки: ')
    obj_2 = pbkdf2_hmac(hash_name='sha256',
                        password=password_2.encode('utf-8'),
                        salt=b'pass',
                        iterations=100)
    res_2 = str(hexlify(obj_2))
    if any(map(lambda i: res_2 in i, users)):
        return 'Пароль верный!'
    else:
        return 'Пароль не верный!\nПоробуйте еще раз...'


print(gen_pass())

