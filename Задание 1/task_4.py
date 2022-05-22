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

dict_user = {'login1': ['1234', False], 'login2': ['134', False], 'login3': ['234', True], 'login4': ['1234', False]}

def check_user_1(dict_user, login_in, pass_in): # O(n)
# последовательно проверить для каждого пользователя    
    for login in dict_user.keys(): # O(n)
        if login == login_in: # O(1)
            if dict_user[login][1]: # O(1)
                if dict_user[login][0] == pass_in: # O(1)
                    return 'Допущен' # O(1)
                else:
                    return 'Ошибка в логине или пароле' # O(1)
            else:
                return 'Активируйте аккаунт' # O(1)
    return 'Неизвестный логин' # O(1)

print(check_user_1(dict_user, '', ''))
print(check_user_1(dict_user, 'login1', ''))
print(check_user_1(dict_user, 'login3', ''))
print(check_user_1(dict_user, 'login3', '234'))

##########################

def check_user_2(dict_user, login_in, pass_in): # O(n**2)
    for login in dict_user.keys(): # O(n)
        if login == login_in: # O(1)
            for item in dict_user.items():
                if item[0] == login:
                    if item[1][1]:
                        if item[1][0] == pass_in:
                            return 'Допущен' # O(1)
                        else:
                            return 'Ошибка в логине или пароле' # O(1)
                    return 'Активируйте аккаунт' # O(1)
    else:        
        return 'Неизвестный логин' # O(1)
    return login

print(check_user_2(dict_user, '', ''))
print(check_user_2(dict_user, 'login1', ''))
print(check_user_2(dict_user, 'login3', ''))
print(check_user_2(dict_user, 'login3', '234'))

# Функция check_user_1 имеет меньшую сложность (O(n) < O(n**2)), поэтому эффективнее
