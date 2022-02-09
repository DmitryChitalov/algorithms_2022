
import sqlite3
from hashlib import sha512
from uuid import uuid4


class Cache:
    def __init__(self):
        self.conn = sqlite3.connect('db_for_algorythm-url.db')
        self.cursor = self.conn.cursor()
        self.salt = uuid4().hex

    def get_hash(self):
        url = input('URL: ')
        res_hash = sha512(url.encode() + self.salt.encode()).hexdigest()
        return url, res_hash

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS urls_unique (
           url_address TEXT NOT NULL UNIQUE PRIMARY KEY,
            url_hash_salted TEXT NOT NULL UNIQUE);
        """)
        self.conn.commit()

# info = cursor.execute('SELECT url_hash_salted FROM urls_unique WHERE url_address = ?', (url,))
# if info.fetchone() is None:
#     cursor.execute("INSERT INTO urls_unique (url_address, url_hash_salted) values (?, ?);", (url, res_hash))
#     conn.commit()
#     print('Данные записаны')
# else:
#     print(info.fetchone())

    def action(self):
        url, res_hash = self.get_hash()
        self.cursor.execute('SELECT url_hash_salted FROM urls_unique WHERE url_address = ?', (url,))
        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT INTO urls_unique (url_address, url_hash_salted) values (?, ?);", (url, res_hash))
            self.conn.commit()
            print('Данные записаны')
        else:
            self.cursor.execute('SELECT url_hash_salted FROM urls_unique WHERE url_address = ?', (url,))
            print(self.cursor.fetchone()[0])
        self.conn.close()


if __name__ == '__main__':
    test_1 = Cache()
    test_1.create_table()
    test_1.action()
