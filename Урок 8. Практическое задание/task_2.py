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


class BinaryTreeException(Exception):
    pass


class NodeExist(BinaryTreeException):
    def __init__(self):
        super().__init__(f'Node already exists')


class ValueGreaterThanRoot(BinaryTreeException):
    def __init__(self):
        super().__init__(f'Node value greater than root')


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def validation(func):
        def wrapper(self, new_node):
            if self.get_root_val() < new_node:
                raise ValueGreaterThanRoot
            if new_node in [node.get_root_val() for node in self.walk_tree()]:
                raise NodeExist
            return func(self, new_node)
        return wrapper

    def walk_tree(self):
        nodes = [self]
        if self.left_child:
            nodes.extend(self.left_child.walk_tree())
        if self.right_child:
            nodes.extend(self.right_child.walk_tree())
        return nodes

    # добавить левого потомка
    @validation
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
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

    # добавить правого потомка
    @validation
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
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

    def __str__(self):
        return f"Node[{self.root}]"


if __name__ == "__main__":
    try:
        r = BinaryTree(8)
        print(r.get_root_val())
        print(r.get_left_child())
    except BinaryTreeException as e:
        print(f"Got {e} exception")

    try:
        r.insert_left(40)
        print(r.get_left_child())
        print(r.get_left_child().get_root_val())
    except BinaryTreeException as e:
        print(f"Got {e} exception")

    try:
        r.insert_right(7)
        print(r.get_right_child())
        print(r.get_right_child().get_root_val())
    except BinaryTreeException as e:
        print(f"Got {e} exception")

    try:
        r.get_right_child().set_root_val(7)
        print(r.get_right_child().get_root_val())
    except BinaryTreeException as e:
        print(f"Got {e} exception")

    try:
        r.insert_left(7)
        print(r.left_child().get_root_val())
    except BinaryTreeException as e:
        print(f"Got {e} exception")
