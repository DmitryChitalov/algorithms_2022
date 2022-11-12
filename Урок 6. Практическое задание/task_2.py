"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опишите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""
from memory_profiler import profile


@profile
def check_num(number, even_numbers=0, odd_numbers=0):
    if number == 0:
        return even_numbers, odd_numbers
    if number % 10 % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    return check_num(number // 10, even_numbers, odd_numbers)


@profile
def my_func(number):
    def check_num(number, even_numbers=0, odd_numbers=0):
        if number == 0:
            return even_numbers, odd_numbers
        if number % 10 % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
        return check_num(number // 10, even_numbers, odd_numbers)

    return check_num(number)


check_num(12345)
"""в первом случае при запуске @profile мы видим результат замеров выделяемой памяти для каждого захода рекурсии, 
что не удобно и не информативно"""
my_func(12345)
"""просто поместив функцию с рекурсией в другую функцию при использовании @profile получаем замер выделенной памяти под 
полное отрабатывание рекурсии"""
