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


# O(n) - Линейная
def authorization_one(user, password):
    for k, v in my_dict.items():
        if k == user:
            if v['password'] == password and v['activation']:
                return 'Учетная запись активирована.'
            elif v['password'] == password and not v['activation']:
                return 'Учетная запись не активирована. Необходимо пройти активацию.'
            elif v['password'] != password:
                return 'Введен неверный пароль.'
    return 'Такого пользователя не существует'


# O(1) - Константная
def authorization_two(user, password):
    if my_dict.get(user):
        if my_dict[user]['password'] == password and my_dict[user]['activation']:
            return 'Учетная запись активирована.'
        elif my_dict[user]['password'] == password and not my_dict[user]['activation']:
            return 'Учетная запись не активирована. Необходимо пройти активацию.'
        elif my_dict[user]['password'] != password:
            return 'Введен неверный пароль.'
    return 'Такого пользователя не существует'


my_dict = {
    'lolo': {'password': '123456', 'activation': True},
    'toto': {'password': '123789', 'activation': False},
    'wewe': {'password': '456987', 'activation': True},
    'lili': {'password': '789654', 'activation': False},
    'jiji': {'password': '147852', 'activation': True}
}

print('\nРешение №2 будет более быстрым, т.к. имеет константную сложность.\n')

print(authorization_one('lolo', '123456'))
print(authorization_one('toto', '123789'))
print(authorization_one('wewe', '123456'))
print(authorization_one('coco', '123456'))

print(f'\n{"*" * 50}\n')

print(authorization_two('lolo', '123456'))
print(authorization_two('toto', '123789'))
print(authorization_two('wewe', '123456'))
print(authorization_two('coco', '123456'))