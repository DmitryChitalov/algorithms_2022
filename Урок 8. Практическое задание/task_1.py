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

"""
Ну, вроде получилось, получается, что чтобы потом этот код разобрать, нужно вместе с текстом передавать частоты и в 
приемнике строить такое же дерево.
"""

from collections import Counter, deque


class BinaryTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class HaffmanTree:
    def __init__(self):
        self._code = []

    def encode(self, string):
        self._walk(self.build(string))

    def build(self, string):
        def __build(seq):
            if len(seq) == 1:
                return seq[0]

            el1, el2 = seq.popleft(), seq.popleft()
            weight = el1[1] + el2[1]
            new_el = BinaryTree(left=el1[0], right=el2[0])

            if len(seq) <= 0:
                seq.insert(0, new_el)
                return seq[0]
            else:
                for i in range(len(seq)):
                    if seq[i][1] >= weight:
                        seq.insert(i, (new_el, weight))
                        break
                    if i == len(seq) - 1:
                        seq.append((new_el, weight))
                __build(seq)
            return seq[0]

        return __build(self._initial(string))

    def _walk(self, node, left=None):
        if left is not None:
            self._code.append('0') if left else self._code.append('1')
        if isinstance(node, str):
            # print(node, self._code)
            print(''.join(self._code), end='')
            self._code.pop()
            return
        self._walk(node.left, True)
        self._walk(node.right, False)
        if len(self._code) > 0:
            self._code.pop()

    def _initial(self, string):
        return deque(sorted(dict(Counter(string)).items(), key=lambda i: i[1]))


if __name__ == '__main__':
    s = 'beep boop beer!'
    ht = HaffmanTree()
    ht.encode(s)
