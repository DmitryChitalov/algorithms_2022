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
    def __init__(self, symbol=None, freq=0, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right


def make_tree(nodes):
    while len(nodes) > 1:
        left_child = nodes.pop()
        right_child = nodes.pop()
        node = Node(freq=left_child.freq+right_child.freq, left=left_child, right=right_child)
        nodes.append(node)

    return node


def encode_huffman(root_node, code=''):
    if root_node.symbol:
        return {root_node.symbol: code}

    symbol_codes = dict()
    symbol_codes.update(encode_huffman(root_node.left, code + '0'))
    symbol_codes.update(encode_huffman(root_node.right, code + '1'))
    return symbol_codes


def decode_huffman(encoder_string, root_node):
    result = ''
    node = root_node
    for letter in encoder_string:
        node = node.left if letter == '0' else node.right
        if node.symbol:
            result += node.symbol
            node = root_node
    return result


if __name__ == "__main__":
    input_string = input('Enter the string: ')
    nodes = [Node(*item) for item in sorted(Counter(input_string).items(), key=lambda x: x[1], reverse=True)]
    root = make_tree(nodes)
    symbol_codes = encode_huffman(root)
    encoded = ''.join(symbol_codes[letter] for letter in input_string)
    decoded = decode_huffman(encoded, root)
    print("You have entered: ", input_string)
    print("-"*100)
    print("Original binary: ", "".join([format(ord(letter), 'b') for letter in input_string]))
    print("Encoded string: ", encoded)
    print("Decoded string: ", decoded)
