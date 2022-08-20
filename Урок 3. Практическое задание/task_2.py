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
from sqlite3 import Error
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./users.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
metadata = MetaData()

salt = b'secret_word'


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String,  unique=True)
    password = Column(String)


Base.metadata.create_all(engine)


def login():
    email = input('Введите вашу электронную почту ')
    password = input('Введите ваш пароль для регистрации ')

    try:
        user = Users(email=email,
                     password=pbkdf2_sha256.hash(password, rounds=2, salt=salt))
        session.add(user)
        session.commit()
        session.refresh(user)
        print(f'Пользователь с электронной почтой {email} зарегистрирован')
    except Error as e:
        return e


def verify():
    login_verify = input('Для входа в аккаунт введите ваш логин (эл почту) ')
    current_user = session.query(Users).filter_by(email=login_verify).first()
    if current_user:
        pass_verify = input('Для входа в аккаунт введите ваш пароль ')

        if current_user.password == pbkdf2_sha256.hash(pass_verify, rounds=2, salt=salt):
            print('Добро пожаловать в сервис ')
        else:
            print('Пароль введен не верно')
            verify()
    else:
        print('Пользователь с такой почтой не зарегистрирован ')
        verify()


login()
verify()
