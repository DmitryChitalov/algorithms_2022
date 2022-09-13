"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import memory_usage
from pympler.asizeof import asizeof


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


#  Функция № 1.
@decor
def theorem(n):
    def theorem_1(n, sum_n=0):
        if n < 1:
            return sum_n
        return theorem_1(n - 1, sum_n + n)

    return f'{theorem_1(n)} - левая часть равенства,\n{int(n * (n + 1) / 2)} - правя часть равенства'


#  Функция № 2.
@decor
def revers(enter_num, revers_num=0):  # Функция даёт неверный результат при больших числах
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = int((revers_num + num / 10) * 10)
        enter_num //= 10
    return revers(enter_num, revers_num)


res, mem_diff = theorem(15)
print(res)
print(f"Выполнение заняло {mem_diff} Mib")  # Выполнение заняло 0.0078125 Mib
print(asizeof(theorem(15)))  # 280
print('----------------- Другая рекурсивная функция: -----------------')
res, mem_diff = revers(123456789123456)
print(res)
print(f"Выполнение заняло {mem_diff} Mib")  # Выполнение заняло 0.01171875 Mib
print(asizeof(revers(123456789123456)))  # 1440

"""
    При замерах методами memory_profiler Функции № 2 (рекурсивной) аргументы функции попадали
столько же раз, сколько запускалась рекурсия, а результаты пробрасывались через место
вызова функции (print()  и т.д.). В результате - выдача неожиданного результата работы функции
и результаты замеров, которые вряд ли можно считать объективными.
    При замерах, произведённых на Функции № 1 (рекурсивная функция вложена в другую функцию
без рекурсии), такого эффекта не возникает.
    Это и есть выход, я думаю.
"""
