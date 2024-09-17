"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение мемоизацией
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!

П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse', end='')
# print(
#     timeit(
#         "recursive_reverse(num_100)",
#         setup='from __main__ import recursive_reverse, num_100',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_1000)",
#         setup='from __main__ import recursive_reverse, num_1000',
#         number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:

            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem', end='')
# print(
#     timeit(
#         'recursive_reverse_mem(num_100)',
#         setup='from __main__ import recursive_reverse_mem, num_100',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_1000)',
#         setup='from __main__ import recursive_reverse_mem, num_1000',
#         number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))


'''
1)Используя меморизацию мы пытаемся ускорить рекурсию - а рекурсия заранее замедленна
 из за стека вызовов - убираем рекурсию. 

2) Убираем затратный многократный перевод в str - меняем на однократный 

3) вместо for используем list_comprehensions

'''


print(f'Работа функции без меморизации и без рекурсии ',end='')
def my_revers(number):
    str_number = str(number)
    li = [i for i in str_number[::-1]]
    return ''.join(li)


res = my_revers(num_10000)
print(timeit('my_revers(num_10000)', globals=globals(), number=10000))

print(f'Проверим числа number {num_10000} revers_number {res}')


'''Выводы:
меморизация дает ускорение для рекурсии, но рекурсия тратит место из за стека вызовов
если переработать рекурсию то можно получить ускорение работы в 5 раз 
Переработанный код медленнее чем с меморизация+рекрусия но: 
1) переработанный код более `чистый` лаконичный  4 строчки против 13 (меморизация + рекурсия)
2) в результате меморизации мы запоминаем создаем словарь и заполняем егочислом противоположным к каждому
и используя рекурсию мы тоже тратим память на стек вызовов т.е. происходит двойной удар по памяти
   Но если память у нас не лимитирована и жизненно важна скорость то 
необходимо использовать меморизация+рекурсия т.к. она быстрее модернизированной 
функции в 4 раза
'''