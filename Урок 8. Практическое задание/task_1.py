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

from collections import deque


class GetNode:

    def __init__(self, value, letter=None, left=None, right=None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right


def search(node, path='',):

    if node.letter is not None:
        node.value = 0
        return node.letter, path
    if node.right is not None and node.right.value != 0:
        spam = search(node.right, path=f'{path}1')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam
    if node.left is not None and node.left.value != 0:
        spam = search(node.left, path=f'{path}0')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam


unencoded_string = input('Input some string:')

string_dict = {}
for i in unencoded_string:
    if i not in string_dict:
        string_dict[i] = 1
    else:
        string_dict[i] += 1

node_list = deque([GetNode(string_dict[i], i) for i in string_dict])

for i in range(len(string_dict)-1):

    node_list = deque(sorted(node_list, key=lambda node: node.value))

    first_el = node_list.popleft()
    second_el = node_list.popleft()

    new_node = GetNode(first_el.value + second_el.value, left=first_el, right=second_el)

    node_list.appendleft(new_node)

tree = node_list[0]

node_tree = {}
for _ in range(len(string_dict)):
    k = search(tree)
    node_tree[k[0]] = k[1]

print(node_tree)

print(f'Unencoded string:\n{unencoded_string}')

print('Coded string:')
for char in unencoded_string:
    print(node_tree[char], end=' ')


