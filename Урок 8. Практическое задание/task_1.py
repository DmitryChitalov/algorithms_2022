"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
from collections import Counter
import heapq


class MyNode(object):
    __slots__ = ('weight', 'element', 'left', 'right')

    def __init__(self, weight=None, element=None, left=None, right=None):
        self.weight = weight
        self.element = element
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

    def huffman_encode(self, encode):
        if self.left is None and self.right is None:
            yield self.element, encode
        else:
            for n in self.left.huffman_encode(encode + '0'):
                yield n
            for n in self.right.huffman_encode(encode + '1'):
                yield n


code_table = dict()


def huffman_tree(s):
    h = []
    for k, v in Counter(s).items():
        h.append(MyNode(element=k, weight=v))
    heapq.heapify(h)
    while len(h) > 1:
        _el1 = heapq.heappop(h)
        _el2 = heapq.heappop(h)
        el_sum = MyNode(weight=(_el1.weight + _el2.weight), left=_el1, right=_el2)
        heapq.heappush(h, el_sum)
    return h.pop()


s = input('Введите строку: ')

for i in huffman_tree(s).huffman_encode(""):
    code_table[i[0]] = i[1]

for i in s:
    print(code_table[i], end=" ")
