"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


def get_even_odd_count(num, even=0, odd=0):
    if num == 0:
        return f'Количество четных и нечетных цифр в числе равно: {even}, {odd}'
    else:
        cur_num = num % 10
        if cur_num % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
        return get_even_odd_count(num, even, odd)


@profile
def one_table_result(num):
    return f'{get_even_odd_count(num)}'


print(one_table_result(100126546540))
print(get_even_odd_count(100126546540))
# если вызывать рекурсивную функцию через другую функцию, то таблица профилирования будет одна
