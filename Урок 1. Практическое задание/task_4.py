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

dict_users = {'user1': {'password': '1', 'activation': True},
              'user2': {'password': '11', 'activation': False},
              'user3': {'password': '111', 'activation': True},
              'user4': {'password': '1111', 'activation': False},
              'user5': {'password': '11111', 'activation': True}
              }


# 1 вариант. O(1)
def check_user(users, name, password):
    if users.get(name):  # O(1)
        if users[name]['password'] == password and users[name]['activation'] == True:  # O(1)
            return 'Доступ разрешен'  # O(1)
        if users[name]['password'] == password and users[name]['activation'] == False:  # O(1)
            return 'Пройдите активацию'  # O(1)
        if users[name]['password'] != password:  # O(1)
            return 'Не верный пароль'  # O(1)
    else:  # O(1)
        return 'Пользователь не найден'  # O(1)


print(check_user(dict_users, 'user1', '1'))  # O(1)
print(check_user(dict_users, 'user2', '11'))  # O(1)
print(check_user(dict_users, 'user2', '111'))  # O(1)
print(check_user(dict_users, 'user8', '1111'))  # O(1)


# Долго не мог убрать "None" когда вводишь не верный логин...В разборе дз увидел что "else" у меня не там стоял...


# 2 вариант. O(n)
def check_user2(users, name, password):
    for key, value in users.items():  # O(n)
        if key == name:  # O(1)
            if key == name and password == value['password'] and value['activation'] == True:  # O(1)
                return 'Доступ разрешен'  # O(1)
            if key == name and password == value['password'] and value['activation'] == False:  # O(1)
                return 'Пройдите активацию'  # O(1)
            if value['password'] != password:  # O(1)
                return 'Не верный пароль'  # O(1)
    return 'Пользователь не найден'  # O(1)


print(check_user2(dict_users, 'user1', '1'))  # O(1)
print(check_user2(dict_users, 'user2', '11'))  # O(1)
print(check_user2(dict_users, 'user2', '111'))  # O(1)
print(check_user2(dict_users, 'user8', '1111'))  # O(1)

# Первый вариант быстрее и эффективнее т.к. нет цикла. Проверяется не каждый элемент(как во втором варианте) словаря,
# а только значения, соответствующие ключу...
