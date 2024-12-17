"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
import heapq
from collections import Counter


def haffman_tree(s):
    # Подсчёт частоты символов
    count = Counter(s)
    # Создание кучи для дерева Хаффмана
    heap = [[weight, [char, ""]] for char, weight in count.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Извлечение двух наименее вероятных элементов
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        # Присваивание нового префикса и создание нового узла
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        # Объединение в новый узел
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0]


def haffman_code(tree):
    return {char: code for char, code in tree[1:]}


# строка для кодирования
s = "beep boop beer!"

# Построение дерева и получение кодов
tree = haffman_tree(s)
code_table = haffman_code(tree)

# Печать кодов для каждого символа
for i in s:
    print(f"{i} = {code_table[i]}")
