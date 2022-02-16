from random import randint
from timeit import timeit


# без сортировки
def without_sort(lst_obj):
    temp = lst_obj
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


m = 10
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(orig_list)
print(f'Медиана = {without_sort(orig_list)}')

print(
    timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=100))

m = 100
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(f'Медиана = {without_sort(orig_list)}')
print(
    timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=100))

m = 1000
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(f'Медиана = {without_sort(orig_list)}')
print(
    timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=100))

'''
[50, 91, 56, 28, 79, 94, 18, 42, 11, 61, 85, 68, 34, 19, 47, 54, 59, 28, 64, 31, 76]
Медиана = 54
0.023786030000000007
Медиана = 43
1.155777004
Медиана = 50
109.54294209199999
'''
