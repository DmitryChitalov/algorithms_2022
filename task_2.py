
import sqlite3
from hashlib import sha256


class GetCheckHash:
    def __init__(self):
        self.conn = sqlite3.connect('db_for_algorythm.db')
        self.cursor = self.conn.cursor()
        # print("Подключен к SQLite")

    @staticmethod
    def get_hash():
        print('Fill in this form to sign-up/sign-in')
        login = input('Login: ')
        password = input('Password: ')
        res_hash = sha256(login.encode() + password.encode()).hexdigest()
        return login, res_hash

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user_data (
        login TEXT NOT NULL UNIQUE PRIMARY KEY,
        password_hash_salted TEXT NOT NULL UNIQUE);
        """)
        # Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
        self.conn.commit()

    def fill_in_table(self):
        login, res_hash = self.get_hash()
        try:
            self.cursor.execute("INSERT INTO user_data (login, password_hash_salted) values (?, ?);", (login, res_hash))
        except sqlite3.IntegrityError:
            print("You've been already signed up")
        else:
            self.conn.commit()
            print("You've been successfully signed up!")

    def check_hash(self):
        login, res_hash = self.get_hash()
        self.cursor.execute("SELECT password_hash_salted FROM user_data WHERE login = ?", (login,))
        result = self.cursor.fetchall()
        # print(f'Получили засоленный хэш: {result[0][0]}')
        self.conn.close()
        if res_hash == result[0][0]:
            print('You are logged in')
        else:
            print('Log-in failed')


if __name__ == '__main__':
    test_1 = GetCheckHash()
    test_1.create_table()
    test_1.fill_in_table()
    test_1.check_hash()
