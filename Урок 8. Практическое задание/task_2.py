"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, weight=None):
        # корень
        self.weight = weight
        # левый потомок
        self.left = None
        # правый потомок
        self.right = None

    def __str__(self):
        return f'{self.weight}'

    # добавить левого потомка
    def insert_left(self, new_node):
        if self.weight < new_node.weight:
            raise Exception(f'{self.weight}>{new_node.weight}')
            # если у узла нет левого потомка
        if self.left == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left = new_node
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            if self.left.weight > new_node.weight:
                raise Exception(f'{self.left.weight}>{new_node.weight}')
            tree_obj = new_node
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left = self.left
            self.left = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка

        if self.weight > new_node.weight:
            raise Exception(f'{self.weight}>{new_node.weight}')

        if self.right == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right = new_node
        # если у узла есть правый потомок
        else:
            if self.right.weight < new_node.weight:
                raise Exception(f'{self.right.weight}<{new_node.weight}')

            # тогда вставляем новый узел
            tree_obj = new_node
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right = self.right
            self.right = tree_obj

    # метод доступа к правому потомку
    def get_right(self):
        return self.right

    # метод доступа к левому потомку
    def get_left(self):
        return self.left

    def isleaf(self):
        if not isinstance(self.left, Node) and not isinstance(self.right, Node):
            return True
        else:
            return False

    # метод установки корня
    def set_root(self, val):
        self.weight = val


    '''
    Прорисовка графа. На вход идет лист. Дальше в граф добавляются рекурсивно подчиненные листья.  
    '''

    def draw(self):

        mygraph = MyGraph(self)
        mygraph.add_nodes(mygraph.node)
        mygraph.draw()


class MyGraph:

    def __init__(self, node):
        self.node = node
        self.graph = nx.Graph()
        self.graph.add_node(node)

    def add_edge(self, f_item, s_item):
        self.graph.add_edge(f_item, s_item)
        self.graph.add_edge(s_item, f_item)

    def add_nodes(self, tree):

        if isinstance(tree.left, Node):
            self.graph.add_node(tree.left)
            self.add_edge(tree, tree.left)
            self.add_nodes(tree.left)

        if isinstance(tree.right, Node):
            self.graph.add_node(tree.right)
            self.add_edge(tree, tree.right)
            self.add_nodes(tree.right)

    def draw(self):
        nx.draw_circular(self.graph,
                         node_color='red',
                         node_size=1000,
                         with_labels=True)
        plt.show()


def test():
    r = Node(8)
    print(r)
    print(r.get_left())
    print(r.get_right())
    leaf3 = Node(3)
    r.insert_left(leaf3)
    leaf4 = Node(4)
    leaf3.insert_right(leaf4)
    leaf2 = Node(1)
    leaf3.insert_left(leaf2)
    leaf5 = Node(5)
    r.insert_left(leaf5)
    print(r.left)
    r.draw()

if __name__ =='__main__':
    test()

