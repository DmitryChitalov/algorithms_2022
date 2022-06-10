"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    revers_num = ''.join(reversed(str(enter_num)))
    return revers_num


num_user = 1234
print('Время выполнения revers:')
print(f'Для 1000 запусков: {timeit("revers(num_user)", globals=globals(), number=1000)}')
print(f'Для 10000 запусков: {timeit("revers(num_user)", globals=globals(), number=10000)}')
print(f'Для 100000 запусков: {timeit("revers(num_user)", globals=globals(), number=100000)}')
print('-' * 50)
print('Время выполнения revers_2:')
print(f'Для 1000 запусков: {timeit("revers_2(num_user)", globals=globals(), number=1000)}')
print(f'Для 10000 запусков: {timeit("revers_2(num_user)", globals=globals(), number=10000)}')
print(f'Для 100000 запусков: {timeit("revers_2(num_user)", globals=globals(), number=100000)}')
print('-' * 50)
print('Время выполнения revers_3:')
print(f'Для 1000 запусков: {timeit("revers_3(num_user)", globals=globals(), number=1000)}')
print(f'Для 10000 запусков: {timeit("revers_3(num_user)", globals=globals(), number=10000)}')
print(f'Для 100000 запусков: {timeit("revers_3(num_user)", globals=globals(), number=100000)}')
print('-' * 50)
print('Время выполнения revers_4:')
print(f'Для 1000 запусков: {timeit("revers_4(num_user)", globals=globals(), number=1000)}')
print(f'Для 10000 запусков: {timeit("revers_4(num_user)", globals=globals(), number=10000)}')
print(f'Для 100000 запусков: {timeit("revers_4(num_user)", globals=globals(), number=100000)}')
print('-' * 50)
print('Функция revers_3 работает быстрее всего, потому что у среза строки константная сложность, \n'
      'у остальных функций время выполнения выше.\n'
      'Вариант revers_4 чуть медленнее revers_3, но быстрее остальных функций,\n'
      'потому что время работы со строками всегда меньше, чем с остальными типами.')
