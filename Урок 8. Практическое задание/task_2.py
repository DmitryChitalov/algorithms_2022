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


class BTError(Exception):
    pass


class BinaryTree:
    __slots__ = ['root', 'left_child', 'right_child']         # сработает ли это и есть ли смысл?

    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если значние нового узла больше или равно корню, он не может быть левым потомком
        if new_node >= self.root:
            raise BTError('Элемент не может быть левым потомком.')
        else:
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
    def insert_right(self, new_node):
        # если значние нового узла меньше корня, он не может быть правым потомком
        if new_node < self.root:
            raise BTError('Элемент не может быть правым потомком.')
        else:
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
        if self.right_child is None:
            raise BTError('У узла нет правого потомка')
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        if self.left_child is None:
            raise BTError('У узла нет левого потомка')
        return self.left_child


    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        if self.root is None:
            raise BTError('элемент отсутствует')
        else:
            return self.root


try:
    r = BinaryTree(8)
    print(r.get_root_val())          # 8
#   print(r.get_left_child())        # нет левого потомка
#   r.insert_left(40)                # Элемент не может быть левым потомком
    r.insert_right(40)               # добавили справа узел 40
#    print(r.get_left_child())       # У узла нет левого потомка
#    print(r.get_left_child().get_root_val())   # У узла нет левого потомка
#   r.insert_right(6)                # Элемент не может быть правым потомком
    r.insert_left(6)                 # добавили слева узел 40
    print(r.get_right_child())          #<__main__.BinaryTree object at 0x000001E7D3906740>
    print(r.get_right_child().get_root_val())       # 40
    r.get_right_child().set_root_val(16)            # установили узлу 40 значение 16
    print(r.get_right_child().get_root_val())       # 16
except BTError as e:
    print('Произошла ошибка: ', e)
