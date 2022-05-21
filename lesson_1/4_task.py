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

users_data = {'user_01': ['passwd_01', 1], 'user_02': ['passwd_02', 0], 'user_03': ['passwd_03', 0],
              'user_o4': ['passwd_03', 1], 'user_05': ['passwd_05', 1], 'user_06': ['passwd_05', 1]}

# Сложность O(1)
def authentication_s():
    login = input('Enter your login: ')  # O(1)
    passwd = input('Enter your password: ')  # O(1)
    try:
        if users_data[login][0] == passwd:  # O(1)
            if users_data[login][1] == 1:  # O(1)
                print(f"You're welcome, {login}")  # O(1)
            elif users_data[login][1] != 1:  # O(1)
                print(f"{login}, you need to activate your account")  # O(1)
                while True:
                    act = input("Enter yes if you agreed to activate your account, else enter any letter ")  # O(1)
                    if act.lower() != 'yes':  # O(1)
                        break
                    elif act.lower() == 'yes':  # O(1)
                        users_data[login][1] = 1  # O(1)
                        print('Your account has been activated successfully')  # O(1)
                        break
        else:
            print('Incorrect password, try again.')  # O(1)
    except KeyError:
        print("User doesn't exist")  # O(1)


# Сложность: O(n)
def authentication_f():
    login = input('Enter your login: ')  # O(1)
    passwd = input('Enter your password: ')  # O(1)
    if login in users_data.keys() and passwd == users_data[login][0]:  # O(n)
        if users_data[login][1] == 1:  # O(1)
            print(f"You're welcome, {login}")  # O(1)
        elif users_data[login][1] != 1:  # O(1)
            print(f"{login}, you need to activate your account")  # O(1)
            while True:
                act = input("Enter yes if you agreed to activate your account, else enter any letter ")  # O(1)
                if act.lower() != 'yes':  # O(1)
                    break
                elif act.lower() == 'yes':  # O(1)
                    users_data[login][1] = 1  # O(1)
                    print('Your account has been activated successfully')  # O(1)
                    break
    else:
        print('Incorrect user`s login or password')  # O(1)


authentication_s()
