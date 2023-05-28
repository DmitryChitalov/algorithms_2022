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
"""


import random
import timeit


def findmedian(data):
    """

    :param data:
    :return:
    """
    for i in range(len(data)-1):
        ctr_bgr = 0
        ctr_smlr = 0
        n = data.count(data[i])
        for el in data:
            if el < data[i]: # Считает элементы меньше чем текущий
                ctr_bgr = ctr_bgr+1
            if el > data[i]: # Считает элементы больше чем текущий
                ctr_smlr = ctr_smlr + 1
        if abs(ctr_bgr-ctr_smlr) <= (not len(data)%2) + n-1: # Разница между счётчиками должна быть меньше количества
            # идентичных элементов - 1. Плюс один, если список имеет чётноё число элементов
            return data[i]




if __name__ == "__main__":
    random.seed()
    m = 100
    lenght = 2*m+1
    inputdata = [random.randint(-100,100) for i in range(lenght)]
    #print(inputdata)
    print(f"Медиана - {findmedian(inputdata)}")
    print(f"Проверка - {sorted(inputdata)[m]}") # медиана с помощью встроенной функции для проверки
    print(sorted(inputdata))  # Отсортированный массив
    print(findmedian([0,0,1,1,1,2,2,3,3]))


    a = lambda: findmedian([random.randint(-100, 100) for i in range(10)])
    b = lambda: findmedian([random.randint(-100, 100) for i in range(100)])
    c = lambda: findmedian([random.randint(-500, 500) for i in range(1000)])
    print(timeit.timeit(a, number=1000))
    print(timeit.timeit(b, number=1000))
    print(timeit.timeit(c, number=1000)) #Очень медленно ~30c
    # Существует очень эффективный алгоритм median of medians, но он использует сортировку для пожмножеств
    # Мой алгоритм проходит по каждому элементу и считает элементы которые болтше или меньше него