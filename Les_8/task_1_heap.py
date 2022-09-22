"""
идею использовать heapq подсмотрела в интернете
но с деком понятнее, на мой взгляд
обнаружила, что два слова с "одинаковой" структурой кодируются одинаково, возникают вопросы к декодированию
"""

import heapq
from collections import Counter, namedtuple


# классы для хранения информации о структуре дерева
class Node(namedtuple("Node", ["left", "right"])):
    # пропишем метод обхода
    def walk(self, code, code_sym):
        self.left.walk(code, code_sym + "0")  # пойти влево, "0"
        self.right.walk(code, code_sym + "1")  # пойти вправо, "1"


class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева
    def walk(self, code, code_sym):
        # потомков нет, поэтому пишем сам символ или 0, если символов нет
        code[self.char] = code_sym or "0"


def huffman_code(s):
    h = []  # список для очереди
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        # последовательно извлекаем 2 элемента с наименьшими частотами
        freq1, cnt1, left = heapq.heappop(h)
        freq2, cnt2, right = heapq.heappop(h)
        # поместим в очередь новый элемент, с частотой равной сумме частот
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))  # закидываем в кучу
        count += 1
    code = {}  # словарик с кодировкой
    if h:
        [(freq, cnt, root)] = h
        root.walk(code, "")  # пройдём от корня до листьев и соберём кодировку
    return code


s = 'abababacadee'
s1 = 'bcbcbcbdbeff'
code = huffman_code(s)
code1 = huffman_code(s1)
encoded = " ".join(code[ch] for ch in s)
encoded1 = " ".join(code1[ch] for ch in s1)

for ch in code:
    print(f'{ch}: {code[ch]}')
print(encoded)
print(encoded1)
