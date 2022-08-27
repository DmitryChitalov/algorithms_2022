import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        condb = sqlite3.connect('authdatabase.db')
        return condb
    except Error:
        print(Error)


def user_exists(user, condb):
    cursordb = condb.cursor()
    cursordb.execute("SELECT EXISTS (SELECT 1 FROM users WHERE login = ?);", (user,))
    out = cursordb.fetchone()
    return out[0]


def add_user(user, passwd_hash, condb):
    cursordb = condb.cursor()
    cursordb.execute("INSERT INTO users (login, passwdhash) VALUES (?, ?);", (user, passwd_hash))
    condb.commit()


def get_user(user, condb):
    cursordb = condb.cursor()
    cursordb.execute("SELECT login, passwdhash FROM users WHERE login = ?;", (user,))
    user_info = cursordb.fetchone()
    return user_info


# Таблица users
con = sql_connection()
cursordb = con.cursor()
cursordb.execute("""CREATE TABLE IF NOT EXISTS users(
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE,
    passwdhash TEXT);
""")
con.close()
