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


class BinaryTree:
    __slots__ = ['root', 'left_child', 'right_child']

    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def __str__(self):
        return str(self.root)

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if self.root >= new_node:
                if self.left_child is None:
                    self.left_child = BinaryTree(new_node)
                else:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            else:
                raise Exception('Value error!')
        except Exception as e:
            print(e)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root <= new_node:
                if self.right_child is None:
                    self.right_child = BinaryTree(new_node)
                else:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
            else:
                raise Exception('Value error!')
        except Exception as e:
            print(e)

    def get_right_child(self):
        try:
            return self.right_child
        except AttributeError:
            print('Error accessing class attribute')

    def get_left_child(self):
        try:
            return self.left_child
        except AttributeError:
            print('Error accessing class attribute')

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        try:
            return self.root
        except AttributeError:
            print('Error accessing class attribute')


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(89)
r.insert_left(2)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(120)
r.insert_right(1)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(3)
print(r.get_right_child().get_root_val())
