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


def huffman_tree(input_str):
    
    sorted_s = sorted(Counter(input_str).items(), key=lambda item: item[1])

    while len(sorted_s) > 1:
        weight = sorted_s[0][1] + sorted_s[1][1]
        value =  (sorted_s[0][0], sorted_s[1][0])
        sorted_s[0] = (value, weight)
        sorted_s.pop(1)
        sorted_s.sort(key=lambda v: v[1])

    return sorted_s[0][0]


def huffman_code(tree, code_table = None, path=''):
    if code_table is None:
        code_table = {}
    if not isinstance(tree, tuple | list):
        code_table[tree] = path
    else:
        for idx, el in enumerate(tree):
            huffman_code(el, code_table, f'{path}{idx}')
    return code_table


s = 'beep boop beer!'

code_table = huffman_code(huffman_tree(s))

for i in s:
    print(code_table[i], end=' ')
