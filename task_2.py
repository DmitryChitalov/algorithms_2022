# Дмитрий, решила попробовать сделать через sqlite, так как через CSV уже делала финальное ДЗ по основам,
# захотела попробовать новое.

import sqlite3
from hashlib import sha256

print('Fill in this form to sign-up')
login = input('Login: ')
password = input('Password: ')
res_hash = sha256(login.encode() + password.encode()).hexdigest()
# print(res_hash)

conn = sqlite3.connect('db_for_algorythm.db')
cursor = conn.cursor()
print("Подключен к SQLite")

cursor.execute("""CREATE TABLE IF NOT EXISTS user_data (
   login TEXT NOT NULL UNIQUE PRIMARY KEY,
    password_hash_salted TEXT NOT NULL UNIQUE);
""")
conn.commit()

cursor.execute("INSERT INTO user_data (login, password_hash_salted) values (?, ?);", (login, res_hash))
# Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
conn.commit()

cursor.execute("SELECT password_hash_salted FROM user_data WHERE login = ?", (login,))
result = cursor.fetchall()
print(f'Получили засоленный хэш: {result[0][0]}')

conn.close()


print('Fill in this form to sign-in')
login_check = input('Your login: ')
password_check = input('Your password: ')

check_hash = sha256(login_check.encode() + password_check.encode()).hexdigest()


conn = sqlite3.connect('db_for_algorythm.db')
cursor = conn.cursor()

cursor.execute("SELECT password_hash_salted FROM user_data WHERE login = ?", login_check)
result = cursor.fetchall()

if check_hash == result[0][0]:
    print('You are logged in')
else:
    print('Log-in failed')

conn.close()
