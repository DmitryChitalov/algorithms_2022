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

class Users:
    def __init__(self):
        self.elems = {}

    def print_elems(self):
        print(self.elems)

    def add_users(self,login,password,activate = True) :
        self.elems[login] = (password,activate)

    def checking_user_access_rights(self,login,password): #O(1)
        user = self.elems.get(login) #O(1)
        if user is None: #O(1)
            return False #O(1)
        if user[0] != password or user[1] != True: #O(1)
            return False #O(1)
        return True #O(1)

class Users_2:
    def __init__(self):
        self.elems = []

    def print_elems(self):
        print(self.elems)

    def add_users(self,login,password,activate = True):
        self.elems.append((login,password,activate))

    def checking_user_access_rights(self,login,password): #O(N)
        for user in self.elems: #O(N)
           if user[0] == login and user[1] == password and user[2] == True: #O(1)
               return True #O(1)

        return False #O(1)

def authentication(users_obj):
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if not users_obj.checking_user_access_rights(login, password):
        print('Для указанного логина и пароля нет активной учетной записи')
        answer = input('Хотите пройти авторизацию? y/n: ')
        if answer.lower() == 'y':
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            users_obj.add_users(login,password)
            print(f'Пользователь {login} был успешно зарегистрирован')
        else:
            return False

    return True


if __name__ == '__main__':

    users_obj = Users()
    #users_obj = Users_2()

    users_obj.add_users('user1', '111')
    users_obj.add_users('user2', '1')
    users_obj.add_users('user3', '2')
    users_obj.add_users('user4', '11')
    if authentication(users_obj):
        print('Доступ разрешен')
    else:
        print('Доступ запрещен.')

"""
ВЫВОДЫ:
Сложность первого решения О(1) - константа, это наилучший показатель. Сложность второго решения О(N) - линейная - это 
хуже чем O(1). Следовательно первый вариант более предпочтителен по быстродействию, что особенно сильно проявится на
большом количестве данных.
"""