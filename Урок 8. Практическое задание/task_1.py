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


class Node:

    def __init__(self, val, left=None, right=None):
        self.right = right
        self.left = left
        self.val = val


def get_code(root, codes=dict(), code=''):
    if root is None:
        return
    if isinstance(root.val, str):
        codes[root.val] = code
        return codes
    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')
    return codes


def get_tree(string):
    str_count = Counter(string)
    if len(str_count) <= 1:
        node = Node(None)
        if len(str_count) == 1:
            node.left = Node([key for key in str_count][0])
            node.right = Node(None)
        str_count = {node: 1}
    while len(str_count) != 1:
        node = Node(None)
        item = str_count.most_common()[:-3:-1]
        if isinstance(item[0][0], str):
            node.left = Node(item[0][0])
        else:
            node.left = item[0][0]
        if isinstance(item[1][0], str):
            node.right = Node(item[1][0])
        else:
            node.right = item[1][0]
        del str_count[item[0][0]]
        del str_count[item[1][0]]
        str_count[node] = item[0][1] + item[1][1]
    return [key for key in str_count][0]


def coding(string, codes):
    res = ''
    for el in string:
        res += codes[el]
    return res


def decoding(string, codes):
    res = ''
    i = 0
    while i < len(string):
        for code in codes:
            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])
    return res


user_string = "beep boop beer!"
print(f'Исходная строка: {user_string}')
tree = get_tree(user_string)

codes = get_code(tree)
print(f'Таблица c кодами: {codes}')

coding_string = coding(user_string, codes)
print(f'Кодированная строка: {coding_string}')

decoding_string = decoding(coding_string, codes)
print(f'Декодированная строка: {decoding_string}')
