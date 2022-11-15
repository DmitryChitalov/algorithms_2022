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

users = {
        'user_1': {'password': 'password_1', 'active': True},
        'user_2': {'password': 'password_2', 'active': False},
        'user_3': {'password': 'password_3', 'active': False},
        'user_4': {'password': 'password_4', 'active': True},
        'user_5': {'password': 'password_5', 'active': False},
        'user_6': {'password': 'password_6', 'active': True}
    }

def authentication_1(user): # Общая скорость выполнения O(n)
    print("authentication_1:")
    if user in users:                                       # O(n)
        if users[user]['active']:                           # O(1)
            if input("Password: ") == users[user]['password']: # O(1)
                return 'Access is allowed.'                             # O(1)                                              # O(1)
            return 'Access is denied.'                                  # O(1)
        return 'Activate your account!'                                 # O(1)
    return 'User not registered.'                                       # O(1)

def authentication_2(user): # Общая скорость выполнения O(n)
    print("\nauthentication_2:")
    for key, value in users.items():                                    # O(n)
        if user == key:                                                 # O(1)
            if value['active']:                                         # O(1)
                if input("Password: ") != value['password']:            # O(1)
                    return 'Access is denied.'                          # O(1)
                return 'Access is allowed.'                             # O(1)
            return 'Activate your account!'                             # O(1)
    return 'User not registered.'                                       # O(1)

def authentication_3(user): # Общая скорость выполнения O(1)
    print("\nauthentication_2:")
    try:                                                            # O(1)
        data = users[user]                                          # O(1)
        if data['active']:                                          # O(1)
            if data['password'] != input("Password: "):             # O(1)
                return 'Access is denied.'                          # O(1)
            return 'Access is allowed.'                             # O(1)
        return 'Activate your account!'                             # O(1)
    except KeyError as err:
        return 'User not registered.' 

# Скорость выполнения третьеё функции быстрее, 
# так как отсутствует необходимость в переборе элементов.

if __name__ == '__main__':

    user = input("Username: ")
    print('\n')
    print(authentication_1(user))
    print(authentication_2(user))
    print(authentication_3(user))
