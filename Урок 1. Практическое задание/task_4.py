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
def authorization_1(users, name, password):
    """
    Сложность: O(N)
    """
    for key, value in users.items():
        if key == name:
            if value['password'] != password:
                return "Не верный пароль!"
            elif not value['activation']:
                return "Учетная запись не активирована! Пройдите активацию!"
            else:
                return "Ресурс предоставлен"


    return "Пользователь с данной учетной записью не существует!"


def authorization_2(users, name, password):
    """
    Сложность: O(1)
    """
    if users.get(name):
        if users[name]['password'] != password:
            return "Не верный пароль!"
        elif not users[name]['activation']:
            return "Учетная запись не активирована! Пройдите активацию!"
        else:
            return "Ресурс предоставлен"
    else:
        return "Пользователь с данной учетной записью не существует!"

users1 = {
    'user1': {'password': '111', 'activation': True},
    'user2': {'password': '222', 'activation': True},
    'user3': {'password': '333', 'activation': False}
}

print(authorization_1(users1, 'user1', '111'))
print(authorization_1(users1, 'user1', '222'))
print(authorization_1(users1, 'user3', '333'))
print(authorization_1(users1, 'user4', '444'))

print(authorization_2(users1, 'user1', '111'))
print(authorization_2(users1, 'user1', '222'))
print(authorization_2(users1, 'user3', '333'))
print(authorization_2(users1, 'user4', '444'))