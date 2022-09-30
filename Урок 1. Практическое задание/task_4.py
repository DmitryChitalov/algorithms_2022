"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
pls check  code below

2) оцените сложность каждого выражения в этих решениях в нотации О-большое
pls check O-notation in code below

3) оцените итоговую сложность каждого решения в нотации О-большое
pls check O-notation in code below

4) сделайте вывод, какое решение эффективнее и почему

def authentication1 is more efficient  O(1)
than
def authentication2     O(N*len(...))

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


def authentication1(auth_data, l=0, p=0):  # O(1)
    if l == 0:  # O(1)
        l_entered = str(input('Please enter Login: '))  # O(1)
        p_entered = str(input('Please enter Password: '))  # O(1)
    else:  # O(1)
        l_entered = l  # O(1)
        p_entered = p  # O(1)

    if auth_data[l_entered][0] == p_entered and auth_data[l_entered][1]:  # O(1)
        return True  # O1()
    else:  # O(1)
        return False  # O(1)


def authentication2(auth_data, l=0, p=0):  # O(N*len(...))
    if l == 0:
        l_entered = str(input('Please enter Login: '))  # O(1)
        p_entered = str(input('Please enter Password: '))  # O(1)
    else:  # O(1)
        l_entered = l  # O(1)
        p_entered = p  # O(1)

    for i in range(0, len(auth_data)):                          # O(N)  list inside
        if (list(auth_data.keys())[i] == l_entered and          # O(len(list))  list
            list(auth_data.values())[i][0] == p_entered and
            list(auth_data.values())[i][1]):                # O(N)
            return True  # O(1)
    return False  # O(1)


if __name__ == '__main__':
    auth_data = {
        'login1': ['password1', 1],
        'login2': ['password2', 1],
        'login3': ['password3', 0],
        'login4': ['password4', 1],
        'login5': ['password5', 1],
        'login6': ['password6', 0],
        'login7': ['password7', 1],
        'login8': ['password8', 1]
    }

    # Authomatic test below
    print('\n Authomatic test for authentication1 script running')
    logins_set = sorted(set(auth_data.keys()))
    passw_lst = list(auth_data.values())
    for l in logins_set:
        for p in passw_lst:
            pswrd = p[0]
            print(f'Login : {l}  , password = {pswrd} , Authentication = {authentication1(auth_data, l, pswrd)} ')

    # Authomatic test below
    print('\n Authomatic test for authentication2 script running')
    logins_set = sorted(set(auth_data.keys()))
    passw_lst = list(auth_data.values())
    for l in logins_set:
        for p in passw_lst:
            pswrd = p[0]
            print(f'Login : {l}  , password = {pswrd} , Authentication = {authentication2(auth_data, l, pswrd)} ')

# Manual test below
#     print('\n authentication1 script running')
#     print(authentication1( auth_data ))     # False / True
#     print('\n authentication2 script running')
#     print(authentication2( auth_data ))     # False / True


