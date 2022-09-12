"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile

def recurs_parity(users, even=0, odd=0):
    if users == 0:
        return even, odd
    else:
        last_element = users % 10
        if not last_element % 2:
            even += 1
        else:
            odd += 1
        users = users // 10
        return recurs_parity(users, even, odd)

@profile
def user_enter():
    users = int(input('Введите число: '))
    print(recurs_parity(users))

user_enter()

# При профилировании памяти рекурсивной функции напрямую, будет выводится количество
# информации равное количеству вызовов рекурсии, чтобы решть эту проблему нужно
# обернуть исходную функцию, тогда она не будет замерять каждый вызов рекурсии
"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    27     18.2 MiB     18.2 MiB           1   @profile
    28                                         def user_enter():
    29     18.3 MiB      0.0 MiB           1       users = int(input('Введите число: '))
    30     18.3 MiB      0.0 MiB           1       print(recurs_parity(users))
"""