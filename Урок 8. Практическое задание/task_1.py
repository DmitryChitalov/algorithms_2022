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

# Создаем класс для хранения информации о структуре дерева
class Structure(namedtuple("Node", ["left", "right"])):

    def enum(self, code, res):
        self.left.enum(code, res + "0")
        self.right.enum(code, res + "1")

# Cоздаем класс для хранения листьев отдельно, т.к. у них нет потомков

class Foliage(namedtuple("Foliage", ["char"])):

    def enum(self, code, res):
        code[self.char] = res or "0"

# функция кодирования, решил использовать алгоритм очереди кучи
def h_encode(data):
    h = []
    for char, freq in Counter(data).items():
        h.append((freq, len(h), Foliage(char)))
        heapq.heapify(h)
        count = len(h)
        while len(h) > 1:
            freq1, _count_1, left = heapq.heappop(h)
            freq2, _count_2, right = heapq.heappop(h)

            heapq.heappush(h, (freq1 + freq2, count, Structure(left, right)))

            count +=1
        code = {}

        if h:[(_freq, _count, root)] = h
        root.enum(code, "")

    return code

# функция вывода текста из "закодированных" данных
def h_decode(enc, code):
    h = []
    enc_ch = ""
    for char in enc:
        enc_ch += char
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                h.append(dec_ch)
                enc_ch = ""
                break
    return "".join(h)


def main():
    sentence = "beep boop beer!"
    сode = h_encode(sentence)
    encoded = "".join(сode[ch] for ch in sentence)

    for el in sorted((сode)):
        print(f"'{el}': {сode[el]}")
    print(encoded)
    print(h_decode(encoded, сode))

main()
