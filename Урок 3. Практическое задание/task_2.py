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

from getpass import getpass
import hashlib
import os
from sqlalchemy import Column, Integer, String, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Initialize the database :: Connection & Metadata retrieval
engine = create_engine('sqlite:///tinkoff.sqlite', echo=False)

Base = declarative_base()

class User_db(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    password = Column('password', String)
    salt = Column('salt', BLOB)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Create all tables that do not already exist
        

# SqlAlchemy :: Session setup
session = sessionmaker(bind=engine)
work_session = session()


def create_user():
    while True:
        name = input('Enter your name: ')
        current_user = work_session.query(User_db).filter(User_db.name == name).count()
        if current_user:
            print('This name already use, try another')
        else:
            break
    password = getpass(prompt="New password: ")
    salt = os.urandom(8)
    password_hash = hashlib.pbkdf2_hmac(hash_name='sha256',
                        password=password.encode('utf-8'),
                        salt=salt,
                        iterations = 100000).hex() 
    user = User_db(name=name, password=password_hash, salt=salt)
    work_session.add(user)
    work_session.commit()

def enter():
    name = input('Enter your name: ')
    current_user = work_session.query(User_db).filter(User_db.name == name).one()
    if current_user:
        while True:
            password = getpass(prompt="Enter password for check: ")
            salt = current_user.salt
            password_hash = hashlib.pbkdf2_hmac(hash_name='sha256',
                    password=password.encode('utf-8'),
                    salt=salt,
                    iterations = 100000).hex()
            if password_hash == current_user.password:
                print("You enter right password!")
                break
            else:
                print("You enter wrong password!")

    else:
        print("Unknown user")

Base.metadata.create_all(engine)


while True:
    command = input("Do you want create or just enter exists user? create/enter/exit: ")
    if 'create' in command:
        create_user()  
    elif 'enter' in command:
        enter()
    elif 'exit' in command:
        break
    



