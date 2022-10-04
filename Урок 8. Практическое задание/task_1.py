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


class HaffmanTree:
    def __init__(self, left=None, right=None):
        self.left_branch = left
        self.right_branch = right

    def encode(self, my_string):
        str_counter = Counter(my_string)
        str_deque = deque(sorted(str_counter.items(), key=lambda item: item[1]))
        while len(str_deque) > 1:
            new_node = HaffmanTree(str_deque[0][0], str_deque[1][0])
            new_node_val = str_deque[0][1] + str_deque[1][1]
            str_deque.popleft()
            str_deque.popleft()
            for i, val in enumerate(str_deque):
                if val[1] >= new_node_val:
                    str_deque.insert(i, (new_node, new_node_val))
                    break
            else:
                if len(str_deque) > 0 and str_deque[0][1] >= new_node_val:
                    str_deque.appendleft((new_node, new_node_val))
                else:
                    str_deque.append((new_node, new_node_val))
        self.left_branch = str_deque[0][0].left_branch
        self.right_branch = str_deque[0][0].right_branch
        return self

    def walk(self, code_dict={}, code=''):
        if isinstance(self.left_branch, HaffmanTree):
            self.left_branch.walk(code_dict, code + '0')
        else:
            code_dict[self.left_branch] = code + '0'
        if isinstance(self.right_branch, HaffmanTree):
            self.right_branch.walk(code_dict, code + '1')
        else:
            code_dict[self.right_branch] = code + '1'
        return code_dict


my_tree = HaffmanTree()
my_tree.encode('beep boop beer!')

print(my_tree.walk())
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
