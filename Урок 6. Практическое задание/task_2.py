"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""
from memory_profiler import profile


def table(start=32):
    stop = 128
    if start < stop:
        print(f"{start} - {chr(start)}", end=' ')
        if start % 10 == 1:
            print()
        return table(start + 1)


@profile
def shell():
    table()


shell()
# при профилировании памяти в скрипте с рекурсией замеры происходят при каждом вызове функции, для того чтобы произвести
# один замер нужно добавить функцию и в ней вызвать нужную для замера функцию
