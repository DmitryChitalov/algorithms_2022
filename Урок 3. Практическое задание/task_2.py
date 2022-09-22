import hashlib
import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='root', password='')
cursor = conn.cursor()

DB_NAME = 'user_t'
TABLES = {}
TABLES['user_t'] = (
    "CREATE TABLE 'passwords' ('id' int(20) NOT NULL AUTO_INCREMENT,"
    "'login' varchar(100),"
    "'hash_password' varchar(200),"
    "PRIMARY KEY ('id')"
    ") ENGINE=InnoDB")


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        conn.database = DB_NAME
    else:
        print(err)
        exit(1)


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


def get_hash(login, pwd):
    salt = hashlib.sha256(login.encode('utf-8'))
    hash_obj = hashlib.sha256(pwd.encode('utf-8'))
    hash_pwd = salt.hexdigest() + hash_obj.hexdigest()
    print(f'В базе данных хранится строка: {hash_pwd}')
    return login, hash_pwd


def check_pwd(hash_pwd, count=0):
    pwd = input('Введите пароль еще раз для проверки: ')
    repeat_hash_pwd = get_hash(login, pwd)
    if repeat_hash_pwd == hash_pwd:
        print(f'Вы ввели правильный пароль')
        return write_pwd_to_db(hash_pwd)
    elif count == 3:
        return print(f'Вы ввели неправильный пароль слишком много раз')
    else:
        count += 1
        print('Вы ввели неправильный пароль')
        return check_pwd(hash_pwd, count)


def write_pwd_to_db(hash_pwd):
    query = "INSERT INTO passwords(login, hash_password) VALUES (%s,%s)"
    args = (hash_pwd)
    cursor.execute(query, args)
    conn.commit()
    return print(f'Вы потдвердили регистрацию')


login = input('Введите логин: ')
pwd = input('Введите пароль: ')

conn.commit()
check_pwd(get_hash(login, pwd))
cursor.close()
conn.close()