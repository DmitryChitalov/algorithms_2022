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


class BinaryTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(my_text):
    count_el = Counter(my_text)
    sorted_el = deque(sorted(count_el.items(), key=lambda items: items[1]))
    while len(sorted_el) > 1:
        weight = sorted_el[0][1] + sorted_el[1][1]
        node = BinaryTree(left=sorted_el.popleft()[0], right=sorted_el.popleft()[0])
        for i, item in enumerate(sorted_el):
            if weight > item[1]:
                continue
            else:
                sorted_el.insert(i, (node, weight))
                break
        else:
            sorted_el.append((node, weight))
    return sorted_el[0][0]


def haffman_code(tree, path=''):
    if not isinstance(tree, BinaryTree):
        code_table[tree] = path
    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


code_table = dict()
text = "beep boop beer!"
haffman_code(haffman_tree(text))
print(code_table)
for s in text:
    print(code_table[s], end=' ')
