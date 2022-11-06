"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import profile


@profile
def func_test(number):
    def even_odd_numbers(number, even_numbers=0, odd_numbers=0):
        if number == 0:
            return (f'Количество четных и нечетных цифр в числе: {even_numbers} и {odd_numbers}')
        else:
            current_number = number % 10
            if current_number % 2 == 0:
                even_numbers += 1
            else:
                odd_numbers += 1
            number //= 10
        return even_odd_numbers(number, even_numbers, odd_numbers)

    return even_odd_numbers(number)


func_test(3213246543213546541321654321324654321354654132165432132465432135465414454532169954328813)

"""
Это моя функция из Dz 2, task 2. Алгоритмы и структуры данных на Python. 
Во избежания многократного вывода информации о профилировании памяти рекурсивной функции можно воспользоваться 
внешней функцией, которая оборачивает рекурсивную функцию, и произвести замер памяти этой (внешней) функции. 
Вы об этом говорили на уроке! 

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     19.3 MiB     19.3 MiB           1   @profile
    17                                         def func_test(number):
    18     19.4 MiB      0.1 MiB          90       def even_odd_numbers(number, even_numbers=0, odd_numbers=0):
    19     19.4 MiB      0.0 MiB          89           if number == 0:
    20     19.4 MiB      0.0 MiB           1               return (f'Количество четных и нечетных цифр в числе: {even_numbers} и {odd_numbers}')
    21                                                 else:
    22     19.4 MiB      0.0 MiB          88               current_number = number % 10
    23     19.4 MiB      0.0 MiB          88               if current_number % 2 == 0:
    24     19.4 MiB      0.0 MiB          42                   even_numbers += 1
    25                                                     else:
    26     19.4 MiB      0.0 MiB          46                   odd_numbers += 1
    27     19.4 MiB      0.0 MiB          88               number //= 10
    28     19.4 MiB      0.0 MiB          88           return even_odd_numbers(number, even_numbers, odd_numbers)
    29                                         
    30     19.4 MiB      0.0 MiB           1       return even_odd_numbers(number)


Process finished with exit code 0

"""
