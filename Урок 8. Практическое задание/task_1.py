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

from collections import Counter
from collections import deque


class BinaryTree:
    __slots__ = ['root', 'left_child', "right_child"]

    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None


def huffman_code(s):
    sorted_elements = deque(sorted(Counter(s).items(), key=lambda item: item[1]))
    while len(sorted_elements) > 1:
        weight = sorted_elements[0][1] + sorted_elements[1][1]
        left = sorted_elements.popleft()
        right = sorted_elements.popleft()
        node = BinaryTree(weight)
        node.left_child = left[0]
        node.right_child = right[0]
        for idx, element in enumerate(sorted_elements):
            if element[1] < node.root:
                continue
            else:
                sorted_elements.insert(idx, (node, node.root))
                break
        else:
            sorted_elements.append((node, node.root))
    return sorted_elements[0][0]


code_dict = {}


def create_code(tree, val=''):
    if not isinstance(tree, BinaryTree):
        code_dict[tree] = val

    else:
        create_code(tree.left_child, val=f'{val}0')
        create_code(tree.right_child, val=f'{val}1')


s = 'beep boop beer!'

create_code(huffman_code(s))

for i in s:
    print(f'"{i}" : {code_dict[i]}')
