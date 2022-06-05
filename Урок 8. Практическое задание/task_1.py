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


class MyTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None


class HuffmanCode:
    def __init__(self, seq):
        self.seq = seq
        self.sorted_seq = deque(sorted(Counter(seq).items(), key=lambda a: a[1]))
        self.code_dict = {}
        self.fill_dict(self.create_tree())

    def create_tree(self):
        while len(self.sorted_seq) > 1:
            left = self.sorted_seq.popleft()
            right = self.sorted_seq.popleft()
            my_tree = MyTree(right[1] + left[1])
            my_tree.left = left[0]
            my_tree.right = right[0]
            for i, j in enumerate(self.sorted_seq):
                if j[1] < my_tree.root:
                    continue
                else:
                    self.sorted_seq.insert(i, (my_tree, my_tree.root))
                    break
            else:
                self.sorted_seq.append((my_tree, my_tree.root))
        return self.sorted_seq[0][0]

    def fill_dict(self, input_tree, path=''):
        if isinstance(input_tree, str):
            self.code_dict[input_tree] = path
            return
        self.fill_dict(input_tree.left, f'{path}0')
        self.fill_dict(input_tree.right, f'{path}1')

    def to_code(self):
        result = (self.code_dict[x] for x in self.seq)
        return print(' '.join(result))


test = HuffmanCode('beep boop beer!')

test.to_code()
