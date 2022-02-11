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
def result():
    you_numb = int(input('Введите число: '))

    def digit_from_number(numb=you_numb, even=0, odd=0):
        if numb == 0:
            return f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})'
        digit = numb % 10
        if digit % 2:
            odd += 1
        else:
            even += 1
        return digit_from_number(numb // 10, even, odd)
    return digit_from_number()


if __name__ == '__main__':
    print(result())


'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     18.7 MiB     18.7 MiB           1   @profile
    13                                         def result():
    14     18.7 MiB      0.0 MiB           1       you_numb = int(input('Введите число: '))
    15                                         
    16     18.7 MiB      0.0 MiB           8       def digit_from_number(numb=you_numb, even=0, odd=0):
    17     18.7 MiB      0.0 MiB           7           if numb == 0:
    18     18.7 MiB      0.0 MiB           1               return f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})'
    19     18.7 MiB      0.0 MiB           6           digit = numb % 10
    20     18.7 MiB      0.0 MiB           6           if digit % 2:
    21     18.7 MiB      0.0 MiB           3               odd += 1
    22                                                 else:
    23     18.7 MiB      0.0 MiB           3               even += 1
    24     18.7 MiB      0.0 MiB           6           return digit_from_number(numb // 10, even, odd)
    25     18.7 MiB      0.0 MiB           1       return digit_from_number()
    
Проблема профилирования памяти в скрипте с рекурсией заключается в том, что профилировщик memory_profiler производит 
замер памяти каждого вызова рекурсии. Проблему можно решить, обервнув рекурсивную функцию в другую функцию, то есть
создать декоратор. '''
