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
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_2(lst_obj):
    swapped = False
    for i in range(len(lst_obj) - 1, 0, - 1):
        for j in range(i):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return lst_obj


# замеры 10
orig_list_1 = [randint(-100, 100) for _ in range(10)]
print(timeit("bubble_sort(orig_list_1[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_2(orig_list_1[:])", globals=globals(), number=1000))

# замеры 100
orig_list_2 = [randint(-100, 100) for _ in range(100)]
print(timeit("bubble_sort(orig_list_2[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_2(orig_list_2[:])", globals=globals(), number=1000))

# замеры 1000
orig_list_3 = [randint(-100, 100) for _ in range(1000)]
print(timeit("bubble_sort(orig_list_3[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_2(orig_list_3[:])", globals=globals(), number=1000))

"""При доработки сортировки одномерных целочисленных массивов методом 'Пузырька'
заменила цикл while на for и добавила условие завершения итерации если за проход 
по списку не совершается ни одной сортировки. Оптимизация по времени совсем небольшая. 
Сложность квадратичная. Этот метод неэффективен, т.к. при работе с большими массивами
время выполнения будет квадратично зависеть от количества сортируемых элементов. 
Доработка будет эффективна только при заранее выстроеном массиве от -100 до 100. """
