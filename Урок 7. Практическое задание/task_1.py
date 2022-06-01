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
from cProfile import run
from random import randint
from timeit import timeit

min_l = -100
max_l = 101
l_random = [randint(min_l, max_l) for el in range(90)]


def sort(l_sort: list):
    n = len(l_sort)
    for i in range(n):
        for j in range(n - 1):
            if l_sort[j] < l_sort[j + 1]:
                l_sort[j], l_sort[j + 1] = l_sort[j + 1], l_sort[j]
    return l_sort


def sort_new(l_sort: list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(l_sort) - 1):
            if l_sort[i] < l_sort[i + 1]:
                l_sort[i], l_sort[i + 1] = l_sort[i + 1], l_sort[i]
                swapped = True
    return l_sort


def sort3(l_sort: list):
    n = len(l_sort)-1
    for i in range(n):
        for j in range(n - i):
            if l_sort[j] < l_sort[j + 1]:
                l_sort[j], l_sort[j + 1] = l_sort[j + 1], l_sort[j]
    return l_sort


list_for_test = [el for el in range(min_l, max_l)]
print(
    timeit(
        "sort(list_for_test[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "sort_new(list_for_test[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "sort3(list_for_test[:])",
        globals=globals(),
        number=1000))

"""
Для большей наглядности использовал список большего размера и с наихудшем начальным раскладом: с -1000 до 1000
Улучшение сортировки особой прибавки скорости не дал, но если необходимо отсортировать частично (в конце) 
или полностью отсортированный список, в этом случае он будет быстрее
Гораздо продуктивнее, модернизировать обычный пузырек, так:
    n = len(l_sort)-1
    for i in range(n):
        for j in range(n - i):
т.к. в ходе второго цикла мы находим наименьшее число и передвигаем его вправо, следовательно повторно к нему обращаться
нет смысла, по этому мы можем с каждым i проходом снижать кол-во вложенных проходов j
Замер обычного пузырька:
3.4787225999999998
Замер пузырька с завершением:
3.6886851999999997
Замер с декрементной длинной вложенного цикла:        
2.4837912000000006
"""
