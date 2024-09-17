from random import randint
from timeit import timeit

'''
Взят с хабра - сложность O(N*logN)
'''


# Основной алгоритм сортировки кучей
def HeapSort(data):
    # Формируем первоначальное сортирующее дерево
    # Для этого справа-налево перебираем элементы массива
    # (у которых есть потомки) и делаем для каждого из них просейку
    for start in range(int((len(data) - 2) / 2), -1, -1):
        HeapSift(data, start, len(data) - 1)

    # Первый элемент массива всегда соответствует корню сортирующего дерева
    # и поэтому является максимумом для неотсортированной части массива.
    for end in range(len(data) - 1, 0, -1):
        data[end], data[0] = data[0], data[end]
        # Меняем этот максимум местами с последним
        # элементом неотсортированной части массива
        # После обмена в корне сортирующего дерева немаксимальный элемент
        # Восстанавливаем сортирующее дерево
        # Просейка для неотсортированной части массива
        HeapSift(data, 0, end - 1)
    return data[int((len(data)-1)/2)]


# Просейка свеху вниз, в результате которой восстанавливается сортирующее дерево
def HeapSift(data, start, end):
    # Начало подмассива - узел, с которого начинаем просейку вниз
    root = start

    # Цикл просейки продолжается до тех пор,
    # Пока встречаются потомки, большие чем их родитель
    while True:

        child = root * 2 + 1  # Левый потомок
        # Левый потомок за пределами подмассива - завершаем просейку
        if child > end:
            break

        # Если правый потомок тоже в пределах подмассива,
        # то среди обоих потомков выбираем наибольший
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1

        # Если больший потомок больше корня, то меняем местами
        # при этом больший потомок сам становится корнем,
        # от которого дальше опускаемся вниз по дереву
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break


m = 10
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
# print(orig_list)
print(
    timeit(
        "HeapSort(orig_list[:])",
        globals=globals(),
        number=10000))

m = 100
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "HeapSort(orig_list[:])",
        globals=globals(),
        number=10000))

m = 1000
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "HeapSort(orig_list[:])",
        globals=globals(),
        number=1000))
"""
0.33729117399999997
5.054267296
8.748639148 - за 1000 измерений
"""
