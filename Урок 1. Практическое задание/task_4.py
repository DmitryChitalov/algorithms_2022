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


def act_check_1(dict_obj):
    user_info = ('A', "A")                     # O(1) - имитация ввода логина и пароля
    if dict_obj.get(user_info) is not None:    # O(1)
        if dict_obj[user_info]:                # O(1)
            print('Authentication complete')   # O(1)
            return True                        # O(1)
        else:                                  # O(1)
            print('Activation required')       # O(1)
            return False                       # O(1)
    else:                                      # O(1)
        print('User not found')                # O(1)
        return None                            # O(1)
# Сложность - O(1)


def act_check_2(dict_obj):
    user_info = ('A', "A")                         # O(1) - имитация ввода логина и пароля
    for key, value in dict_obj.items():            # O(N)
        if key == user_info:                       # O(1)
            val_for_check = value                  # O(1)
            if val_for_check:                      # O(1)
                print('Authentication complete')   # O(1)
                return True                        # O(1)
            else:                                  # O(1)
                print('Activation required')       # O(1)
                return False                       # O(1)
        else:                                      # O(1)
            print('User not found')                # O(1)
            return None                            # O(1)
# Сложность - O(N)


users_dict = {('A', 'A'): True, ('B', 'B'): False, ('C', 'C'): False, ('D', 'D'): True, ('E', 'E'): True,
              ('F', 'F'): False, ('G', 'G'): False, ('H', 'H'): True}

act_check_1(users_dict)
act_check_2(users_dict)

# Первый способ предпочтительнее
