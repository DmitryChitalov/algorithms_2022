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


class BinaryTree:
    def __init__(self, left_child = None, right_child = None):
        self.code_table = dict()
        self.left_child = left_child
        self.right_child = right_child


    def hafman_tree(self, s):
        count = Counter(s)
        sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(sorted_elements) != 1:
            while len(sorted_elements) > 1:
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                self.comb = BinaryTree(left_child=sorted_elements.popleft()[0], right_child=sorted_elements.popleft()[0])
                for i, _count in enumerate(sorted_elements):
                    if weight > _count[1]:
                        continue
                    else:
                        sorted_elements.insert(i, (self.comb, weight))
                        break
                else:
                    sorted_elements.append((self.comb, weight))
        else:
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((comb, weight))
        return sorted_elements[0][0]



    def haffman_code(self, tree, path=''):
        if not isinstance(tree, BinaryTree):
            self.code_table[tree] = path
        else:
            self.haffman_code(tree.left_child, path=f'{path}0')
            self.haffman_code(tree.right_child, path=f'{path}1')




s = "beep boop beer!"
s1 = "oop"
res = BinaryTree()
res.haffman_code(res.hafman_tree(s))
bin_str = [res.code_table[i] for i in s]
print('encode')
print(*bin_str)
print(15*'*')
print(*[res.code_table[i] for i in s1])
print(15*'*')
print('decode')
str_ = ''
decode = ''
for i in bin_str:
    str_ += i
    for key, val in res.code_table.items():
        if val == str_:
            decode += key
            str_ = ''

print(decode)