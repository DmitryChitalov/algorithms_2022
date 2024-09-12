from random import randint

lst = [randint(-100, 100) for _ in range(10)]


def bubble_sort(lst):
    n = 1
    count = 0

    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1
        if count == 0:
            break
        n += 1

    return lst


print(bubble_sort(lst))
