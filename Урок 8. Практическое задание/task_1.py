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
from collections import deque, Counter

class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

class Hoffman:
    def __init__(self, string):
        self.string = string
        self.new_string = deque(sorted(Counter(string).items(), key=lambda x: x[1]))
        self.code = {}
        self.unready_tree = self.make_tree
        self.make_code_dict(self.make_tree())

    def make_tree(self):
        while len(self.new_string) > 1:
            left = self.new_string.popleft()
            right = self.new_string.popleft()
            hoff_tree = Tree(right[1] + left[1])
            hoff_tree.left = left[0]
            hoff_tree.right = right[0]
            for i, cnt in enumerate(self.new_string):
                if cnt[1] < hoff_tree.root:
                    continue
                else:
                    self.new_string.insert(i, (hoff_tree, hoff_tree.root))
                    break

            else:
                self.new_string.append((hoff_tree, hoff_tree.root))
        return self.new_string[0][0]

    def make_code_dict(self, tree, path=''):
        if isinstance(tree, str):
            self.code[tree] = path
            return
        self.make_code_dict(tree.left, f'{path}0')
        self.make_code_dict(tree.right, f'{path}1')

    def encoding(self):
        result = (self.code[x] for x in self.string)
        return ''.join(result)

word = 'beep boop beer!'
obj = Hoffman(word)

print(f'Таблица расшифровки - {obj.code}')
print(f'Фраза - {word}\nВ кодировке - {obj.encoding()}')























