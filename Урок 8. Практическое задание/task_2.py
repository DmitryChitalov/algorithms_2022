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


class BinTreeNodeExistExc(Exception):
  def __init__(self, node=None):
    self.message = f'Node {node} already exists in the tree'
    super().__init__(self.message)


class BinTreeNodeLeftExc(Exception):
  def __init__(self, node=None):
    self.message = f'Node {node} can not be inserted as left child. It must be smaller than root'
    super().__init__(self.message)

class BinTreeNodeRightExc(Exception):
  def __init__(self, node=None):
    self.message = f'Node {node} can not be inserted as right child. It must be bigger than root'
    super().__init__(self.message)


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def walk(self, leafs_list = []):
        if isinstance(self.left_child, BinaryTree):
            self.left_child.node_validation(leafs_list)
        else:
            leafs_list.append(self.left_child)
        if isinstance(self.right_child, BinaryTree):
            self.right_child.node_validation(leafs_list)
        else:
            leafs_list.append(self.right_child)
        return leafs_list

    def node_validation(self, new_node):
        for i in self.walk():
            if new_node == i:
                raise BinTreeNodeExistExc(new_node)


    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if new_node >= self.get_root_val():
            raise BinTreeNodeLeftExc(new_node)
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            self.node_validation(new_node)
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if new_node <= self.get_root_val():
            raise BinTreeNodeRightExc(new_node)
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            self.node_validation(new_node)
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
