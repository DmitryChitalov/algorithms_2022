"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
import sys

from memory_profiler import profile


@profile
def recursive(n):
    def row_summ(n, num=1):
        if n == 0:
            return 0
        return num + row_summ(n - 1, num * -0.5)
    return row_summ(n)


@profile
def non_recursive(n):
    return sum((-0.5) ** num for num in range(0, 10))


sys.setrecursionlimit(15000)
n = 2500
print(f'Количество элементов: {n}, их сумма - {recursive(n)}.')
print(f'Количество элементов: {n}, их сумма - {non_recursive(n)}.')


"""
Для того, чтобы профилировать функцию с рекурсией, можно просто обернуть ее в другую функцию.
"""