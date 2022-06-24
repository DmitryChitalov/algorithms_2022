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
from collections import Counter
import heapq


class MyNode:
    def __init__(self, left=None, right=None, symbol=None, weight=None):
        self.left = left
        self.right = right
        self.symbol = symbol
        self.weight = weight

    # Метод сравнения элементов по частоте символа для работы кучи
    def __lt__(self, other):
        return self.weight < other.weight

    def encode(self, encoding):
        if self.left is None and self.right is None:
            yield self.symbol, encoding
        else:
            for v in self.left.encode(encoding + '0'):
                yield v
            for v in self.right.encode(encoding + '1'):
                yield v


code_table = dict()


def huffman_tree_heap(s):
    heap = []
    for ch, freq in Counter(s).items():
        heap.append((MyNode(symbol=ch, weight=freq)))
    heapq.heapify(heap)
    while len(heap) > 1:
        _n1 = heapq.heappop(heap)
        _n2 = heapq.heappop(heap)
        n_sum = MyNode(weight=(_n1.weight + _n2.weight), left=_n1, right=_n2)
        heapq.heappush(heap, n_sum)
    return heap.pop()


s = "beep boop beer!"
for i in huffman_tree_heap(s).encode(""):
    code_table[i[0]] = i[1]

for i in s:
    print(code_table[i], end=' ')
print()
