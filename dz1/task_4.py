
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

##############################################################################
def authentication():
    password_dict = [{'nik_name': 'Alex_01', 'password': '1234', 'status': True}, {'nik_name': 'dima_02', 'password': '243', 'status': True}, {'nik_name': 'Nik_03', 'password': 'saga3543', 'status': True}, {'nik_name': 'vova_06', 'password': '243', 'status': False}]
    nik_name = input('Введите свой ник: ')
    users = filter(lambda item: item['nik_name'] == nik_name, password_dict)
    password = input('Введите пароль: ')
    for i in users:
        for val in i.values():
            if val == password and i['status'] == True:
                return 'Авторизация успешно пройдена!'
            elif val == password and i['status'] == False:
                print('Учетноя запись не активирована!')
                activ = input('Активировать? (y/n): ')
                if activ == 'y':
                    users['status'] = True
                    return 'Учетная запись активирована!'
                else:
                    return 'Учетная запись не активирована!'


print(authentication())

##############################################################################
def my_func_authentication():
    password_dict = [{'nik_name': 'Alex_01', 'password': '1234', 'status': True}, {'nik_name': 'dima_02', 'password': '243', 'status': True}, {'nik_name': 'Nik_03', 'password': 'saga3543', 'status': True}, {'nik_name': 'vova_06', 'password': '243', 'status': False}]
    nik_name = input('Введите свой ник: ')
    users = next((x for x in password_dict if x['nik_name'] == nik_name), None)
    if users != None:
        password = input('Ввудите пароль: ')
        if users['password'] == password and users['status'] == True:
            return 'Авторизация успешно пройдена!'
        elif users['password'] != password:
            return 'Неверный пароль!\nПоробуйте еще раз...'
        else:
            print('Ваша учетноя запись не активирована!\nАктивируйте свою учетную запись...')
            activ = input('Для активации введите (y/n)!:')
            if activ == 'y':
                users['status'] = True
                return 'Учетная запись успешно активирована!'
            else:
                return 'Учетная запись не активированна!'
    else:
        return 'Такого пользователя не существует!'

print(my_func_authentication())