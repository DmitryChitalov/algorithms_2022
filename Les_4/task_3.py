"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

"""
Работа функций revers и revers_2, приведённых в коде дз, не соответствует условию задачи. 
revers отдаёт None, независимо от принятого числа
revers_2 отдаёт перевёрнутое число в формате float и с обрезанными нулями revers_2(4500) -> 54.0
исходный код закомментировала, написала исправленные варианты 
(возможно они не лучшие, но принципиально вроде ничего не изменилось)

Теперь по поводу аналитики:

Вывод программы:

revers: 0.043858402998012025
revers_2: 0.0121112990018446
revers_3: 0.006993723000050522
revers_4: 0.00658445899898652
revers_5: 0.008292927999718813

функции revers и revers_2 работают по абсолютно одинаковому принципу,
с той лишь разницей, что в одной цикл, а в другой рекурсия. Рекурсия работает медленнее.
revers_3 шустрый, т.к. используются срезы, по идее можно оптимизировать, 
если сразу делать return str(enter_num)[::-1], не сохраняя промежуточные значения
revers_4 использует встроенный метод строк, тоже очень быстрый
revers_5 с мемоизацией для сравнения с 2, на большом количестве прогонов работает шустрее
"""

from timeit import timeit
from random import randint


# def revers(enter_num, revers_num=0):
#     if enter_num == 0:
#         return
#     else:
#         num = enter_num % 10
#         revers_num = (revers_num + num / 10) * 10
#         enter_num //= 10
#         revers(enter_num, revers_num)

def revers(enter_num, revers_num=0):
    save_num = enter_num
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num)
    if enter_num == 0:
        if len(str(save_num)) == len(str(int(revers_num))):
            return int(revers_num)
        else:
            return f'{str(int(revers_num))}{(len(str(save_num)) - len(str(int(revers_num)))) * "0"}'


# def revers_2(enter_num, revers_num=0):
#     while enter_num != 0:
#         num = enter_num % 10
#         revers_num = (revers_num + num / 10) * 10
#         enter_num //= 10
#     return revers_num

def revers_2(enter_num, revers_num=0):
    save_num = enter_num
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    if len(str(save_num)) == len(str(int(revers_num))):
        return int(revers_num)
    else:
        return f'{str(int(revers_num))}{(len(str(save_num)) - len(str(int(revers_num)))) * "0"}'


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return reversed(str(enter_num))


# читкод: реализация с мемоизацией
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
def revers_5(enter_num, revers_num=0):
    save_num = enter_num
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num)
    if enter_num == 0:
        if len(str(save_num)) == len(str(int(revers_num))):
            return int(revers_num)
        else:
            return f'{str(int(revers_num))}{(len(str(save_num)) - len(str(int(revers_num)))) * "0"}'


print('revers: ', end='')
print(timeit('revers(randint(0, 500))', globals=globals(), number=10000))
print('revers_2: ', end='')
print(timeit('revers_2(randint(0, 500))', globals=globals(), number=10000))
print('revers_3: ', end='')
print(timeit('revers_3(randint(0, 500))', globals=globals(), number=10000))
print('revers_4: ', end='')
print(timeit('revers_4(randint(0, 500))', globals=globals(), number=10000))
print('revers_5: ', end='')
print(timeit('revers_5(randint(0, 500))', globals=globals(), number=10000))
