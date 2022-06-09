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
    def __init__(self, key, count, left=None, right=None):
        self.key = key
        self.count = count
        self.left = left
        self.right = right
        self.code = ''


def get_huffman_dict(huff_str: str) -> dict:
    node_list = [Node(k, v) for k, v in Counter(huff_str).items()]
    while len(node_list) > 1:
        node_list.sort(key=lambda item: item.count, reverse=True)
        node_left = node_list.pop()
        node_right = node_list.pop()
        node_left.code = '0'
        node_right.code = '1'
        if node_left.count > node_right.count:
            node_left, node_right = node_right, node_left
        new_node = Node('', node_left.count + node_right.count, left=node_left, right=node_right)
        node_list.append(new_node)

    def create_code_dict(node: Node, code_dict: dict, code: str = '') -> dict:
        if node.left:
            create_code_dict(node.left, code_dict, f'{code}{node.code}', )
            create_code_dict(node.right, code_dict, f'{code}{node.code}', )
        else:
            code_dict[node.key] = f'{code}{node.code}'
        return code_dict

    return create_code_dict(node_list[0], {})


def get_huffman_code(string: str) -> str:
    huffman_dict = get_huffman_dict(string)
    return ''.join((huffman_dict[x] for x in string))


s = 'beep boop beer!'

print(get_huffman_dict(s))
print(get_huffman_code(s))
