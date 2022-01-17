"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if self.root < new_node:
                raise ValueError
            if self.left_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except ValueError:
            print('You cannot input value bigger than root here!')

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root > new_node:
                raise ValueError
                # если у узла нет правого потомка
            if self.right_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        except ValueError:
            print('You cannot input value less than root here!')

    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            return self.left_child
        except AttributeError:
            return None

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            return self.left_child
        except AttributeError:
            return None

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        try:
            return self.root
        except AttributeError:
            print()


r = BinaryTree(8)
print(r.get_root_val())  # OK
print(r.get_left_child())  # None
r.insert_left(40)  # ValueError
print(r.get_left_child())  # None
print(r.get_left_child().get_root_val())  # Error
r.insert_right(12)  # OK
print(r.get_right_child())  # 12
print(r.get_right_child().get_root_val())  # 8
r.get_right_child().set_root_val(16)  # 8
print(r.get_right_child().get_root_val())  # 16?
