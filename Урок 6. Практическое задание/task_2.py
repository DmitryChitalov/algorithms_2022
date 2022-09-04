"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


count = 32


def uncodding(number: int):
    if number == 128:
        return True
    print(f'{number} - {chr(number)}', end=' ')
    if (number - 31) % 10 == 0:
        print('\n')
    uncodding(number + 1)


@profile()
def check_memory(fun):
    return fun


print(check_memory(uncodding))

''' во избежание многократного вызова profile(), создал отдельную функцию,
которая вызывает рекурсивную'''