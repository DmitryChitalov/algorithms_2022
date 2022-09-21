"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""

from memory_profiler import memory_usage


def decor_m(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


def sum_digit(digit):
    result = 0
    while True:
        remainder = digit % 10
        result += remainder
        digit = digit // 10
        if digit <= 0:
            break

    return result


@decor_m
def func_1(cube_lst):
    result = 0
    for el in cube_lst:
        if sum_digit(el) % 7 == 0:
            result += el

    print(result)

    result = 0
    for i in range(len(cube_lst)):
        cube_lst[i] += 17
        if sum_digit(cube_lst[i]) % 7 == 0:
            result += cube_lst[i]

    print(result)


def multiple_seven(el):
    if sum_digit(el) % 7 == 0:
        return el
    else:
        return 0


@decor_m
def func_2(cube_lst):
    sum_el = sum(map(multiple_seven, cube_lst))
    print(sum_el)
    sum_el = list(map(lambda x: x + 17, cube_lst))
    sum_el = sum(map(multiple_seven, sum_el))
    print(sum_el)


if __name__ == '__main__':
    cube_list = [i ** 3 for i in range(1, 100000, 2)]
    func_1(cube_list.copy())
    func_2(cube_list.copy())

"""
Выполнение func_1 заняло 2.328125 Mib
Выполнение func_2 заняло 0.015625 Mib
Использование функции map позволило существенно снизить затраты памяти
"""
