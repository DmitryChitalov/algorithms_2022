"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randint
from timeit import timeit


user_lst_1 = [randint(-100, 100) for i in range(10**3)]
user_lst_2 = [randint(-100, 100) for i in range(10**3)]


# Изначальная функция:
def bubble_sort(lst_obj):
    for i in range(len(lst_obj) - 1):
        for j in range(len(lst_obj) - i - 1):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
    return lst_obj


# Используем маркер
def bubble_sort_marker(lst_obj):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
    return lst_obj


print(timeit("bubble_sort(user_lst_1)", globals=globals(), number=100))
print(timeit("bubble_sort_marker(user_lst_2)", globals=globals(), number=100))

"""
Результаты:
4.8226908999968146
0.14204780000000028

Использование маркера значительно сокращает время, затрачиваемое на сортировку
"""


user_lst_1 = [randint(-100, 100) for i in range(10**2)]
user_lst_2 = [randint(-100, 100) for i in range(10**2)]
print(timeit("bubble_sort(user_lst_1)", globals=globals(), number=100))
print(timeit("bubble_sort_marker(user_lst_2)", globals=globals(), number=100))
"""
Результаты:
0.042267199998605065
0.002100300000165589
"""


user_lst_1 = [randint(-100, 100) for i in range(10)]
user_lst_2 = [randint(-100, 100) for i in range(10)]
print(timeit("bubble_sort(user_lst_1)", globals=globals(), number=100))
print(timeit("bubble_sort_marker(user_lst_2)", globals=globals(), number=100))
"""
Результаты:
0.0006639999992330559
0.0001281000004382804
"""

"""
Чем меньше список, тем меньше разница в пользу использования маркера
"""