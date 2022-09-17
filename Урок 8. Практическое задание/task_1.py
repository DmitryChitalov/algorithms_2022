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

from recordclass import recordclass


class Node(recordclass('Node', ['left', 'right'])):
    def walk(self, code, way):
        self.left.walk(code, f'{way}0')
        self.right.walk(code, f'{way}1')


class Leaf(recordclass('Leaf', ['char'])):
    def walk(self, code, way):
        code[self.char] = way or '0'  # '0' для повторяющихся букав.


def huffman_encode(my_str):
    heap_list = []
    for sign, freq in Counter(my_str).items():
        heap_list.append((freq, len(heap_list), Leaf(sign)))

    heapq.heapify(heap_list)

    count = len(heap_list)
    while len(heap_list) > 1:
        freq_1, count_1, left = heapq.heappop(heap_list)  # count_1, чтобы при сравнении ошибки не выдавало.
        freq_2, count_2, right = heapq.heappop(heap_list)  # count_2, чтобы при сравнении ошибки не выдавало.
        heapq.heappush(heap_list, (freq_1 + freq_2, count, Node(left, right)))  # Добавляется в конец одинаковых.
        count += 1

    code = {}
    if heap_list:  # Для пустой строки.
        [(freq, count, root)] = heap_list
        root.walk(code, '')
    for key, val in code.items():
        print(f'{key}: {val}')
    new_str = ''
    for let in my_str:
        new_str = f'{new_str}{code[let]} '
    return new_str


print(huffman_encode('abra cadabra'))
print(huffman_encode('beep boop beer!'))
print(huffman_encode('aaaaaaaaa'))
print(ascii(huffman_encode('')))
