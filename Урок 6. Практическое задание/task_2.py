"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

'''
За исходный код взято задание 2.3 Алгоритмы питон.
Ответ: при запуске рекурсивной функции происходят замеры памяти функции каждый раз как функция запускается, например,
для выполнения кода рекурсии потребуется вызвать функцию 4 раза, то в результате мы получим 4 отчета по замеру памяти.
Чтобы обойти эту проблему можно использовать функцию обертку, внутри которой будет находится рекурсия, тогда на выходе
получим только один отчет.
'''

from memory_profiler import profile
@profile # получаем 5 отчетов
def reverse_number(number, result=''):
    if number == 0:
        return result
    result_number = str(number % 10)
    result += result_number
    number = number // 10
    return reverse_number(number, result)


print(reverse_number(1230))  # => 0321


@profile # получаем один отчет
def wrapper(number, result=''):

    def reverse_number(number, result=''):
        if number == 0:
            return result
        result_number = str(number % 10)
        result += result_number
        number = number // 10
        return reverse_number(number, result)
    return reverse_number(number, result)
print(wrapper(1230))  # => 0321
