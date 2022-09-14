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


class HaffmanTree:
    def __init__(self, lobj=None, robj=None):
        self.left_branch = lobj
        self.right_branch = robj

    def encode(self, mystring):
        string_counter = Counter(mystring)
        string_deque = deque(sorted(string_counter.items(), key=lambda item: item[1]))
        while len(string_deque) > 1:
            new_node = HaffmanTree(string_deque[0][0], string_deque[1][0])
            new_node_val = string_deque[0][1] + string_deque[1][1]
            string_deque.popleft()
            string_deque.popleft()
            for i in range(0, len(string_deque)):
                if string_deque[i][1] >= new_node_val:
                    string_deque.insert(i, (new_node, new_node_val))
                    break
            else:
                if len(string_deque) > 0 and string_deque[0][1] >= new_node_val:
                    string_deque.appendleft((new_node, new_node_val))
                else:
                    string_deque.append((new_node, new_node_val))
        self.left_branch = string_deque[0][0].left_branch
        self.right_branch = string_deque[0][0].right_branch
        return self

    def walk(self, code_dict, code=''):
        if isinstance(self.left_branch, HaffmanTree):
            self.left_branch.walk(code_dict, code + '0')
        else:
            code_dict[self.left_branch] = code + '0'
        if isinstance(self.right_branch, HaffmanTree):
            self.right_branch.walk(code_dict, code + '1')
        else:
            code_dict[self.right_branch] = code + '1'
        return code_dict


mytree = HaffmanTree()
mydict = dict()
mytree.encode('beep boop beer!')

print(mytree.walk(mydict))

