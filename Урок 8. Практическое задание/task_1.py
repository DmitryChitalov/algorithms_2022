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

def create_nodes(nod):
    while len(nod) > 1:
        left_child = nod.pop()
        right_child = nod.pop()
        node = Node(freq=left_child.freq+right_child.freq, left=left_child, right=right_child)
        nod.append(node)
    return node
def haffman_code(up_nd, code=''):
    if up_nd.symbol:
        return {up_nd.symbol: code}
    symbol_codes = dict()
    symbol_codes.update(haffman_code(up_nd.left, code + '0'))
    symbol_codes.update(haffman_code(up_nd.right, code + '1'))
    return symbol_codes

def haffman_decode(encoder_string, root_node):
    result = ''
    node = root_node
    for letter in encoder_string:
        node = node.left if letter == '0' else node.right
        if node.symbol:
            result += node.symbol
            node = root_node
    return result

if __name__ == "__main__":
    data_in = input('Введите значение для  кодирования -    ')
    nodes = [Node(*item) for item in sorted(Counter(data_in).items(), key=lambda x: x[1], reverse=True)]
    root = create_nodes(nodes)
    code_str = haffman_code(root)
    code = ''.join(code_str[str] for str in data_in)
    decod = haffman_decode(code, root)
    print("Введенное число - ", data_in)
    print("Бинарник :", "".join([format(ord(check), 'b') for check in data_in]))
    print("Закодированное значение: ", code)
    print("Декодированное значение: ", decod)