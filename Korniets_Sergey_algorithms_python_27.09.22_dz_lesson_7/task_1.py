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

def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = True
        if flag == False:
            break
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list[:]))
print(bubble_sort_2(orig_list[:]))

# замеры 10
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))      # 0.008097100006125402
print(timeit("bubble_sort_2(orig_list[:])", globals=globals(), number=1000))    # 0.007197199993242975

# замеры 100
orig_list = [randint(-100, 100) for _ in range(100)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))      # 0.6273661000013817
print(timeit("bubble_sort_2(orig_list[:])", globals=globals(), number=1000))    # 0.5997879999995348

# замеры 1000
orig_list = [randint(-100, 100) for _ in range(1000)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))      # 77.17954710000049
print(timeit("bubble_sort_2(orig_list[:])", globals=globals(), number=1000))    # 76.66674339999736

"""
Вывод: доработка алгоритма позволила сократить время сортировки. Однако, на больших массивах
(при значительном времени выполнения) результаты могут отличаться, ввиду перераспределения
вычислительного ресурса на другие нужды операционной системы.
"""
