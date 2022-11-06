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

"""Кодирование методом Хафмана ООП"""

from collections import Counter, deque


class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(str_obj):
    count_str = Counter(str_obj)

    sorted_str = deque(sorted(count_str.items(), key=lambda item: item[1]))

    while len(sorted_str) > 1:

        weight = sorted_str[0][1] + sorted_str[1][1]
        node = MyNode(left=sorted_str.popleft()[0], right=sorted_str.popleft()[0])

        for i, item in enumerate(sorted_str):
            if weight > item[1]:
                continue
            else:
                sorted_str.insert(i, (node, weight))
                break
        else:
            sorted_str.append((node, weight))

    return sorted_str[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, MyNode):
        code_table[tree] = path

    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


str_obj = "beep boop beer!"

haffman_code(haffman_tree(str_obj))

for i in str_obj:
    print(code_table[i], end=' ')

print()
