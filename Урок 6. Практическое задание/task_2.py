"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import memory_usage, profile



def recurs_count_odd_even_numbers(number, odd_num = 0, even_num = 0):
    if number:
        rem = number % 10
        number = number // 10
        if rem % 2 == 0:
            return recurs_count_odd_even_numbers(number, odd_num, even_num + 1)
        else:
            return recurs_count_odd_even_numbers(number, odd_num + 1, even_num)
    else:
        return even_num, odd_num

@profile
def memory_for_recurs(number, odd_num = 0, even_num = 0):
    return recurs_count_odd_even_numbers(number, odd_num=0, even_num=0)

m1 = memory_usage()
a = 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123
print(f'Количество четных и нечетных цифр в числе равно: {memory_for_recurs(int(a))}')
m2 = memory_usage()
print(f"Выполнение заняло {m2[0] - m1[0]} Mib")

"""
Проблема. 
При каждом рекурсивном вызове функции вызывается и профайлер, 
в результате профайлер отображает расход памяти по каждому вызову функции, общего результата мы не видим.
Решение.
Вызвать рекурсивную функцию из другой функции и профилировать работу этой функции.
"""