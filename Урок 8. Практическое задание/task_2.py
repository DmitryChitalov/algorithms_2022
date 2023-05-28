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

"""
1) Максим Салтыков
2) Алгоритмы и структуры данных на Python. Базовый курс
3) дату старта курса(именно курса, а не обучения) 
4) номер урока 260931
5) номер профиля 4389736
"""

from typing import Union


class DependenceException(Exception):
    """

    """

    def __init__(self, message="Изменение значения может нарушить правила дерева"):
        self.message = message
        super().__init__(self.message)

class BinaryTree:
    def __init__(self, root_obj, root = True):
        self.is_root = root
        self.is_leaf = True
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if new_node > self.root:
            raise ValueError('Must be smaller than root/ Должно быть меньше корня')
        else:
            if self.left_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node,False)
                self.is_leaf = False
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node,False)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if new_node < self.root:
            raise ValueError('Must be bigger than root/ должно быть больше корня')
        else:
            if self.right_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node,False)
                self.is_leaf = False
            # если у узла есть правый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node,False)
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
        if self.is_root == False: # Значение можно менять только если нода является корнем
            raise DependenceException
        else:
            self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def graft(self, tree: "BinaryTree", right: bool) -> "Union[BinaryTree, None]":
        """
        Прививает дерево tree к правой или левой ветке корня, в зависимости от значения right
        Возвращает предыдущее значение ветки
        :param tree: subtree to be added
        :param right: True - right branch, False - left branch
        :return:
        """
        if type(tree) is not BinaryTree:
            raise ValueError("Must be BinaryTree")
        tree.is_root = False
        self.is_leaf = False
        if right == True:
            if tree.get_root_val() < self.root:
                raise ValueError('Must be bigger than root/ должно быть больше корня')
            buf = self.right_child
            self.right_child = tree
            return buf
        else:
            if tree.get_root_val() > self.root:
                raise ValueError('Must be smaller than root/ должно быть меньше корня')
            buf = self.left_child
            self.left_child = tree
            return buf



r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
try:
    r.insert_left(40)
except ValueError:
    r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
try:
    r.get_right_child().set_root_val(16)
except DependenceException:
    r.insert_right(16)
print(r.get_right_child().get_root_val())
subtree = BinaryTree(18)
subtree.insert_right(19)
subtree.insert_left(17)
r.get_right_child().graft(subtree, True)
print(r.get_right_child().get_right_child().get_root_val())
print(r.get_right_child().get_right_child().get_right_child().get_root_val())
print(r.get_right_child().get_right_child().get_left_child().get_root_val())
