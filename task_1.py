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


# Узел дерева
class Node():
    def __init__(self, symbol='', weight=0):
        self.left = None
        self.right = None
        self.symbol = symbol  # Символ
        self.weight = weight  # Вес


# Построение дерева
def huffman_tree(s):
    freq = Counter(s)
    nodes = [Node(x, freq[x]) for x in freq.keys()]
    for _ in range(len(freq)-1):
        nodes.sort(key=lambda n: n.weight)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node('', left.weight + right.weight)
        parent.left = left
        parent.right = right
        nodes.insert(0,parent)
    return nodes.pop()


# Кодировка
def haffman_code(tree):
    code_table = {}

    def tree_traversal(tree, path):
        if tree.left:
            tree_traversal(tree.left, f'{path}0')
        if tree.right:
            tree_traversal(tree.right, f'{path}1')
        if tree.symbol != '':
            code_table[tree.symbol] = path

    tree_traversal(tree, '')
    return code_table


# тестирование
s = "beep boop beer!"
res = haffman_code(huffman_tree(s))
for i, item in enumerate(res.items()):
    print(f"{i+1}. '{item[0]}' ---> {item[1]}")
print('-------------------')
for x in s:
    print(res[x], end=' ')
print()