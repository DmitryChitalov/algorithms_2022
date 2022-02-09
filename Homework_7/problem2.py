from random import randint
from statistics import median

n = [randint(-100, 100) for i in range(11)]

def nom(arr):                                                   # первый вариант
    index = 0
    while index < len(arr):
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
    return arr[len(arr) // 2]

def off(arr):                                                   # работает в большинстве случаев, не придумал лучше
    summa = 0
    for i in arr:
        summa += i
    avg = summa // len(arr)
    barr = [abs(avg - i) for i in arr]
    isk = arr[barr.index(min(barr))]
    return isk

def imp(arr):                                                   # третий вариант
    return median(arr)


print(n)
print(nom(n))
print(off(n))
print(imp(n))