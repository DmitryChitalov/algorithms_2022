

# Общая сложность O(n)
def authorization_f(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Добро пожаловать! Доступ к ресурсу предоставлен"
            elif value['password'] == user_password \
                    and not value['activation']:
                return "Учетная запись не активна! Пройдите активацию!"
            elif value['password'] != user_password:
                return "Пароль не верный"

    return "Данного пользователя не существует"


# общая сложность O(1)
def authorization_s(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password \
                and users[user_name]['activation']:
            return "Добро пожаловать! Доступ к ресурсу предоставлен"
        elif users[user_name]['password'] == user_password \
                and not users[user_name]['activation']:
            return "Учетная запись не активна! Пройдите активацию!"
        elif users[user_name]['password'] != user_password:
            return "Пароль не верный"
    else:
        return "Данного пользователя не существует"


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

print(authorization_s(my_users, 'user6', '1111'))
print(authorization_f(my_users, 'user6', '1111'))
