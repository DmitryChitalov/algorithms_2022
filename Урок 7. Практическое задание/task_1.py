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
from timeit import timeit
from random import randint


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_opti(lst_obj):
    n = 1
    while n < len(lst_obj):
        my_opti = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                my_opti = False
        if my_opti:
            break
        n += 1
    return lst_obj


if __name__ == '__main__':
    orig_list = [randint(-100, 100) for _ in range(10)]
    print(orig_list)
    print(bubble_sort(orig_list[:]))
    print(bubble_sort_opti(orig_list[:]))

    # замеры 10
    print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
    print(timeit("bubble_sort_opti(orig_list[:])", globals=globals(), number=1000))

    orig_list = [randint(-100, 100) for _ in range(100)]

    # замеры 100
    print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
    print(timeit("bubble_sort_opti(orig_list[:])", globals=globals(), number=1000))

    orig_list = [randint(-100, 100) for _ in range(1000)]

    # замеры 1000
    print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
    print(timeit("bubble_sort_opti(orig_list[:])", globals=globals(), number=1000))

    """
    Результаты замеров:
    Замер 1
    Без оптимизатора 0.02710289997048676
    С оптимизатором 0.013570500072091818
    Без оптимизатора 0.6632499999832362
    С оптимизатором 0.6974942998494953
    Без оптимизатора 82.53135819989257
    С оптимизатором 92.5641485999804
    Замер 2
    Без оптимизатора 0.008312700083479285
    С оптимизатором 0.00615650019608438
    Без оптимизатора 0.6978559999261051
    С оптимизатором 0.6395455999299884
    Без оптимизатора 89.46219410002232
    С оптимизатором 96.06909079989418
    
    Вывод: может ускорять если попадется такой расклад,
    но при массовых замерах такие случаи не часты и эффекта
    это не приносит, а за счет дополнительных действий даже
    время увеличивается. 
    """
