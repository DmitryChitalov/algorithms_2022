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
# надеюсь транслитерация соблюдена

import heapq
from collections import Counter
from collections import namedtuple


class Branch(namedtuple("Node", ["left", "right"])):  # дерево
    def crawler(self, code, acc):

        self.left.crawler(code, acc + "0")  # налево - "0"
        self.right.crawler(code, acc + "1")  # напрво - "1"

class Foliage(namedtuple("Leaf", ["char"])):  # листья
    def crawler(self, code, acc):
        code[self.char] = acc or "0"

def huffman_code(s):  # код Хаффмана
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Foliage(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)  # элемент с минимальной частотой - левый узел
        freq2, _count2, right = heapq.heappop(h)  # следующий элемент с минимальной частотой - правый узел

        heapq.heappush(h, (freq1 + freq2, count, Branch(left, right)))
        count += 1
    code = {}  # словарь кодов символов
    if h:
        [(_freq, _count, root)] = h
        root.crawler(code, "")
    return code  

def main():
    line = input()  # длина строки  до 10**4
    code = huffman_code(line)
    encoded = "".join(code[ch] for ch in line)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)

if __name__ == "__main__":
    main()
