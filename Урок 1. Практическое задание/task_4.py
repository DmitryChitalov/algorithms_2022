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


def checking_account_1(login, password, acc):  # O(n)
    if login not in acc.keys():  # O(n)
        return f'Пользователь не найден. Пройдите авторизацию.'  # O(1)
    elif password == str(acc[login][0]) and acc[login][1]:  # O(1)
        return f'Добро пожаловать, {login}!'  # O(1)
    elif password == str(acc[login][0]) and not acc[login][1]:  # O(1)
        return f'Активируйте Вашу учётную запись, {login}!'  # O(1)
    elif password != str(acc[login][0]) and not acc[login][1]:  # O(1)
        return f'Введён неверный пароль, {login}!'  # O(1)
    else:
        return f'Логин {login} занят. Зарегистрируйтесь и пройдите авторизацию под другим логином!'  # O(1)


def checking_account_2(login, password, acc):  # O(1)
    if not acc.get(login):  # O(1)
        return f'Пользователь не найден. Пройдите авторизацию.'  # O(1)
    elif password == str(acc[login][0]) and acc[login][1]:  # O(1)
        return f'Добро пожаловать, {login}!'  # O(1)
    elif password == str(acc[login][0]) and not acc[login][1]:  # O(1)
        return f'Активируйте Вашу учётную запись, {login}!'  # O(1)
    elif password != str(acc[login][0]) and not acc[login][1]:  # O(1)
        return f'Введён неверный пароль, {login}!'  # O(1)
    else:
        return f'Логин {login} занят. Зарегистрируйтесь и пройдите авторизацию под другим логином!'  # O(1)


accounts = {'oleg': [111111, True], 'vlad': [333333, False]}

print(checking_account_1('oleg', '111111', accounts))
print(checking_account_1('oleg', '222222', accounts))
print(checking_account_1('vlad', '111111', accounts))
print(checking_account_1('vlad', '333333', accounts))
print(checking_account_1('serg', '333333', accounts))
print("_____________________________________________")
print(checking_account_2('oleg', '111111', accounts))
print(checking_account_2('oleg', '222222', accounts))
print(checking_account_2('vlad', '111111', accounts))
print(checking_account_2('vlad', '333333', accounts))
print(checking_account_2('serg', '333333', accounts))

"""
Функция checking_account_2 работает эффективнее функции checking_account_1,
за счёт работы встроенной функции get (O(1)), в отличие от сложности
перебора (O(n)).
"""