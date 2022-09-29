"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""


from memory_profiler import profile


# @profile
# def my_def(num, even_numbers=0, non_even_numbers=0):
#     if num == 0:
#         return even_numbers, non_even_numbers
#     else:
#         number = num % 10
#         if number % 2 == 0:
#             even_numbers += 1
#         else:
#             non_even_numbers += 1
#         return my_def(num // 10, even_numbers, non_even_numbers)
#
# my_def(15987)

"""
Проблема в процессе замеров заключается в том, что данные сложно читаемы.
Таблиц столько, скольки и вызовов рекурсии, а если функцию оборачиваешь в функцию,
то таблица одна по всему процессу.
В столбце 'Occurrences' показано, сколько раз вызвано то или иное выражение.
"""

@profile
def my_def_1():
    def my_def(num, even_numbers=0, non_even_numbers=0):
        if num == 0:
            return even_numbers, non_even_numbers
        else:
            number = num % 10
            if number % 2 == 0:
                even_numbers += 1
            else:
                non_even_numbers += 1
            return my_def(num // 10, even_numbers, non_even_numbers)

    my_def(15987)


my_def_1()