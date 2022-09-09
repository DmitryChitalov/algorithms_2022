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

from __future__ import annotations

from collections import Counter, deque


class Node:
    def __init__(
            self,
            frequency: int,
            char: str,
            left: Node = None,
            right: Node = None
    ):

        self.frequency = frequency
        self.char = char
        self.left = left
        self.right = right
        self.code = ''


class Huffman:
    def __init__(self, string: str):
        self.string = string
        self.tree = self._build_tree()
        self.char_codes = self._get_codes(self.tree)
        self.bin_string = self._encode()

    def _build_tree(self) -> Node:
        chars_freq = Counter(self.string)
        nodes = deque([Node(freq, char) for char, freq in sorted(chars_freq.items(), key=lambda item: item[1])])

        while len(nodes) > 1:
            right = nodes.popleft()
            left = nodes.popleft()

            left.code = 0
            right.code = 1

            new_node = Node(left.frequency + right.frequency, left.char + right.char, left, right)
            nodes.append(new_node)

        return nodes[0]

    def _get_codes(
            self,
            node: Node,
            codes: dict = None,
            value: str = '') -> dict:

        if codes is None:
            codes = dict()

        new_value = value + str(node.code)
        if node.left:
            self._get_codes(node.left, codes, new_value)
        if node.right:
            self._get_codes(node.right, codes, new_value)
        if not node.left and not node.right:
            codes[node.char] = new_value

        return codes

    def _encode(self) -> str:
        encoding_output = [self.char_codes[char] for char in self.string]
        return ''.join([str(item) for item in encoding_output])

    def get_encoded(self) -> str:
        return self.bin_string

    def get_char_codes(self) -> dict:
        return self.char_codes

    def get_tree(self) -> Node:
        return self.tree


if __name__ == '__main__':

    test_string = "beep boop beer!"
    huffman = Huffman(test_string)
    print(huffman.get_encoded())
