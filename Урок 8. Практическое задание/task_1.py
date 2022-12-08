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
from collections import Counter, deque


class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(s):
    count_s = Counter(s)

    sorted_s = deque(sorted(count_s.items(), key=lambda item: item[1]))

    while len(sorted_s) > 1:

        weight = sorted_s[0][1] + sorted_s[1][1]
        node = MyNode(left=sorted_s.popleft()[0], right=sorted_s.popleft()[0])

        for i, item in enumerate(sorted_s):
            if weight > item[1]:
                continue
            else:
                sorted_s.insert(i, (node, weight))
                break
        else:
            sorted_s.append((node, weight))

    return sorted_s[0][0]


def haffman_code(tree, path=''):
    if not isinstance(tree, MyNode):
        code_table[tree] = path
    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


code_table = dict()

s = input('Введите строку: ')

haffman_code(haffman_tree(s))

for i in s:
    print(code_table[i], end=' ')

