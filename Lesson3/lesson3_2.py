import pymysql.cursors
from uuid import uuid4
import hashlib
from binascii import hexlify

conn = pymysql.connect(host='localhost', user='root', password='Rexema_4082', database='password_hash')
cursor = conn.cursor()
pswd = input('Введите пароль: ')
salt = uuid4().hex
salt = 'my_salt'
res = hashlib.sha256(salt.encode() + pswd.encode()).hexdigest()
print(res)
cursor.execute(f'INSERT INTO users (password_hash) VALUES ("{res}")')
conn.commit()


def check():
    conn = pymysql.connect(host='localhost', user='root', password='Rexema_4082', database='password_hash')
    cursor = conn.cursor()
    pswd = input('Введите пароль: ')
    salt = uuid4().hex
    salt = 'my_salt'
    res = hashlib.sha256(salt.encode() + pswd.encode()).hexdigest()
    print(res)
    cursor.execute("SELECT password_hash FROM users")
    result = cursor.fetchall()
    for x in result:
        x = str(x).replace("'", "").replace('(', "").replace(")", "").replace(",", "")

        if res in x:
            print(f'В базе данных хранится строка: {x} ')


check()
