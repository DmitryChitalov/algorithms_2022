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
# Cложность O(n)
def access_verification1(users, user_name, user_password):
    for key, value in users.items():                                                 # O(N)
        if key == user_name:                                                         # O(N) 
            if value['password'] == user_password and value['activation']:           # O(N)
                return "Access granted."                                             # O(1)
            elif value['password'] == user_password and not value['activation']:     # O(N)
                return "Please activate your account."                               # O(1) 
            elif value['password'] != user_password:                                 # O(N)
                return "It's a wrong password."                                      # O(1)

    return "Invalid username"                                                        # O(1)


# Cложность O(1)
def access_verification2(users, user_name, user_password):
    if users.get(user_name):                                                                         # O(1)
        if users[user_name]['password'] == user_password and users[user_name]['activation']:         # O(1)
            return "Access granted."                                                                 # O(1)
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:   # O(1)
            return "Please activate your account."                                                   # O(1)
        elif users[user_name]['password'] != user_password:                                          # O(1)
            return "It's a wrong password."                                                          # O(1)
    else:
        return "Invalid username"                                                                    # O(1)

# Второе решение более эффективно, так как имеет сложность О(1)



users_db = {'user1': {'password': '1234', 'activation': False},
            'user2': {'password': '2345', 'activation': True,
            'user3': {'password': '3456', 'activation': True},
            'user4': {'password': '4567', 'activation': False}
            }

print(access_verification1(users_db, 'user4', '4567'))
print(access_verification2(users_db, 'user1', 'buytr'))
