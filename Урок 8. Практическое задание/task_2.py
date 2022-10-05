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

'''
1) Использование slots
2) Исключение при валидации
'''


class ValidError(BaseException):
    def __init__(self, info):
        self.info = info


class BinaryTree:
    __slots__ = ['root', 'left_child', "right_child", 'val']

    def __init__(self, val, root_obj=None):
        # корень
        self.root = root_obj if root_obj else self
        # Значение
        self.val = val
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, val):
        if not (type(val) is int and val <= self.val):
            raise ValidError(f"It can't be left child, because new item: {val} is bigger than root: {self.val}")
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(val, self)

        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(val, self)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.insert_left(self.left_child.val)
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, val):
        if not (type(val) is int and val > self.val):
            raise ValidError(f"It can't be left child, because new item: {val} is smaller than root: {self.val}")
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(val, self)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(val, self)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.insert_right(self.right_child.val)
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):

        self.root = BinaryTree(obj)

    # метод доступа к корню
    def get_root_val(self):
        return self.root.val


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_right(60)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
