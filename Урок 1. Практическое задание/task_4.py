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
# Общая сложность O(N)
def authorization_f(users, user_name, user_password):
    for key, value in users.items(): # O(N)
        if key == user_name: # O(1)
            if value['password'] == user_password and value['activation']: # O(1)
                return "Добро пожаловать! Доступ к ресурсу предоставлен" # O(1)
            elif value['password'] == user_password and not value['activation']: # O(1)
                return "Учетная запись не активна! Пройдите активацию!" # O(1)
            elif value['password'] != user_password: # O(1)
                return "Пароль не верный" # O(1)

    return "Данного пользователя не существует" # O(1)


# общая сложность O(1)
def authorization_s(users, user_name, user_password):
    if users.get(user_name): # O(1)
        if users[user_name]['password'] == user_password and users[user_name]['activation']: # O(1)
            return "Добро пожаловать! Доступ к ресурсу предоставлен" # O(1)
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']: # O(1)
            return "Учетная запись не активна! Пройдите активацию!" # O(1)
        elif users[user_name]['password'] != user_password: # O(1)
            return "Пароль не верный" # O(1)
    else:
        return "Данного пользователя не существует" # O(1)


"""
Вторая реализация будет намного эффективнее, 
так как в ней не используется цикл, 
поиск в словаре по ключу имеет сложность - O(1)
"""


my_users = {'user1': {'password': '11111', 'activation': True},
            'user2': {'password': '11111', 'activation': False},
            'user3': {'password': '11111', 'activation': True},
            'user4': {'password': '11111', 'activation': False}
            }

print(authorization_s(my_users, 'user11', '11111'))
print(authorization_f(my_users, 'user6', '1111'))
