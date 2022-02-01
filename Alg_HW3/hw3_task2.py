import mysql.connector
from mysql.connector import Error
from binascii import hexlify
import hashlib
import random
import string


def create_connection(host_name, user_name, user_password, db_name):
    connect = None
    try:
        connect = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connect


def insert_to_db(connect, login, salt, hash_ob):
    insert_info_query = f"""
    INSERT INTO info_password(login, salt, hash) VALUES
        ("{login}", "{salt}", "{hexlify(hash_ob)}")
    """
    with connect.cursor() as cursor:
        cursor.execute(insert_info_query)
        connect.commit()
    print(f'В базе данных хранится строка {hexlify(hash_ob)}')


def get_from_db(login, connect):
    select_password_query = f"""
SELECT salt, hash FROM info_password
where login = '{login}';
"""
    with connect.cursor() as cursor:
        cursor.execute(select_password_query)
        result = cursor.fetchall()
    return result


def create_hash(passwd, slt):
    hash_ob = hashlib.pbkdf2_hmac(hash_name='sha256', password=passwd.encode(),
                                  salt=slt.encode(), iterations=1000)
    return hash_ob


def generate_random_salt(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_hash(login: str, connect):
    password = input('Введите пароль')
    salt = generate_random_salt(12)
    hash_object = create_hash(password, salt)
    insert_to_db(connect, login, salt, hash_object)


def check_hash(login, connect):
    password = input('Введите пароль еще раз ')
    res = get_from_db(login, connect)
    salt, hash_object = res[0]
    hash_calc = create_hash(password, salt)
    if hash_object == str(hexlify(hash_calc)):
        print('Вы ввели правильный пароль!')
    else:
        print('Пройдите процедуру заново')


connection = create_connection("localhost", "root", "12345678", 'sm_app')
generate_hash('kirilica', connection)
check_hash('kirilica', connection)
