"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

# Урок 2. Курс Алгоритмы.
# Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
# __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#

from memory_profiler import memory_usage
from memory_profiler import profile
from random import randint
from sys import setrecursionlimit

setrecursionlimit(10000)


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


j = 0
i = 0


def enter_a_number():
    my_flag = True
    while my_flag:
        try:
            my_number = int(input('Введите число: '))
            my_flag = False
        except ValueError:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
    return my_number


@decor  # Выполнение заняло 2.1640625 MiB. Результат: (1013, 976) при отключенном @profile.
@profile
def to_measure(number):
    def even_odd(my_num):  # @profile указывает на рост потребляемой памяти (Increment) на 3.2 MiB
        # При этом Mem usage возросла на 4,1 MiB.
        global i, j

        # базовый случай
        if my_num == 0:
            return 1, 0

        # рекурсивный случай (вызов ф-ции из себя)
        my_num_pop = my_num % 10
        parity_check = my_num_pop % 2
        my_num_whole = my_num // 10
        if parity_check == 0 or my_num_pop == 0:
            j += 1
        else:
            i += 1

        even_odd(my_num_whole)

        return j, i

    return even_odd(number)  # По окончании скрипта Mem usage увеличилась на 2.3 MiB по сравнению с началбной.


if __name__ == '__main__':
    my_num = sum(i ** i for i in range(700))
    res, mem_diff = to_measure(my_num)
    print(f"Выполнение заняло {mem_diff} MiB. Результат: {res}")

#  При использовании декоратора @profiler из профилировщика memory_profiler
#  для измерений объема памяти, выделяемой в процессе выполнения скрипта,
#  в котором содержится рекурсия без модификации функции, к которой применяется декоратор,
#  приведет к тому, что декоратор @profiler сработает столько раз,
#  сколько раз вызывается функция. Это не удобно.
#  Для того, чтобы декоратор @profiler обработал сразу все рекурсивные вызовы,
#  необходимо "прописать" рекурсию внутри другой функции (вложить),
#  тогда напротив каждой записанной строки рекурсии декоратор @profiler
#  укажет ее вклад в потребление памяти в процессе выполнения скрипта.
