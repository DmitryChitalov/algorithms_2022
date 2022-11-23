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
from collections import Counter, namedtuple


class Branch(namedtuple("Branch", ["left", "right"])):
    def walk(self, code, ac):
        self.left.walk(code, ac + "0")
        self.right.walk(code, ac + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, ac):
        code[self.char] = ac or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, count_1, left = heapq.heappop(h)
        freq2, count_2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Branch(left, right)))
        count += 1
    codes = {}
    if h:
        [(freq, count, root)] = h
        root.walk(codes, "")
    return codes


s = "beep boop beer!"
code = huffman_encode(s)
encoded = "".join(code[ch] for ch in s)
print(encoded)
