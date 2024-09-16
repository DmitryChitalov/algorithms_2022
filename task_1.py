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
from timeit import repeat, default_timer

##############################################################################
"""
Доработанная пузырьковая сортировка в среднем быстрее стандартной в 1.2 раза.

Данная доработка оказывается эффективной, если входной массив уже отчасти или
полностью отсортирован. В самом лучшем случае - массив полностью отсортирован,
доработанный алгоритм произведет O(n) операций вместо O(n^2) операций
стандартного алгоритма.
"""


def bubble_sort_desc(lst):
    for i in range(len(lst)-1,-1,-1):
        for j in range(i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def bubble_sort_desc_optim(lst):
    for i in range(len(lst)-2,-1,-1):
        flag = 0
        for j in range(i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag = 1
        if flag == 0:
            break
    return lst


# Тестирование
test_lst = [randint(-100, 100) for _ in range(10)]
setup = 'test_lst = [randint(-100, 100) for _ in range(10)]'

print('Исходный массив:\t\t\t\t\t  ', *test_lst, sep='  ')
print('Пузырьковая сортировка:\t\t\t\t  ', *bubble_sort_desc(test_lst), sep='  ', end='')
res = repeat('bubble_sort_desc(test_lst)', setup, default_timer, repeat=100_000, number=1, globals=globals())
res1 = sum(res)/len(res)
print(f'  ---> время: {res1:.2e}')
print('Пузырьковая сортировка (доработанная):', *bubble_sort_desc(test_lst), sep='  ', end='')
res = repeat('bubble_sort_desc_optim(test_lst)', setup, default_timer, repeat=100_000, number=1, globals=globals())
res2 = sum(res)/len(res)
print(f'  ---> время: {res2:.2e}')
print(f'Доработанная пузырьковая сортировка быстрее стандартной приблизительно в {res1/res2:.2f} раза')
