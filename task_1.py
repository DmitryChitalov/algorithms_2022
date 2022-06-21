from random import randint
from timeit import timeit

test_list = [randint(-100, 100) for _ in range(10)]
test_list_2 = [randint(-100, 100) for _ in range(500)]
test_list_3 = [50, 46, 43, 39, 35, 21, 15, 11, 5, 0, -3]


def bubble_sort(lst_obj):
    for i in range(len(lst_obj)-1):
        if lst_obj[i] < lst_obj[i+1]:
            lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
    return lst_obj


# print(bubble_sort(orig_list))


def bubble_sort_2(lst_obj):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(len(lst_obj)-1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                has_swapped = True
    return lst_obj


# print(bubble_sort_2(orig_list))

print(timeit('bubble_sort(test_list[:])', globals=globals(), number=1000))
print(timeit('bubble_sort_2(test_list[:])', globals=globals(), number=1000))

print(timeit('bubble_sort(test_list_2[:])', globals=globals(), number=1000))
print(timeit('bubble_sort_2(test_list_2[:])', globals=globals(), number=1000))

print(timeit('bubble_sort(test_list_3[:])', globals=globals(), number=1000))
print(timeit('bubble_sort_2(test_list_3[:])', globals=globals(), number=1000))


"""
0.0061309999999999976
0.043302499999999994
0.3919903
96.5785472
0.0030193999999994503
0.0030450999999942496

Чем больше длина массива, тем медленнее отрабатывает оптимизированный код. И даже в изначально отсортированном списке,
оптимизированный работает медленнее...
"""