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
from task_2 import Node
from collections import Counter, deque
from operator import itemgetter


class HfNode(Node):

    def __init__(self, weight, ch=None):
        super().__init__(weight)
        self.ch = ch

    def insert_left(self, new_node):
        pass

    def insert_right(self, new_node):
        pass

    def __str__(self):
        return f'{self.weight}-{self.ch}'

    @staticmethod
    def create_node_from2(left, right):
        new_node = HfNode(left.weight + right.weight, f'{left.ch} {right.ch}')
        new_node.left, new_node.right = left, right
        return new_node

    def set_root(self, weight, ch):
        super().set_root(weight)
        self.ch = ch


class HuffmanGraph:
    def __init__(self, val):
        if len(val) == 0:
            raise Exception('Empty string!')
        sort = self.find_freq(val)
        # Инициализируем листья в очереди
        deq = deque([HfNode(j[1], j[0]) for j in sort])
        while len(deq) > 1:
            # Берем 2 крайних левых листа и делаем из них новый лист.
            newnode = HfNode.create_node_from2(deq.popleft(), deq.popleft())
            # Вставляем новый лист в очередь так, чтобы вес листа был меньше или равен весу следущего листа.
            for i, item in enumerate(deq):
                if newnode.weight <= item.weight:
                    deq.insert(i, newnode)
                    break
            else: # вставляем в конец
                deq.append(newnode)
        self.root = deq[0]

    @staticmethod
    def find_freq(val):
        return sorted(Counter(s).items(), key=itemgetter(1))

    @staticmethod
    def haffman_code(node, code_table, path=''):
        if isinstance(node.get_left(), HfNode):
            hg.haffman_code(node.get_left(), code_table, path=f'{path}0')
        if isinstance(node.get_right(), HfNode):
            hg.haffman_code(node.get_right(), code_table, path=f'{path}1')
        if node.isleaf():
            code_table[node.ch] = path


s = "beep boop beer!"
# s = ""
print(HuffmanGraph.find_freq(s))
hg = HuffmanGraph(s)
hg.haffman_code(hg.root, code_table := {}, path='')
print(code_table)
hg.root.draw()
