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

from hashlib import sha256
import sqlite3

class Database(object):
    """ Класс для определения временной базы данных

    Methods:
        generate_hash   -> str  : Статический метод. Генерирует хеш пароля из введённых логина и пароля. Возвращает логин и хеш пароля.
        add_user        -> None : Проверяет введённый логин на наличие в базе данных. В случае отсутствия вносит в БД.
        check_user      -> str  : Проверяет наличие введённого логина в БД и сравнивает хеш пароля в БД с хешем введённого пароля.

    """

    def __init__(self) -> None:
        # Инициализировать объект класса Database, создать временную БД и добавить в неё таблицу.
        self.__database = sqlite3.connect("file:users.db?mode=memory")
        self.__cursore = self.__database.cursor()
        self.__create_db()

    def __create_db(self) -> None:
        # Создать таблицу
        self.__cursore.execute("""
            CREATE TABLE IF NOT EXISTS HashesTable (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login VARCHAR(255) NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                UNIQUE(login));
            """
            )
        self.__database.commit()
        print(f"В оперативной памяти инициализирована тестовая база данных.\nСоздана таблица \"{self.__get_tables_name()}\".")

    @staticmethod
    def generate_hash() -> str:
        # Сгенерировать хешь пароля из введённых логина и пароля.
        login: str = input("Введите логин: ")
        password: str = input("Введите пароль: ")
        return login, sha256(login.encode() + password.encode()).hexdigest()

    def add_user(self) -> None:
        # Добавить пользователя в БД при отсутствии.
        print("\nДобавление пользователя в таблицу:")
        login, password_hash = self.generate_hash()
        if not self.__cursore.execute(f"SELECT login FROM HashesTable WHERE login = ?", (login,)).fetchone():
            self.__cursore.execute(f"INSERT INTO HashesTable (login, password_hash) VALUES (?, ?);", (login, password_hash,))
            self.__database.commit()
            print(f"В базу данных записан пользователь: \"{login}\" с хешем пароля: {password_hash}")
        else:
            self.__cursore.rollback()
            print("Пользователь с таким логином уже существует.")

    def check_user(self) -> str:
        # Проверить пользователя на наличие в БД и верности введённого пароля.
        print("\nПроверка пользователя.")
        login, password_hash = self.generate_hash()
        user = self.__cursore.execute(f"SELECT login, password_hash FROM HashesTable WHERE login=?", (login,)).fetchone()
        if user:
            if user[1] == password_hash:
                return "Введён верный пароль."
            return "Введён неверный пароль."
        return "Пользователь отсутствует в системе."

    def __get_tables_name(self) -> str:
        # Получить имя таблицы.
        table = self.__cursore.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';").fetchone()
        if table:
            return table[0]
        return "База пуста."

    def __del__(self) -> None:
        # Закрыть соединение с БД и удалить объект.
        self.__database.close()
        print("\nБД удалена.")

if __name__ == "__main__":

    database = Database()
    print(database.__doc__)
    database.add_user()
    print(database.check_user())
    print(database.check_user())
    print(database.check_user())
    del database

#############################
#                           #
#  Пример работы программы  #
#                           #
#############################

# В оперативной памяти инициализирована тестовая база данных.
# Создана таблица "HashesTable".

# Добавление пользователя в таблицу:
# Введите логин: Пользователь
# Введите пароль: йцукен123
# В базу данных записан пользователь: "Дмитрий" с хешем пароля: bdc56fdd2f3d408543602ed0a9a4bc65ed04a8121f687c785afd7266574d12b4

# Проверка пользователя.
# Введите логин: Пользователь
# Введите пароль: йцукен123
# Введён верный пароль.

# Проверка пользователя.
# Введите логин: Йцукен
# Введите пароль: Пользователь
# Пользователь отсутствует в системе.

# Проверка пользователя.
# Введите логин: Пользователь
# Введите пароль: йцукен
# Введён неверный пароль.

# БД удалена.