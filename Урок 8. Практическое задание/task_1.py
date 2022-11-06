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
from collections import  Counter
from collections import  namedtuple

class Wood(namedtuple("Wood",["left", "right"])):
    def walk (self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Sheet (namedtuple("Sheet",["char"])):
    def walk(self,code,acc):
        code[self.char] = acc or "0"

def huffman_encode(s):
    line = []
    for symbol , freq in Counter(s).items():
        line.append((freq, len(line), Sheet(symbol)))
    heapq.heapify(line)
    count = len(line)
    while len(line) > 1:
        freq1, _count2, left = heapq.heappop(line)
        freq2, _count2, right = heapq.heappop(line)
        heapq.heappush(line, (freq1 + freq2, count, Wood(left, right)))

        count += 1
    code = {}
    if line:
        [(_freq, _count, root)] = line
        root.walk(code, "")
        return code

def main():
    s = input("Введите строку: ")
    code = huffman_encode(s)
    encoded = "".join(code[symbol] for symbol in s)
    for symbol in code:
        print(f'{symbol}: {code[symbol]}')
    print(encoded)

if __name__ == '__main__':
    main()