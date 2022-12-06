"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import psycopg2
from hashlib import sha256

con = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="1111", 
  host="127.0.0.1", 
  port="5432"
)

con.cursor().execute('''CREATE TABLE IF NOT EXISTS passwords
(
  hash   VARCHAR(512)
);
commit;''')


def create_hash(password):

    salt = "!@#$"
    hash_obj = sha256(password.encode() + salt.encode())
    result = hash_obj.hexdigest()
    return result
   
def check_pass(password):

    with con:
        curs = con.cursor()
        curs.execute('SELECT hash FROM passwords')
        res = [x[0] for x in curs.fetchall()]
        if hash not in res:
            h = create_hash(password)
            curs.execute(f"INSERT into passwords (hash) VALUES ('{h}'); commit;")
            print(f'В базе данных хранится строка: {h}')
        else:
            print(f'В базе данных хранится строка: {res}')
        pass2 = create_hash(input('Введите пароль еще раз для проверки:'))
        curs.execute('SELECT hash FROM passwords')
        res = [x[0] for x in curs.fetchall()]
        if pass2 in res:
            return 'Вы ввели правильный пароль'
        else:
            return 'Вы ввели неправильный пароль'

print(check_pass(input('Введите пароль:')))
