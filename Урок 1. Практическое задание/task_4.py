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


users = {}
'''   id       login  password  is_activate'''
users['1'] = ('first', 'pass1', True)
users['2'] = ('second', 'pass2', False)
users['3'] = ('three', 'pass3', False)

def view_users():
    '''сложность линейная O(N)'''
    print(f'введите номер пользователя для прооверки')
    for id_user, value in users.items():  # O(N)
        login, *_ = value
        print(f'{id_user} {login}')
    id_user = input()
    user = users.get(id_user)  # O(1)
    if user:
        if not user[2]:
            print(f'{user[0]} - вам необходимо пройти активацию')
            question = input(f'Активируем аккаунт {user[0]}? да/нет\n')
            if question.lower() in ['да', 'д', 'y', 'yes']:  # O(N) 
                users[id_user] = (user[0], user[1], True)
                print(f'аккаунт {user[0]} активирован')
            else:
                print(f'Активация не совершена доступ для {user[0]} запрещен')
        else:
            print(f'Добро пожаловать! {user[0]}')
    else:
        print(f'Пользователя под таким номером - {id_user} не существует')

#view_users()

def view_users2():
    '''сложность O(N^2) квадратичная'''
    for user_tup in users.values():
        for val in user_tup:
            if isinstance(val, bool):
                if val == False:
                    print(f'активируйте учетную запись пользователя {user_tup[0]}')
                else:
                    print(f'учетная запись пользователя {user_tup[0]} активирована')
                

view_users2()



def check_user(user):
    if user[2]:
        print(f'пользователь {user[0]} активирован')
    else:
        print(f'пользователь {user[0]} не активирован. Пройдите активацию')


users = list(users.values())


def check_1(users):
    '''сложность константная O(1)'''
    while len(users) > 0:   # O(1)
        user = users.pop()  # O(1)
        check_user(user)   

def check_2(users):
    '''линейная O(N)'''
    for user in users:   # O(N) но т.к. у здесь известно количество пользователей O(1)
        check_user(user)

def check_4(users):
    '''линейно логарифмическая O(N log N)'''
    sorted(users)  # O(N log N)
    print(users)

# check_1(users)
# check_2(users)
# check_4(users)


