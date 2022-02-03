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
# значительно сократить время работы алгоритма
# Без проверки:
# 0.046379299950785935
# С проверкой:
# 7.24999699741602e-05
# Однако стоит переставить местами первый и последний элемент и скорость 
# значительно падает, и становится эквивалентной массиву с рандомными элементами. 
# В данном случае хорошо бы помогла шейкерная сортировка!

import random
from timeit import timeit


list_1 = [i for i in random.choices(range(-100, 100), k=1000)]
list_2 = [i for i in range(1000, 0, -1)]
list_3 = list_2.copy()
list_3[0], list_3[-1] = list_3[-1], list_3[0]

def bubble_sort_reverse(sequence: list)->list:
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


print(timeit(stmt='bubble_sort_reverse(list_1[:])', globals=globals(), number=1))
print(timeit(stmt='bubble_sort_reverse(list_2[:])', globals=globals(), number=1))
print(timeit(stmt='bubble_sort_reverse(list_3[:])', globals=globals(), number=1))
