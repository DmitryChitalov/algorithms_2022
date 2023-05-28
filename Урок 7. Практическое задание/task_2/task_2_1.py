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


import random
import timeit


def shellsort(data):
    """

    :param data:
    :return:
    """
    k = len(data)// 2 - 1 # разница между индексами элементов ("гэп")
    while k != 0:
        for i in range(k,len(data)): # Проход по элементам
            if data[i-k] > data[i]:
                tmp = data[i]
                data[i] = data[i-k]
                data[i-k] = tmp
                for ii in range(i,0,-k): # Если происходит замена, то проверяем предыдущие элементы с гэпом k
                    if ii - 2*k >=0 and data[ii - 2*k] > data[ii-k]:
                        tmp = data[ii-k]
                        data[ii-k] = data[ii - 2*k]
                        data[ii - 2*k] = tmp
                    else:
                        break
        k = k//2 ## делим гэп на два без остатка
    return data


if __name__ == "__main__":
    random.seed()
    m = 5
    lenght = 2*m+1
    inputdata = [random.randint(-100,100) for i in range(lenght)]
    print(inputdata)
    sorteddata = shellsort(inputdata[:])
    print(sorteddata)
    print(f"Медиана - {sorteddata[len(sorteddata)//2]}")
    print(f"Проверка - {sorted(inputdata)[m]}")
    #print(shellsort([random.randint(-100,100) for i in range(lenght)]))

    a = lambda: shellsort([random.randint(-100,100) for i in range(10)])
    b = lambda: shellsort([random.randint(-100, 100) for i in range(100)])
    c = lambda: shellsort([random.randint(-500, 500) for i in range(1000)])
    #print(shellsort([random.randint(-500, 500) for i in range(1000)]))
    print(timeit.timeit(a, number=1000))
    print(timeit.timeit(b, number=1000))
    print(timeit.timeit(c, number=1000))
