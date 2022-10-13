# Предпочтителена функция check_2,
# в ней не используется цикл, поиск в словаре по ключу имеет сложность O(1)


# общая сложность О(N)
def check_1(login, password):
    for key, value in users.items():
        if key == login:
            if value['password'] == password and value['status']:
                return 'Вход выполнен!'
            elif value['password'] != password:
                return 'Неверный пароль!'
            elif value['password'] == password and not value['status']:
                return 'Активируйте профиль!'
    return 'Пользователь не найден'

# общая сложность O(1)
def check_2(login, password):
    if not users.get(login):
        return 'Пользователь не найден!'
    if not users.get(login).get('password') == password:
        return 'Неверный пароль!'
    if not users.get(login).get('status'):
        return 'Активируйте профиль!'
    return 'Вход выполнен!'


users = {'user_1': {'password': 'password_1', 'status': True},
         'user_2': {'password': 'password_2', 'status': False}
         }

print(check_1('user_1', 'password_1'))
print(check_1('user_1', 'pass'))
print(check_1('user_2', 'password_2'))
print(check_1('user', 'password_1'))

print(check_2('user_2', 'password_2'))
print(check_2('user_1', 'password_1'))
print(check_2('user_2', 'pass'))
print(check_2('user', 'password_2'))