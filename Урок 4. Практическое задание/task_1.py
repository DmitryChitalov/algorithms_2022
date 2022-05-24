"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """
    Приступим к оптимизации: убираем лишние строки кода, используем силу comprehensions
    В итоге наша функция будет состоять из одной (или все же правильней учитывать строку объявления, из двух) строки
    """
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def list_input(n):
    """
    генератор списка из 3тьего задания
    """
    my_list = [n + 1 for n in range(n)]
    return my_list


# Создадим тестовый массив с помошью функции из ДЗ 3 из 1000 элементов, на нем и будем отрабатывать производительность
a = list_input(1000)

# Замерим стандартную ф-ю func_1()
print(timeit("func_1(a)", globals=globals(), number=1000))
# результат на моей машине - 0.08748290000949055 сек.

# И теперь замерим мою оптимизированную ф-ю func_2() на том же массиве:
print(timeit("func_2(a)", globals=globals(), number=1000))
# Результат - 0.051145600038580596 сек.

"""
Итого: list comprehension и лаконичная запись кода позволила нам получить выйгрыш в скорости почти в 42%!!!!
(я прям сам неповерил и вычислил процент еще раз!) Я считаю, что оптимизация, определенно удалась!
"""