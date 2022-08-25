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
import time

CUSTOMER_STORAGE = {('log_1"', '1'): 1, ('log_2"', '2'): 0, ('log_3"', '3'): 1, ('log_4"', '4'): 0}


def customer_authorization_in(cus_log, cus_pass):  # O(N)
    if ((cus_log, cus_pass) in CUSTOMER_STORAGE) and CUSTOMER_STORAGE[(cus_log, cus_pass)] == 1:  # O(N) + O(1)
        print(f'{cus_log}, welcome')  # O(1)
    else:
        print(f'{cus_log}, complete the registration')  # O(1)


start_time = time.clock()
customer_authorization_in('log_3"', '3')
print("{:g} s".format(time.clock() - start_time))
start_time = time.clock()
customer_authorization_in('log_4"', '4')
print("{:g} s".format(time.clock() - start_time))


def customer_authorization_for(cus_log, cus_pass):  # O(1)
    if CUSTOMER_STORAGE.get((cus_log, cus_pass)) and CUSTOMER_STORAGE[(cus_log, cus_pass)] == 1:
        # O(1) = O(1) + O(1)
        print(f'{cus_log}, welcome')  # O(1)
    else:
        print(f'{cus_log}, complete the registration')  # O(1)


start_time = time.clock()
customer_authorization_for('log_3"', '3')
print("{:g} s".format(time.clock() - start_time))
start_time = time.clock()
customer_authorization_for('log_4"', '4')
print("{:g} s".format(time.clock() - start_time))

# Второй  алгоритм быстрее,потому что доступ к элементам выполняется за константное время,
# а первый медленнее, так как время его исполнения линейное.
