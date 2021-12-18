#! +
"""
2021-12-18
Geekbrains. Факультет python-разработки
Студент: Папко Роман.
Четверть 1. Алгоритмы и структуры данных на Python. Базовый курс
Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
Домашнее задание 4.
"""
"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""



class User:
    def __init__(self, name, passwd, acti):
        self.name = name
        self.passwd = passwd
        self.acti = acti
        
    def check_name(self, uname):
        if self.name != uname:
            return False
        return True
    
    def check_password(self, password):
        if password != self.passwd:
            return False
        return True
    
    def check_activation(self):
        print(self.name, self.acti)
        if self.acti == 0:
            return False
        return True
    
    def activation(self):
        self.acti = 1
        
    def deactivation(self):
        self.acti = 0

def find_user(lst, uname):
    names = [lst[i].name for i in range(0, len(lst))]  # !!! O(n)
    if username in names:
        return names.index(uname)
    else:
        return False

users = [
    User('u1', 'p1', 1),
    User('u2', 'p2', 0),
    User('u3', 'p3', 1),
    User('u4', 'p4', 1),
    User('u5', 'p5', 0)
    ]


username = 'u3'  # input(f'Enter user name:')
passwd = 'p3'  #input(f'Enter password:')

idx = find_user(users, username)
if idx:
    pass
else:
    print(f'User is not exists')
