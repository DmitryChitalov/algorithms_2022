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


class BinaryTree:
    def __init__(self, value, left_child=None, right_child=None):
        self.right_child = right_child
        self.left_child = left_child
        self.value = value


def get_code(root, codes=dict(), path=''):
    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = path
        return codes

    get_code(root.left_child, codes, path + '0')
    get_code(root.right_child, codes, path + '1')

    return codes


def get_tree(string):
    freq_analysis = Counter(string)

    if len(freq_analysis) <= 1:
        node = BinaryTree(None)

        if len(freq_analysis) == 1:
            node.left_child = BinaryTree([key for key in freq_analysis][0])
            node.right_child = BinaryTree(None)

        freq_analysis = {node: 1}

    while len(freq_analysis) > 1:
        node = BinaryTree(None)
        spam = freq_analysis.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left_child = BinaryTree(spam[0][0])

        else:
            node.left_child = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right_child = BinaryTree(spam[1][0])

        else:
            node.right_child = spam[1][0]

        del freq_analysis[spam[0][0]]
        del freq_analysis[spam[1][0]]
        freq_analysis[node] = spam[0][1] + spam[1][1]

    return [key for key in freq_analysis][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

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


def is_correct(string, decode_str):
    return string == decode_str


my_string = input('Введите строку для сжатия: ')
tree = get_tree(my_string)
print(f'Исходная строка: "{my_string}", занимает бит: {len(my_string) * 8}')

codes = get_code(tree)
print(f'Коды символов: {codes}')

coding_str = coding(my_string, codes)
print(f'Кодированная строка: "{coding_str}", занимает бит: {len(coding_str)}')

decoding_str = decoding(coding_str, codes)
print('Раскодированная строка: ', decoding_str)

print('Декодировано правильно:', is_correct(my_string, decoding_str))
