"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr



from timeit import timeit

nums = [1, 4, 2, 3, 98, 16, 54, 11, 27, 99, 44, 52, 76, 13]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

print(f'Выполнение func_1(nums) заняло {timeit("func_1(nums[:])", globals=globals(), number=10000)} секунд')

# Выполнение func_1(nums) заняло 0.03224602099999999 секунд

def func_1(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

print(f'Выполнение func_1(nums) заняло {timeit("func_1(nums[:])", globals=globals(), number=10000)} секунд')


# Выполнение func_1(nums) заняло 0.025840965999999993 секунд
"""
Нашла это объяснение на Stackoverflow:
list comprehension работает быстрее за счёт специальной инструкции для виртуальной машины - LIST_APPEND, а не за счёт отдельной, 
свойственной только ему способности к оптимизации. LIST_APPEND избавляет от поиска атрибута/метода append у объекта и последующего вызова этого метода,
 как это происходит в обычном цикле (lst.append(new_item)).
"""

def func_1(nums):
    return [i for i, v in enumerate(nums) if v % 2 == 0]

"""
За счет того, что в функции используется одна встроенная функция enumerate() вместо двух range() и len() удалось добиться оптимизации по времени
"""
print(f'Выполнение func_1(nums) заняло {timeit("func_1(nums[:])", globals=globals(), number=10000)} секунд')

# Выполнение func_1(nums) заняло 0.020747837000000005 секунд