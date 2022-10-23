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
from collections import Counter, deque, namedtuple


class TreeStructure(namedtuple("TreeStructure", ["left", "right"])):
    def walk(self, code, sym):
        self.left.walk(code, sym + '0')
        self.right.walk(code, sym + '1')


class Leaves(namedtuple("Leaves", ["char"])):
    def walk(self, code, sym):
        code[self.char] = sym or '0'


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


def main(st='Hello, world!'):
    code = haffman_enc(st)
    encoded = "".join(code[el] for el in st)
    for el in sorted(code):
        print(f'Код элемента: {el} >>> {code[el]}')
    print(f"Закодированная по Хаффману строка:\n{encoded}")


main()
main('What a wonderful world')
