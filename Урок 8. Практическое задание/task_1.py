"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? Тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? Постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

import heapq
from collections import Counter
from collections import deque
from collections import namedtuple


class TreeStructure(namedtuple("TreeStructure", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaves(namedtuple("Leaves", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def haffman_enc(string):
    lst = []
    count_dct = Counter(string)
    sorted_elements = deque(sorted(count_dct.items(), key=lambda item: item[1]))
    for k, v in sorted_elements:
        lst.append((v, len(lst), Leaves(k)))
    heapq.heapify(lst)
    counter = len(lst)
    while len(lst) > 1:
        v1, _count1, left = heapq.heappop(lst)
        v2, _count2, right = heapq.heappop(lst)

        heapq.heappush(lst, (v1 + v2, counter, TreeStructure(left, right)))

        counter += 1
    code = {}
    if lst:
        [(_v, _count, root)] = lst
        root.walk(code, "")
    return code


def main():
    st = 'This is my last lesson!'
    code = haffman_enc(st)
    encoded = "".join(code[el] for el in st)
    for el in sorted(code):
        print(f'Код элемента: {el} >>> {code[el]}')
    print(f"Наша закодированная строка:\n{encoded}")


main()

"""
Сложный материал. Нашел метод реализации с использованием кучи, а также именованных
кортежей. Немного доработал его, попытался вникнуть в суть происходящего и местами даже
вник)
"""

# Код элемента:   >>> 101
# Код элемента: ! >>> 1001
# Код элемента: T >>> 11100
# Код элемента: a >>> 0000
# Код элемента: e >>> 0010
# Код элемента: h >>> 11101
# Код элемента: i >>> 1100
# Код элемента: l >>> 1101
# Код элемента: m >>> 11110
# Код элемента: n >>> 1000
# Код элемента: o >>> 0011
# Код элемента: s >>> 01
# Код элемента: t >>> 0001
# Код элемента: y >>> 11111
# Наша закодированная строка:
# 1110011101110001101110001101111101111110111010000010001101110100100101001110001001
