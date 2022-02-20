"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
from collections import deque, Counter

class Huffman:

    __slots__ = ("_letter_tree", "_huffman_code", "__code_table", "source_string")

    def __init__(self, letter_tree, source_string):
        self.source_string = source_string
        self._letter_tree = letter_tree
        self.__code_table = dict()
        self._huffman_code = str()

        self.__create_huffman_table(self._letter_tree)


    def __create_huffman_table(self, tree: dict, path: str = ""):
        if not isinstance(tree, dict):
            self.__code_table[tree] = path
        else:
            self.__create_huffman_table(tree[0], path=f'{path}0')
            self.__create_huffman_table(tree[1], path=f'{path}1')

    def __create_huffman_code(self):
        for letter in self.source_string:
            self._huffman_code += self.__code_table[letter]

    @staticmethod
    def get_sorted_letters(source_string: str) -> deque:
        letter_frequency = Counter(source_string)
        return deque(reversed(letter_frequency.most_common()))

    @classmethod
    def create_from_string(cls, source_string: str):
        sorted_letters = cls.get_sorted_letters(source_string=source_string)
        if len(sorted_letters) != 1:
            while len(sorted_letters) > 1:
                weight = sorted_letters[0][1] + sorted_letters[1][1]
                subtree = {
                    0: sorted_letters.popleft()[0],
                    1: sorted_letters.popleft()[0]
                }
                for index, element in enumerate(sorted_letters):
                    if weight > element[1]:
                        continue
                    else:
                        sorted_letters.insert(index, (subtree, weight))
                        break
                else:
                    sorted_letters.append((subtree, weight))
        else:
            weight = sorted_letters[0][1]
            subtree = {
                0: sorted_letters.popleft()[0],
                1: None
            }
            sorted_letters.append((subtree, weight))
        return cls(letter_tree=sorted_letters[0][0], source_string=source_string)

    @property
    def get_tree(self) -> dict:
        return self._letter_tree

    @property
    def get_table(self) -> dict:
        return self.__code_table

    @property
    def get_huffman_code(self):
        self.__create_huffman_code()
        return self._huffman_code


if __name__ == "__main__":
    s = "beep boop beer!"
    tree = Huffman.create_from_string(s)
    print("tree", tree.get_tree)
    print("code_table", tree.get_table)
    print("code", tree.get_huffman_code)
