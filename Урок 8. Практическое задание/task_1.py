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


class Node:
    def __init__(self, l_child=None, r_child=None):
        self.l_child = l_child
        self.r_child = r_child


class Haffman:
    def __init__(self, obj):
        self.obj = obj
        self.desk: deque = None

    def create_desk(self):
        """
        создем  доску
        считаем эелементы
        расспологаем их по возврастанию
        """
        self.desk = deque(sorted(Counter(self.obj).items(), key=lambda key: key[1]))

    def build_tree(self):
        """
        Строим дерево
        полуаем эелементы, создаем ветку, добавляем новый элемен на доску
        """
        while len(self.desk) > 1:
            elem_1 = self.desk.popleft()
            elem_2 = self.desk.popleft()

            weight = elem_1[1] + elem_2[1]
            node = Node(elem_1[0], elem_2[0])

            for i in range(len(self.desk)):
                if self.desk[i][1] < weight:
                    continue
                else:
                    self.desk.insert(i, (node, weight))
                    break
            else:
                self.desk.append((node, weight))
        return self.desk[0][0]


decoded = dict()


def decode_haffman(obj, path=''):
    if not isinstance(obj, Node):
        decoded[obj] = path
    else:
        decode_haffman(obj.l_child, f'{path}0')
        decode_haffman(obj.r_child, f'{path}1')


a = Haffman("beep boop beer!")

a.create_desk()
tree = a.build_tree()
print(tree)
decode_haffman(tree)
print(decoded)
