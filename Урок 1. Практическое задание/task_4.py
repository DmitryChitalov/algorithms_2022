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
user_list = {
    'active': {'admin': 12345678, 'moderator': 87654321, "user": 1234},
    'nonactive': {'user1': 11111, 'user2': 2222, 'user3': 5555555}
}
#Сложность данного алгоритма O(1)

def validation(username, password):
    if username in user_list['active'].keys() and password in user_list['active'].values():
        return f'Login succeful: {username}'
    elif username in user_list['active'] and password not in user_list['active'].values():
        return f'invalid password: {username}'
    elif username not in user_list['active'] or username in user_list['nonactive']:
        return f'"The account is not active! Complete the activation! : {username}'

print(validation('admin',123456786))
print(validation('moderator', 87654321))
print(validation('user1', 11111))
print(validation('dsdfsd', 546435534))

print()

#Сложность данного алгоритма O(n)

def validation1(username, password):
    for key, val in user_list['active'].items():
        if key == username:
            if val == password:
                return f'Login succeful: {username}'
            elif key == username and val != password:
                return f'invalid password: {username}'

    for key, val in user_list['nonactive'].items():
        if key == username:
            if val == password:
                return f'"The account is not active! Complete the activation! : {username}'
            elif key == username and val != password:
                return f'invalid password: {username}'




print(validation1('moderator', 87654321))
print(validation1('moderator', 876543211))
print(validation1('user1', 11111))
print(validation1('user1', 444))