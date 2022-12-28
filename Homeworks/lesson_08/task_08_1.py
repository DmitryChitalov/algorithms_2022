"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? Тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма.
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? Постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque


class HuffmanNode:
    def __init__(self, left_child=None, right_child=None):
        self.left_child = left_child
        self.right_child = right_child


def create_huffman_tree(string):
    values_frequency_deque = deque(sorted(Counter(string).items(), key=lambda item: item[1]))
    if len(values_frequency_deque) != 1:
        while len(values_frequency_deque) > 1:
            weight_new_node = values_frequency_deque[0][1] + values_frequency_deque[1][1]
            new_node = HuffmanNode(values_frequency_deque.popleft()[0], values_frequency_deque.popleft()[0])
            for idx, node in enumerate(values_frequency_deque):
                if weight_new_node <= node[1]:
                    values_frequency_deque.insert(idx, (new_node, weight_new_node))
                    break
            else:
                values_frequency_deque.append((new_node, weight_new_node))
    else:
        weight_new_node = values_frequency_deque[0][1]
        new_node = HuffmanNode(values_frequency_deque.pop(), None)
        values_frequency_deque.append((new_node, weight_new_node))
    return values_frequency_deque[0][0]


def create_encoded_values_dict(dct, tree, path=''):
    if not isinstance(tree, HuffmanNode):
        dct[tree] = path
    else:
        create_encoded_values_dict(dct, tree.left_child, path=f'{path}0')
        create_encoded_values_dict(dct, tree.right_child, path=f'{path}1')


if __name__ == '__main__':
    string_test = "beep boop beer!"
    encoded_values_dict = {}
    create_encoded_values_dict(encoded_values_dict, create_huffman_tree(string_test))

    for value, encoded_value in encoded_values_dict.items():
        print(f'{value} --> {encoded_value}')