# Script results are below :
# Authomatic test for authentication1 script running
# Login : login1  , password = password1 , Authentication = True
# Login : login1  , password = password2 , Authentication = False
# Login : login1  , password = password3 , Authentication = False
# Login : login1  , password = password4 , Authentication = False
# Login : login1  , password = password5 , Authentication = False
# Login : login1  , password = password6 , Authentication = False
# Login : login1  , password = password7 , Authentication = False
# Login : login1  , password = password8 , Authentication = False
# Login : login2  , password = password1 , Authentication = False
# Login : login2  , password = password2 , Authentication = True
# Login : login2  , password = password3 , Authentication = False
# Login : login2  , password = password4 , Authentication = False
# Login : login2  , password = password5 , Authentication = False
# Login : login2  , password = password6 , Authentication = False
# Login : login2  , password = password7 , Authentication = False
# Login : login2  , password = password8 , Authentication = False
# Login : login3  , password = password1 , Authentication = False
# Login : login3  , password = password2 , Authentication = False
# Login : login3  , password = password3 , Authentication = False
# Login : login3  , password = password4 , Authentication = False
# Login : login3  , password = password5 , Authentication = False
# Login : login3  , password = password6 , Authentication = False
# Login : login3  , password = password7 , Authentication = False
# Login : login3  , password = password8 , Authentication = False
# Login : login4  , password = password1 , Authentication = False
# Login : login4  , password = password2 , Authentication = False
# Login : login4  , password = password3 , Authentication = False
# Login : login4  , password = password4 , Authentication = True
# Login : login4  , password = password5 , Authentication = False
# Login : login4  , password = password6 , Authentication = False
# Login : login4  , password = password7 , Authentication = False
# Login : login4  , password = password8 , Authentication = False
# Login : login5  , password = password1 , Authentication = False
# Login : login5  , password = password2 , Authentication = False
# Login : login5  , password = password3 , Authentication = False
# Login : login5  , password = password4 , Authentication = False
# Login : login5  , password = password5 , Authentication = True
# Login : login5  , password = password6 , Authentication = False
# Login : login5  , password = password7 , Authentication = False
# Login : login5  , password = password8 , Authentication = False
# Login : login6  , password = password1 , Authentication = False
# Login : login6  , password = password2 , Authentication = False
# Login : login6  , password = password3 , Authentication = False
# Login : login6  , password = password4 , Authentication = False
# Login : login6  , password = password5 , Authentication = False
# Login : login6  , password = password6 , Authentication = False
# Login : login6  , password = password7 , Authentication = False
# Login : login6  , password = password8 , Authentication = False
# Login : login7  , password = password1 , Authentication = False
# Login : login7  , password = password2 , Authentication = False
# Login : login7  , password = password3 , Authentication = False
# Login : login7  , password = password4 , Authentication = False
# Login : login7  , password = password5 , Authentication = False
# Login : login7  , password = password6 , Authentication = False
# Login : login7  , password = password7 , Authentication = True
# Login : login7  , password = password8 , Authentication = False
# Login : login8  , password = password1 , Authentication = False
# Login : login8  , password = password2 , Authentication = False
# Login : login8  , password = password3 , Authentication = False
# Login : login8  , password = password4 , Authentication = False
# Login : login8  , password = password5 , Authentication = False
# Login : login8  , password = password6 , Authentication = False
# Login : login8  , password = password7 , Authentication = False
# Login : login8  , password = password8 , Authentication = True
#
#  Authomatic test for authentication2 script running
# Login : login1  , password = password1 , Authentication = True
# Login : login1  , password = password2 , Authentication = False
# Login : login1  , password = password3 , Authentication = False
# Login : login1  , password = password4 , Authentication = False
# Login : login1  , password = password5 , Authentication = False
# Login : login1  , password = password6 , Authentication = False
# Login : login1  , password = password7 , Authentication = False
# Login : login1  , password = password8 , Authentication = False
# Login : login2  , password = password1 , Authentication = False
# Login : login2  , password = password2 , Authentication = True
# Login : login2  , password = password3 , Authentication = False
# Login : login2  , password = password4 , Authentication = False
# Login : login2  , password = password5 , Authentication = False
# Login : login2  , password = password6 , Authentication = False
# Login : login2  , password = password7 , Authentication = False
# Login : login2  , password = password8 , Authentication = False
# Login : login3  , password = password1 , Authentication = False
# Login : login3  , password = password2 , Authentication = False
# Login : login3  , password = password3 , Authentication = False
# Login : login3  , password = password4 , Authentication = False
# Login : login3  , password = password5 , Authentication = False
# Login : login3  , password = password6 , Authentication = False
# Login : login3  , password = password7 , Authentication = False
# Login : login3  , password = password8 , Authentication = False
# Login : login4  , password = password1 , Authentication = False
# Login : login4  , password = password2 , Authentication = False
# Login : login4  , password = password3 , Authentication = False
# Login : login4  , password = password4 , Authentication = True
# Login : login4  , password = password5 , Authentication = False
# Login : login4  , password = password6 , Authentication = False
# Login : login4  , password = password7 , Authentication = False
# Login : login4  , password = password8 , Authentication = False
# Login : login5  , password = password1 , Authentication = False
# Login : login5  , password = password2 , Authentication = False
# Login : login5  , password = password3 , Authentication = False
# Login : login5  , password = password4 , Authentication = False
# Login : login5  , password = password5 , Authentication = True
# Login : login5  , password = password6 , Authentication = False
# Login : login5  , password = password7 , Authentication = False
# Login : login5  , password = password8 , Authentication = False
# Login : login6  , password = password1 , Authentication = False
# Login : login6  , password = password2 , Authentication = False
# Login : login6  , password = password3 , Authentication = False
# Login : login6  , password = password4 , Authentication = False
# Login : login6  , password = password5 , Authentication = False
# Login : login6  , password = password6 , Authentication = False
# Login : login6  , password = password7 , Authentication = False
# Login : login6  , password = password8 , Authentication = False
# Login : login7  , password = password1 , Authentication = False
# Login : login7  , password = password2 , Authentication = False
# Login : login7  , password = password3 , Authentication = False
# Login : login7  , password = password4 , Authentication = False
# Login : login7  , password = password5 , Authentication = False
# Login : login7  , password = password6 , Authentication = False
# Login : login7  , password = password7 , Authentication = True
# Login : login7  , password = password8 , Authentication = False
# Login : login8  , password = password1 , Authentication = False
# Login : login8  , password = password2 , Authentication = False
# Login : login8  , password = password3 , Authentication = False
# Login : login8  , password = password4 , Authentication = False
# Login : login8  , password = password5 , Authentication = False
# Login : login8  , password = password6 , Authentication = False
# Login : login8  , password = password7 , Authentication = False
# Login : login8  , password = password8 , Authentication = True
#
# Process finished with exit code 0
