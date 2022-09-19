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


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['symbol'])):
    def walk(self, code, acc):
        code[self.symbol] = acc


def huffman_encode(any_str):
    queue = []
    for ch, freq in Counter(any_str).items():
        queue.append((freq, len(queue), Leaf(ch)))
    heapq.heapify(queue)
    # Counter(any_str)
    count = len(queue)
    while len(queue) > 1:
        freq_1, _count_1, left = heapq.heappop(queue)
        freq_2, _count_2, right = heapq.heappop(queue)
        heapq.heappush(queue, (freq_1 + freq_2, count, Node(left, right)))
        count += 1
    [(elem, _count, root)] = queue
    code = {}
    root.walk(code, '')
    return code


def main():
    user_str = input('Введите строку: ')
    code = huffman_encode(user_str)
    encoded = ''.join(code[sym] for sym in user_str)
    for sym in code:
        print(f'{sym}: {code[sym]}')
    print(encoded)


if __name__ == '__main__':
    main()
