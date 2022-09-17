from collections import deque
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

class HuffmanDecode:
    def __init__(self, val, letter=None, left_val=None, right_val=None):
        self.letter = letter
        self.val = val
        self.left_val = left_val
        self.right_val = right_val

def search(node, path=''):
    if node.letter is not None:
        node.val = 0
        return node.letter, path

    if node.left_val is not None and node.left_val.val != 0:
        res = search(node.left_val, path=f'{path}0')
        if node.right_val.val == 0 and node.left_val.val == 0:
            node.val = 0
        return res
    if node.right_val.val != 0 and node.right_val is not None:
        res = search(node.right_val, path=f'{path}1')
        if node.right_val.val == 0 and node.left_val.val == 0:
            node.val = 0
        return res

string = input('Введите строку:')
dct = {}
for i in string:
    if i not in dct:
        dct[i] = 1
    else:
        dct
node_list = deque([HuffmanDecode(dct[i], i) for i in dct])

for i in range(len(dct)-1):
    node_list = deque(sorted(node_list, key=lambda node: node.val))
    first_el = node_list.popleft()
    second_el = node_list.popleft()
    new_node = HuffmanDecode(first_el.val + second_el.val, left_val=first_el, right_val=second_el)
    node_list.appendleft(new_node)

tree = node_list[0]

dct_2 = {}
for _ in range(len(dct)):
    k = search(tree)
    dct_2[k[0]] = k[1]
del tree

print('Результат(кодированная строка):')
for i in string:
    print(dct_2[i], end='')
