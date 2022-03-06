import random, timeit

elements = [random.randint(-100, 100) for i in range(100)]


def bubblesort_N(elements):
    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):
            if elements[i] < elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
    return elements


def bubblesort_Y(elements):
    t = True
    while t:
        t = False
        for n in range(len(elements) - 1, 0, -1):
            for i in range(n):
                if elements[i] < elements[i + 1]:
                    elements[i], elements[i + 1] = elements[i + 1], elements[i]
                    t = True
    return elements


print(elements)
print(bubblesort_Y(elements))
print(bubblesort_N(elements))

print(timeit.timeit("bubblesort_N(elements)", setup="from __main__ import bubblesort_N, elements", number=1000))
print(timeit.timeit("bubblesort_Y(elements)", setup="from __main__ import bubblesort_Y, elements", number=1000))

# оптимизированиая функция сортировки (bubblesort_Y) быстрее