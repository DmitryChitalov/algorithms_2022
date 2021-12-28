import sqlite3
from hashlib import sha512
from uuid import uuid4

salt = uuid4().hex

url = input('URL: ')
res_hash = sha512(url.encode() + salt.encode()).hexdigest()
# print(res_hash)

conn = sqlite3.connect('db_for_algorythm_url.db')
cursor = conn.cursor()
print("Подключен к SQLite")

cursor.execute("""CREATE TABLE IF NOT EXISTS urls_unique (
   url_address TEXT NOT NULL UNIQUE PRIMARY KEY,
    url_hash_salted TEXT NOT NULL UNIQUE);
""")
conn.commit()

cursor.execute('SELECT url_hash_salted FROM urls_unique WHERE url_address = ?', (url,))
if cursor.fetchone() is None:
    cursor.execute("INSERT INTO urls_unique (url_address, url_hash_salted) values (?, ?);", (url, res_hash))
    conn.commit()
    print('Данные записаны')
else:
    cursor.execute('SELECT url_hash_salted FROM urls_unique WHERE url_address = ?', (url,))
    print(cursor.fetchone()[0])

conn.close()
