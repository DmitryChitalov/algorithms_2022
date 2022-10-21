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
from heapq import heapify, heappop, heappush
from collections import Counter
class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __lt__(self, other):
        return isinstance(other, str)

    def __gt__(self, other):
        return isinstance(other, str)

    def pr(self, pref=''):
        if isinstance(self.left, Tree):
            yield from self.left.pr(f'{pref}0')
        else:
            yield self.left, f'{pref}0'
        if isinstance(self.right, Tree):
            yield from self.right.pr(f'{pref}1')
        else:
            yield self.right, f'{pref}1'



def encode_haffman(st):
    heap = [(i, v) for v, i in Counter(st).items()]
    heapify(heap)
    print(heap)

    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        heappush(heap, (a[0]+b[0], Tree(a[1], b[1])))

    tabl = heappop(heap)[1]

    h = {k: v for k, v in tabl.pr()}
    d_h = {v: k for k, v in tabl.pr()}
    return ''.join([h[i] for i in st]), d_h


st, dct = encode_haffman(input())

tmp = ''
for i in st:
    tmp += i
    if tmp in dct.keys():
        print(dct[tmp], end='')
        tmp=''