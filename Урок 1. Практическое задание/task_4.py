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

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# O(n^2)
def check_login_1(login, password, database) -> int:
    find_login = False  # O(1)

    for data in database:  # O(n)
        # if data['login'] == login:  # O(1)
        #     find_login = data  # O(1)
        for x in data:  # O(n)
            if x == 'login' and data['login'] == login:
                find_login = data  # O(1)

    if find_login is False:  # O(1)
        return 0  # O(1)

    if find_login['password'] == password:  # O(1)
        if find_login['activated'] is True:  # O(1)
            return 1  # O(1)
        else:  # O(1)
            return 3  # O(1)

    return 0  # O(1)


# O(n)
def check_login_2(login: str, password: str, database: list) -> int:
    match = list(filter(lambda x: x['login'] == login, database))  # O(n)

    if not match:  # O(1)
        return False  # O(1)
    else:  # O(1)
        match = match[0]  # O(1)

    if match['password'] == password:  # O(1)
        if match['activated'] is True:  # O(1)
            return 1  # O(1)
        else:  # O(1)
            return 3  # O(1)

    return 0  # O(1)

# O(1)
def check_login3(user_name: str, user_password: str, users: list) -> int:
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activated']:
            return 1
        elif users[user_name]['password'] == user_password and not users[user_name]['activated']:
            return 3
        elif users[user_name]['password'] != user_password:
            return 0
    else:
        return 0


def result_message(reason):
    if reason == 0:
        return "Мы Вас не знаем... Попробуйте другие комбинации, переберите."
    if reason == 1:
        return "Ура. Успешный вход."
    if reason == 3:
        return "Мы предлагаем Вам - Пройти активацию аккаунта."


def run_application():
    #################
    users = [
        {
            'login': 'masteryoda',
            'password': '123123',
            'activated': True
        },
        {
            'login': 'masteryoda2',
            'password': '123123',
            'activated': True
        },
        {
            'login': 'masteryoda3',
            'password': '123123',
            'activated': False
        }
    ]
    # FIX
    users2 = {
        'masteryoda': {
            'password': '123123',
            'activated': True
        }
    }
    #################
    print("Аутентификация метод 1:")
    print(result_message(check_login_1(input("Введите логин: "), input("Введите пароль: "), users)))

    #################
    print("Аутентификация метод 2:")
    result = check_login_2(input("Введите логин: "), input("Введите пароль: "), users)
    print(result_message(result))

    #################
    print("Аутентификация метод 3:")
    result = check_login3(input("Введите логин: "), input("Введите пароль: "), users2)
    print(result_message(result))


if __name__ == '__main__':
    run_application()
