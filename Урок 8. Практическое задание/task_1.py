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

from collections import Counter, deque


class BinaryTree:

    def __init__(self, new_root, left=None, right=None):
        self.root = new_root
        self.left = left
        self.right = right


class Haffman:

    def __init__(self, s):
        self.code_table = dict()
        self.str_to_code = s
        self.count = Counter(self.str_to_code)
        self.sorted_str = deque(sorted(self.count.items(), key=lambda item: item[1]))
        self.tree = self.build_tree()
        self.build_code(self.tree)

    def build_tree(self):
        while len(self.sorted_str) > 1:
            l = self.sorted_str.popleft()
            r = self.sorted_str.popleft()
            new_tree = BinaryTree(l[1] + r[1], l[0], r[0])
            for i, j in enumerate(self.sorted_str):
                if j[1] < new_tree.root:
                    continue
                else:
                    self.sorted_str.insert(i, (new_tree, new_tree.root))
                    break
            else:
                self.sorted_str.append((new_tree, new_tree.root))

        return self.sorted_str[0][0]

    def build_code(self, tree, path=''):
        if type(tree) == str:
            self.code_table[tree] = path
            return
        self.build_code(tree.left, f'{path}0')
        self.build_code(tree.right, f'{path}1')

    def get_code(self):
        res = []
        for i in self.str_to_code:
            res.append(self.code_table[i])
        return ' '.join(res)


s = Haffman('beep boop beer!')

for i, j in s.code_table.items():
    print(f'"{i}": {j}')
print(f'code: {s.get_code()}')
