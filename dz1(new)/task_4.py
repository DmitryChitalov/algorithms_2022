
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
# Сложность: O(n^2)
def authentication():
    password_dict = [{'nik_name': 'Alex_01', 'password': '1234', 'status': True}, {'nik_name': 'dima_02', 'password': '243', 'status': True}, {'nik_name': 'Nik_03', 'password': 'saga3543', 'status': True}, {'nik_name': 'vova_06', 'password': '243', 'status': False}]
    nik_name = input('Введите свой ник: ')
    users = filter(lambda item: item['nik_name'] == nik_name, password_dict)
    password = input('Введите пароль: ')
    for i in users:                                            # O(n)
        for val in i.values():                                 # O(n)
            if val == password and i['status'] == True:        # O(1)
                return 'Авторизация успешно пройдена!'         # O(1)
            elif val == password and i['status'] == False:     # O(1)
                print('Учетноя запись не активирована!')       # O(1)
                activ = input('Активировать? (y/n): ')         # O(1)
                if activ == 'y':                               # O(1)
                    users['status'] = True                     # O(1)
                    return 'Учетная запись активирована!'      # O(1)
                else:                                          # O(1)
                    return 'Учетная запись не активирована!'   # O(1)


print(authentication())

##############################################################################
# Сложность: O(1)
def my_func_authentication():
    password_dict = [{'nik_name': 'Alex_01', 'password': '1234', 'status': True}, {'nik_name': 'dima_02', 'password': '243', 'status': True}, {'nik_name': 'Nik_03', 'password': 'saga3543', 'status': True}, {'nik_name': 'vova_06', 'password': '243', 'status': False}]
    nik_name = input('Введите свой ник: ')
    users = next((x for x in password_dict if x['nik_name'] == nik_name), None)            # O(n)
    if users != None:                                                                      # O(1)
        password = input('Введите пароль: ')                                               # O(1)
        if users['password'] == password and users['status'] == True:                      # O(1)
            return 'Авторизация успешно пройдена!'                                         # O(1)
        elif users['password'] != password:                                                # O(1)
            return 'Неверный пароль!\nПоробуйте еще раз...'                                # O(1)
        else:
            print('Ваша учетноя запись не активирована!\nАктивируйте свою учетную запись...') # O(1)
            activ = input('Для активации введите (y/n)!:')                                    # O(1)
            if activ == 'y':                                                                  # O(1)
                users['status'] = True                                                        # O(1)
                return 'Учетная запись успешно активирована!'                                 # O(1)
            else:
                return 'Учетная запись не активированна!'
    else:
        return 'Такого пользователя не существует!'

print(my_func_authentication())



# Эфективней второе решение так как там используется генератор цикла оно менее затратное и более быстрое.
# В первом решении цикол в цикле это сложность n^2