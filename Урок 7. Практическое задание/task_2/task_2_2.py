"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов

Листинг работы скрипта приведен на lines : 125 : 154
предлагаю 2 варианта функции:
--  sorting_by_del1 :
удаляется максимальное число из левой половины списка
и удаляется минимальное число из правой половины списка

-- sorting_by_del2 :
удаляется максимальное число из левой половины списка
если кол-во элементов списка четное, еще раз
удаляется максимальное число из левой половины списка

Оба варианта работают, но с разным результатом.,

Замеры времени:
#  -- Замеры: --
#
#  for list of size 11
#  Sorting time of "sorting_by_del1"  (sec) = 0.004987099999999998
#  Sorting time of "sorting_by_del2"  (sec) = 0.005273300000000002
#
#  for list of size 101
#  Sorting time of "sorting_by_del1"  (sec) = 0.1077575
#  Sorting time of "sorting_by_del2"  (sec) = 0.12418159999999998
#
#  for list of size 1001
#  Sorting time of "sorting_by_del1"  (sec) = 6.6253855
#  Sorting time of "sorting_by_del2"  (sec) = 7.1048184
"""

from random import randint
from timeit import timeit


def sorting_by_del1(sequence1):
    #print(sequence1)
    if not is_median(sequence1):
        seq_len = len(sequence1)
        mid_index = int(( seq_len -1 )/2)
        # print (f'{sequence1[:mid_index+1]} {sequence1[mid_index:]} ')
        sequence1.remove(max(sequence1[:mid_index+1]))
        sequence1.remove(min(sequence1[mid_index-1:]))
        if not sequence1:
            return []
        sorting_by_del1(sequence1)
        return sequence1
    else:
        return sequence1

def sorting_by_del2(sequence2):
    #print(sequence2)
    if not is_median(sequence2):
        seq_len = len(sequence2)
        mid_index = int(( seq_len -1 )/2)
        sequence2.remove(max(sequence2[mid_index:]))
        if not len(sequence2) % 2:
            sequence2.remove(max(sequence2[:mid_index+1]))
        sorting_by_del2(sequence2)
        return sequence2
    else:
        return sequence2

def is_median(seq):
    if not len(seq) % 2:
        raise ValueError
    med_index = int((len(seq) - 1) / 2)
    result = False
    if len(seq) ==1:
        return True
    a = max(seq[:med_index])
    b= seq[med_index]
    c = min(seq[med_index:])
    # print( f'{seq[:med_index]}, {b}, {seq[med_index+1:]}')
    if a <= b <= c:
        result = True
    return result

print(f'\n  --- Result of Sorting by deleting: ---')


print(f'\n for list of size 11')
lst_object = [randint(-100, 100) for _ in range(11)]
print(f' list_obj = {lst_object}')
lst_object_sorted1 = sorting_by_del1(lst_object[:])
print(f' Sorted list_ by "sorting_by_del1" = {lst_object_sorted1}')
i_median1 = int((len(lst_object_sorted1) - 1) / 2)
print(f' Median index = {i_median1} ,  Median value  = {lst_object_sorted1[i_median1]}')
print(' Sorting time (sec) = ', end='')
print(timeit("sorting_by_del1(lst_object[:])", globals=globals(), number=1000))
print('')
print(f' list_obj = {lst_object}')
lst_object_sorted2 = sorting_by_del2(lst_object[:])
print(f' Sorted list_ by "sorting_by_del2" = = {lst_object_sorted2}')
i_median2 = int((len(lst_object_sorted2) - 1) / 2)
print(f' Median index = {i_median2} ,  Median value  = {lst_object_sorted2[i_median2]}')
print(' Sorting time (sec) = ', end='')
print(timeit("sorting_by_del2(lst_object[:])", globals=globals(), number=1000))

print(f'\n  -- Замеры: -- ')
for i in range(1, 4):
    list_len = 10 ** i + 1
    print(f'\n for list of size {list_len}')
    lst_object = [randint(-100, 100) for _ in range(list_len)]
    print(' Sorting time of "sorting_by_del1"  (sec) = ', end='')
    print(timeit("sorting_by_del1(lst_object[:])", globals=globals(), number=1000))
    print(' Sorting time of "sorting_by_del2"  (sec) = ', end='')
    print(timeit("sorting_by_del2(lst_object[:])", globals=globals(), number=1000))


#  --- Result of Sorting by deleting: ---
#
# for list of size 11
#  list_obj = [5, -99, 89, 85, 25, 61, -79, -69, 92, -41, 84]
#  Sorted list_ by "sorting_by_del1" = [5, -99, 25, 92, 84]
#  Median index = 2 ,  Median value  = 25
#  Sorting time (sec) = 0.004134700000000002
#
#  list_obj = [5, -99, 89, 85, 25, 61, -79, -69, 92, -41, 84]
#  Sorted list_ by "sorting_by_del2" = = [-99, -79, -69]
#  Median index = 1 ,  Median value  = -79
#  Sorting time (sec) = 0.004984100000000002
#
#  -- Замеры: --
#
#  for list of size 11
#  Sorting time of "sorting_by_del1"  (sec) = 0.004987099999999998
#  Sorting time of "sorting_by_del2"  (sec) = 0.005273300000000002
#
#
#  for list of size 101
#  Sorting time of "sorting_by_del1"  (sec) = 0.1077575
#  Sorting time of "sorting_by_del2"  (sec) = 0.12418159999999998
#
#
#  for list of size 1001
#  Sorting time of "sorting_by_del1"  (sec) = 6.6253855
#  Sorting time of "sorting_by_del2"  (sec) = 7.1048184
#
#
# Process finished with exit code 0
