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
from collections import namedtuple


class Tree(namedtuple("Tree", ["left", "right"])):

    def walk(self, code, pref):
        self.left.walk(code, pref + "0")
        self.right.walk(code, pref + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, pref):
        code[self.char] = pref or "0"


def haffman_encode(str_obj):
    line = []
    for symbol, weight in Counter(str_obj).items():
        line.append((weight, len(line), Leaf(symbol)))
    heapq.heapify(line)
    count = len(line)
    while len(line) > 1:
        weight1, _count1, left = heapq.heappop(line)
        weight2, _count2, right = heapq.heappop(line)
        heapq.heappush(line, (weight1 + weight2, count, Tree(left, right)))
        count +=1
    code = {}
    if line:
        [(_weight, _count, root)] = line
        root.walk(code, "")
        return code


def main():
    s = input('Введите строку: ')
    code = haffman_encode(s)
    encoded = "".join(code[symbol] for symbol in s)
    for symbol in code:
        print(f'{symbol}: {code[symbol]}')
    print(encoded)


if __name__ == '__main__':
    main()