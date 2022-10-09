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


# Решение № 1
# Сложность O(1)

def logIn(login_name, db_dict):
    if login_name in db_dict:  # O (1)
        if db_dict[login_name][1]:  # O(1)
            print('Добро Пожаловать!')
            return True
        else:
            print('Необходимо активировать учетную запись!')
            return False
    else:
        print('Пользователя с таким логином не существует')
        return False


users_db = {
    'login1': ['password1', False],
    'login2': ['password2', True],
    'login3': ['password3', True],
    'login4': ['password4', False],
    'login5': ['password5', False],
    'login6': ['password6', True],
    'login7': ['password7', False],
    'login8': ['password8', True]
}


# logIn('login4', users_db)

# Решение №2
# Сложность O(n)
def logIn_2(login_name, db):
    for i in db:                       # O(n)
        if i[0] == login_name:         # O(1)
            if i[2]:                   # O(1)
                print('Добро пожаловать')  # O(1)
                break

            else:
                print('Необходимо активировать учетную запись!') # O(1)
                break
        elif db.index(i) == len(db) - 1:  # O(1)
            print('Пользователя с таким логином не существует') # O(1)


users = [
    ['login1', 'password1', False],
    ['login2', 'password2', False],
    ['login3', 'password3', True],
    ['login4', 'password4', False],
    ['login5', 'password5', True],
    ['login6', 'password6', False],
    ['login7', 'password7', True],
    ['login8', 'password8', True]
]
logIn_2('login33', users)
