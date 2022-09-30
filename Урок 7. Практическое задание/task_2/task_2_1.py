"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

"""
Сортировка Шелла 

Идея метода заключается в сравнение разделенных на группы элементов последовательности, находящихся друг от друга 
на некотором расстоянии. Изначально это расстояние равно d или N/2, где N — общее число элементов. На первом шаге
каждая группа включает в себя два элемента расположенных друг от друга на расстоянии N/2; они сравниваются между собой,
и, в случае необходимости, меняются местами. На последующих шагах также происходят проверка и обмен, но расстояние d 
сокращается на d/2, и количество групп, соответственно, уменьшается. Постепенно расстояние между элементами
уменьшается, и на d=1 проход по массиву происходит в последний раз.
"""
from random import randint
from timeit import timeit


def shell_sort(sort_list):
    i = len(sort_list) // 2
    while i > 0:
        for value in range(i, len(sort_list)):
            current_value = sort_list[value]
            position = value

            while position >= i and sort_list[position - i] > current_value:
                sort_list[position] = sort_list[position - i]
                position -= i
                sort_list[position] = current_value

        i //= 2
    return sort_list


m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(orig_list)
print(shell_sort(orig_list))
print(timeit("shell_sort(orig_list[:])", globals=globals(), number=100))

m = 100
orig_list_2 = [randint(0, 100) for j in range(2 * m + 1)]
print(timeit("shell_sort(orig_list_2[:])", globals=globals(), number=100))

m = 1000
orig_list_3 = [randint(0, 100) for k in range(2 * m + 1)]
print(timeit("shell_sort(orig_list_3[:])", globals=globals(), number=100))

#  0.0017359000048600137
#  0.05486479999672156
#  0.7279105999914464
