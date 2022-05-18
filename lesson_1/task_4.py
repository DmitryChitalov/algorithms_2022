"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# Сложность O(n)
def check_1(logins, log_name, log_password):
    for key, value in logins.items():
        if key == log_name:
            if value['password'] == log_password and value['activation'] == 'True':
                return "Доступ есть"
            elif value['password'] == log_password and value['activation'] != "True":
                return "Учетная запись не активна! Пройдите активацию"
            elif value['password'] != log_password:
                return "Пароль неверный! Повторите ввод"
    return "Пользователь не найден!"


# Сложность O(1)
def check_2(logins, log_name, log_password):
    if logins.get(log_name):
        if logins[log_name]['password'] == log_password and logins[log_name]['activation'] == 'True':
            return "Доступ есть"
        elif logins[log_name]['password'] == log_password and logins[log_name]['activation'] != "True":
            return "Учетная запись не активна! Пройдите активацию"
        elif logins[log_name]['password'] != log_password:
            return "Пароль неверный! Повторите ввод"
    return "Пользователь не найден!"


my_dict = {"user1": {
    "password": "123",
    "activation": "True"
}, "user2": {
    "password": "321",
    "activation": "False"}}

print(check_1(my_dict, 'user1', '123'))  # -> Доступ есть
print(check_1(my_dict, 'user2', '123'))  # -> Пароль неверный! Повторите ввод
print(check_1(my_dict, 'user3', '123'))  # -> Пользователь не найден!
print(check_1(my_dict, 'user2', '321'))  # ->Учетная запись не активна! Пройдите активацию

print(check_2(my_dict, 'user1', '123'))  # -> Доступ есть
print(check_2(my_dict, 'user2', '123'))  # -> Пароль неверный! Повторите ввод
print(check_2(my_dict, 'user3', '123'))  # -> Пользователь не найден!
print(check_2(my_dict, 'user2', '321'))  # ->Учетная запись не активна! Пройдите активацию
