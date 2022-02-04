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
def func_for_decorator(user_num):
    def check_equality(num):
        return num if num == 1 else num + check_equality(num-1)
    return check_equality(user_num)


test_1 = int(input('Введите число: '))
if func_for_decorator(test_1) == test_1 * (test_1 + 1) / 2:
    print('Равенство выполняется')
else:
    print('Равенство не выполняется')


"""
Проблема: вывод таблицы при каждом вызове рекурсии. Решение - дополнительная функция вокруг рекурсивной и применение
профилирования к этой функции для вывода единственной общей таблицы.
"""
