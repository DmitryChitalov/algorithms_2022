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


class Haffman:
    def __init__(self):
        self.tree = None
        self.code = ''
        self.table = {}
        self.text = ''

    def __make_tree(self, left: tuple, right: tuple):
        l_el, l_col = left
        r_el, r_col = right
        el = {0: l_el, 1: r_el}
        key = l_col + r_col
        return key, el

    def __haffman_code(self):
        for sym in self.text:
            self.code += self.table[sym]

    def __haffman_table(self, tree, code=''):
        if type(tree) != dict:
            self.table.setdefault(tree, code)
        else:
            self.__haffman_table(tree[0], code=code + '0')
            self.__haffman_table(tree[1], code=code + '1')

    def encode(self, text):
        self.text = text
        sorted_tuple = deque(sorted(Counter(text).items(), key=lambda x: x[1]))
        while len(sorted_tuple) >= 0:
            key, tree = self.__make_tree(sorted_tuple.popleft(), sorted_tuple.popleft())
            for idx, el in enumerate(sorted_tuple):
                if el[1] >= key:
                    sorted_tuple.insert(idx, (tree, key))
                    break
                elif idx == len(sorted_tuple) - 1:
                    sorted_tuple.append((tree, key))
                    break
            if len(sorted_tuple) == 0:
                self.tree = tree
                break
        self.__haffman_table(self.tree)
        self.__haffman_code()
        return self.code, self.tree

    def decode(self, code: str, tree: dict):
        self.tree = tree
        self.code = code
        self.__haffman_table(self.tree)
        table = {v: k for k, v in self.table.items()}
        code = ''
        self.text = ''
        for sym in self.code:
            code += sym
            if code in table:
                self.text += table[code]
                code = ''
        return self.text


s1 = Haffman()
s2 = Haffman()
c, t = s1.encode('Кодирование и декодирование Хаффмана')
print(s2.decode(code=c, tree=t))
print('tree:', s1.tree)
print('code:', s1.code)

