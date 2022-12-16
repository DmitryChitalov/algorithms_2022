"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""

from timeit import timeit
from random import randint
from cProfile import run
from memory_profiler import profile,memory_usage

@profile
def recursive_profile(number):
    def recursive_reverse(number):
        if number == 0:
            return str(number % 10)
        return f'{str(number % 10)}{recursive_reverse(number // 10)}'
    return recursive_reverse(number)

print(recursive_profile(123456789))


"""При рекурсии профайлер выдает на кадое обращение к функции таблицу, чтобы этого избежать обернем функцию другой 
не рекурсивной функцией
"""