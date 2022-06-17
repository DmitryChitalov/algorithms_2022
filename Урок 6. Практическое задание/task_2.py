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
def test(numbers, count_even=0, count_odd=0):
    if numbers == 0:
        return count_even, count_odd
    else:
        num = numbers % 10
        numbers = numbers // 10
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    return test(numbers, count_even, count_odd)


try:
    number = int(input('Введите число: '))
    print('Количество четных и нечетных цифр в числе равно: ' + str(test(number)))
except ValueError:
    print('Введено не натуральное число')


def mod_test(numbers, count_even=0, count_odd=0):
    if numbers == 0:
        return count_even, count_odd
    else:
        num = numbers % 10
        numbers = numbers // 10
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    return test(numbers, count_even, count_odd)


@profile
def prof_test(num):
    return mod_test(num)


try:
    number = int(input('Введите число: '))
    print('Количество четных и нечетных цифр в числе равно: ' + str(prof_test(number)))
except ValueError:
    print('Введено не натуральное число')

"""
Проблема: Рекурсивно запускается не только функция но и обертка, таким образом мы видим много выводов в консоль
Решение: Создать дополнительную функцию, обернуть её, в ней вызвать рекурсивную функцию без декоратора, для замеров
запускать дополнительную функцию вместо функции с рекурсией
"""
