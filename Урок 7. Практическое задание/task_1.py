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
# ======= Итоги =======
# Проверка на то смещался ли пузырек во внутренем цикле или нет позволяет 
# значительно сократить время работы алгоритма в случаях когда список почти отсортирован.
# Если список состоит из случайный чисел, тогда разницы в скорости работы практически нет.
# timeit(stmt=bubble_sort_advanced(list_random_100_el[:]), globals=globals(), number=100) = 0.05978869996033609
# timeit(stmt=bubble_sort_simple(list_random_100_el[:]), globals=globals(), number=100) =   0.05635110003640875
# timeit(stmt=bubble_sort_advanced(list_sorted_100_el[:]), globals=globals(), number=100) = 0.0008536000386811793
# timeit(stmt=bubble_sort_simple(list_sorted_100_el[:]), globals=globals(), number=100) =   0.030856099969241768
# timeit(stmt=bubble_sort_advanced(list_almost_sorted_100_el1[:]), globals=globals(), number=100) = 0.006926600006408989
# timeit(stmt=bubble_sort_simple(list_almost_sorted_100_el1[:]), globals=globals(), number=100) = 0.030829800001811236
# timeit(stmt=bubble_sort_advanced(list_almost_sorted_100_el2[:]), globals=globals(), number=100) = 0.03323399997316301
# timeit(stmt=bubble_sort_simple(list_almost_sorted_100_el2[:]), globals=globals(), number=100) = 0.03240590001223609
# Однако стоит переставить местами первый и последний элемент и скорость 
# значительно падает, и становится эквивалентной массиву с рандомными элементами. 
# В данном случае хорошо бы помогла шейкерная сортировка!

import random
from timeit import timeit


list_random_100_el = [i for i in random.choices(range(-100, 100), k=100)]
list_sorted_100_el = [i for i in range(100, 0, -1)]
list_almost_sorted_100_el1 = list_sorted_100_el.copy()
list_almost_sorted_100_el2 = list_sorted_100_el.copy()
list_almost_sorted_100_el1[0], list_almost_sorted_100_el1[10] = (list_almost_sorted_100_el1[10], 
                                                                list_almost_sorted_100_el1[0])
list_almost_sorted_100_el2[0], list_almost_sorted_100_el2[-1] = (list_almost_sorted_100_el2[-1], 
                                                                list_almost_sorted_100_el2[0])

def bubble_sort_advanced(sequence: list)->list:
    is_sorted = False
    index_last_element = len(sequence)-1
    for collected_bubble_index in range(0, index_last_element):
        if not is_sorted:
            is_sorted = True
            for i in range(index_last_element, collected_bubble_index, -1):
                if sequence[i] > sequence[i-1]:
                    sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
                    is_sorted = False
        else:
            break
    return sequence

def bubble_sort_simple(sequence: list)->list:
    index_last_element = len(sequence)-1
    for collected_bubble_index in range(0, index_last_element):
            for i in range(index_last_element, collected_bubble_index, -1):
                if sequence[i] > sequence[i-1]:
                    sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
    return sequence

for list_ in ['list_random_100_el', 
                'list_sorted_100_el', 
                'list_almost_sorted_100_el1', 
                'list_almost_sorted_100_el2']:
    for func in ['bubble_sort_advanced', 'bubble_sort_simple']:
        stmt = f'{func}({list_}[:])'
        message = f"timeit(stmt={stmt}, globals=globals(), number=100) = "
        print(f"{message:90}{timeit(stmt=stmt, globals=globals(),number=100)}")



