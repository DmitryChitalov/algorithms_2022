"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
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
import hashlib
import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///client.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, fullname, password):
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.fullname, self.password)


def get_client_by_username(username):
    """Получение клиента по имени"""
    client = session.query(User.fullname).filter(
        User.fullname == username).first()
    list_cl_name = list(client)[0]
    return list_cl_name


def enter_password(cl_password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', cl_password.encode('utf-8'), salt, 100000)
    storage = salt + key
    return storage


def get_password_by_username(username):
    """Получение пароля по имени"""
    client_password = session.query(User.password).filter(
        User.fullname == username).first()
    list_storage = list(client_password)[0]

    salt_from_storage = list_storage[:32]
    key_from_storage = list_storage[32:]  # 32 является длиной соли
    return salt_from_storage, key_from_storage


def authenticate():
    """ Проверка паароля """
    user = input('Выберите пользователя: Vasiliy Pypkin, Kolia Kola, Zina Korzina: ')
    inp_password = input('Введите пароль: ')
    salt, old_key = get_password_by_username(user)
    print('В базе данных хранится строка: ', old_key)
    inp_password = input('Введите пароль еще раз для проверки: ')
    key = hashlib.pbkdf2_hmac('sha256', inp_password.encode('utf-8'), salt, 100000)
    if key == old_key:
        print('Вы ввели правильный пароль.')
    else:
        print('Пароль неверный.')


# Создание таблицы
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
vasiaUser = User("Vasiliy Pypkin", enter_password("123"))

session.add(vasiaUser)
session.add_all([User("Kolia Kola", enter_password("123")), User("Zina Korzina", enter_password("123"))])
session.commit()

if __name__ == '__main__':
    authenticate()
