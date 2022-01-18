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


users_data = {
    'Viktor': {
        'login': 'Viktor',
        'password': 'abra',
        'is_activated': False
    },
    'Peter': {
        'login': 'Peter',
        'password': "abracad",
        'is_activated': False
    },
    'Sara': {
        'login': 'Sara',
        'password': "abracadabra",
        'is_activated': True
    },
    'Ivan': {
        'login': 'Ivan',
        'password': "abracadabra111",
        'is_activated': True
    }
}


def activate_user(user: dict):
    user['is_activated'] = True                  #O(1)
    print(f"{user.get('Login')} , {user}")       #O(1)


def ask_activate():
    print("Ваша учетная запись не активна!")                            #O(1)
    answer = input("Активировать вашу учетную запись? (yes or no):\n")  #O(1)
    if answer == 'yes':                                                 #O(1)
        return True                                                     #O(1)
    else:
        return False                                                    #O(1)

# T(n) =  O(1)
def auth_1(user_name):
    result = users_data.get(user_name)      #O(1)
    return result                           #O(1)

# T(n) =  O(n)
def auth_2(user_name):
    for key, value in users_data.items():    # O(n)
        if key == user_name:                 # O(1)
            result = value                   # O(1)
            return result                    # O(1)


def check_status(user_name):
    #info_user = auth_1(user_name) # 1-ый вариант решения
    info_user = auth_2(user_name)  # 2-ый вариант решения
    if info_user and info_user.get("is_activated"):
        print(f"{info_user.get('login')} ваша учетная запись активна")
    elif info_user and not info_user.get("is_activated"):
        if ask_activate():
            activate_user(info_user)
            return print(f"{info_user.get('login')} ваша учетная запись успешно активирована")
        else:
            return print("Аккаунт не активирован, до свидания!")
    else:
        print(f"{user_name}  Вас нет в базе данных!")
        return False
    return True

print(check_status(input("Ваш логин: ")))
""" Решение с функцией def auth_1(user_name) самое эффективное, так как наименее сложное"""