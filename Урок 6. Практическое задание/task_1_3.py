"""
КУРС: "Основы языка Python". Урок 5: "Генераторы и comprehensions. Множества". Задание 4.
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего.
"""
from pympler.asizeof import asizeof
from numpy import array


# https://github.com/AzarnykhOleg/Python-Basics/pull/6
def get_numbers(src: list):
    lst = [num for num in src if num > src[src.index(num) - 1]]
    return lst


# Обновлённый вариант
def get_numbers_1(src: list):
    lst = array([num for num in src if num > src[src.index(num) - 1]])
    return lst


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 444]
print(get_numbers(src))
print(asizeof(get_numbers(src)))  # -> 352
print('----------------- Новый вариант -----------------')
print(get_numbers_1(src))
print(asizeof(get_numbers_1(src)))  # -> 152

"""
Прибегнув к использованию модуля библиотеки Numpy вместо создания списка,
удалось более эффективно задействовать ресурсы памяти.
"""
