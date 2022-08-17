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
users = {'user_1': {'password': '12345', 'active': True},'user_2': {'password': 'qwerty', 'active': False},'user_3': {'password': '2022', 'active': True}}


def user_authorization_1(users, user_name, user_pass): # O(1)
     if users.get(user_name):
         if users[user_name]['password'] == user_pass and users[user_name]['active'] == True:  # O(1)
             return f'Authorization is completed'  # O(1)
         elif users[user_name]['password'] == user_pass and users[user_name]['active'] == False:  # O(1)
             return f'Authorization is failed!'  # O(1)
         elif users[user_name]['password'] != user_pass:  # O(1)
             return f'Password incorrect'
     else:
         return f'{user_name} does not exist'


def user_authorization_2(users, user_name, user_pass): # O(N)
    for user, status in users.items():  # O(N)
        if user == user_name:  # O(1)
            if status['password'] == user_pass and status['active'] == True:  # O(1)
                return f'Authorization is completed'  # O(1)
            elif status['password'] == user_pass and  status['active'] == False:
                return f'Authorization is failed!'  # O(1)
            elif status['password'] != user_pass:  # O(1)
                return f'Password incorrect'
        else:
            return f'{user_name} does not exist'  # O(1)


print(user_authorization_1(users, 'user_2', 'qwerty'))
print(user_authorization_1(users, 'user_3', 'qwerty'))
print(user_authorization_2(users, 'user_1', '12345'))
print(user_authorization_2(users, 'user_4', '2022'))

# Первый алгоритм имеет меньшую сложность, так как поиск по ключу в словаре имеет констатный тип - метод get способен сразу получать значение по ключу без необходимости переборки всего словаря.