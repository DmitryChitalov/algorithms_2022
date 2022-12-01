"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import profile

number = input('Введите целое число: ')


@profile
def wrapper_func():
    def reversed_num_recurs(number, result=''):
        if not number:
            return f'Число наоборот: {result}'
        else:
            result += str(int(number) % 10)
            number = int(number) // 10
            return reversed_num_recurs(number, result)

    return reversed_num_recurs(number, result='')


print(wrapper_func())

# При работе с рекурсивной функцией для корректного отображения результата работы @profile необходимо эту функцию обернуть
#  в другую функцию, т.к. если этого не сделать, то для каждого шага рекурсии выводится своя таблица.
