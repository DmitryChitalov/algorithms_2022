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


class ValidateException(Exception):
    def __init__(self, root, branch):
        self.root = root
        self.branch = branch

    def __str__(self):
        if self.root > self.branch:
            return f'{self.branch} меньше {self.root} - добавьте в левую ветку'
        return f'{self.branch} не меньше {self.root} - добавьте в правую ветку'


class BinaryTree:
    def __init__(self, root_obj, parent=None):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        # родитель
        self.parent = parent

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node >= self.root:
            raise ValidateException(self.root, new_node)
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node, parent=self)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node, parent=self)
            # меняем имеющемуся потомку родителя на новый узел
            self.left_child.parent = tree_obj
            # и спускаем имеющегося потомка на один уровень ниже
            # в левую или правую ветку
            if tree_obj.root > self.left_child.root:
                tree_obj.left_child = self.left_child
            else:
                tree_obj.right_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:
            raise ValidateException(self.root, new_node)
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node, parent=self)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node, parent=self)
            self.right_child.parent = tree_obj
            # и спускаем имеющегося потомка на один уровень ниже
            if tree_obj.root > self.right_child.root:
                # если новый узел больше имеющегося, спускаем в левую ветку
                tree_obj.left_child = self.right_child
            else:
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
        # проверяем родителя и на какой ветке находится потомок, чтобы правильно установить корень
        if (self.parent.left_child == self and obj < self.parent.root) or \
                (self.parent.right_child == self and obj >= self.parent.root):
            self.root = obj
        else:
            raise ValidateException(self.parent.root, obj)

    # метод доступа к корню
    def get_root_val(self):
        return self.root


try:
    r = BinaryTree(8)
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left(4)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right(12)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(16)
    print(r.get_right_child().get_root_val())
except ValidateException as e:
    print(e)
