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
from collections import Counter, deque


class HuffmanCode:
    class _Node:
        def __init__(self, left_side=None, right_side=None):
            self.left_side = left_side
            self.right_side = right_side

    def __init__(self, string: str):
        self.string = string
        self._tree = self._huffman_tree()
        self.__code_table = dict()

    @property
    def byte_string(self):
        return ' '.join(format(ord(s), 'b') for s in self.string)

    def _huffman_tree(self) -> _Node:
        frequencies = deque(sorted(Counter(self.string).items(), key=lambda item: item[1]))

        while len(frequencies) != 1:
            weight = frequencies[0][1] + frequencies[1][1]
            node = self._Node(left_side=frequencies.popleft()[0], right_side=frequencies.popleft()[0])

            for idx, item in enumerate(frequencies):
                if weight < item[1]:
                    frequencies.insert(idx, (node, weight))
                    break
            else:
                frequencies.append((node, weight))
        return frequencies[0][0]

    def _huffman_code(self, tree: _Node, path: str = ''):
        if isinstance(tree, self._Node):
            self._huffman_code(tree.left_side, path=f'{path}0')
            self._huffman_code(tree.right_side, path=f'{path}1')
        else:
            self.__code_table[tree] = path

    @property
    def huffman_code(self):
        output_tree = self._tree
        self._huffman_code(output_tree)
        return ' '.join(self.__code_table.values())


if __name__ == '__main__':
    s = "beep boop beer!"
    k = 'Lol Kek Cheburek'
    code = HuffmanCode(s)
    code2 = HuffmanCode(k)
    print('Before:', code.byte_string)
    print('After:', code.huffman_code)
    print()
    print('Before:', code2.byte_string)
    print('After:', code2.huffman_code)
