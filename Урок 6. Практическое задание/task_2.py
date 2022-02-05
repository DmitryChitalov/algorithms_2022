"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""
from memory_profiler import profile

@profile
def decor(func):
    def wrapper(*argv):
        return func(*argv)
    return wrapper

@decor
def get_rev_number(number, rev_number = ''):                        # 0
    if number == 0:                                                 # 0
        return rev_number                                           # 0
    else:
        last_number = number % 10                                   # 0
        rev_number += str(last_number)                              # 0
        return get_rev_number(number // 10, rev_number)             # 0.2

print(get_rev_number(1234))
