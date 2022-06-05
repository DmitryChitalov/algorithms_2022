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


class MyError(Exception):
    def __init__(self, text):
        self.txt = text

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
        # если у узла нет левого потомка

        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            try:
                if new_node < self.root:
                    self.left_child = BinaryTree(new_node)
                else:
                    raise MyError('Данный узел нужно вставлять справа')
            except TypeError:
                print('Введите число в качестве атрибута потомка')
            except MyError as mr:
                print(mr)
        # если у узла есть левый потомок
        else:
            try:
                if new_node < self.left_child.root:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
                else:
                    raise MyError('Данный узел нужно вставлять справа')
            except TypeError:
                print('Введите число в качестве атрибута потомка')
            except MyError as mr:
                print(mr)

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            try:
                if new_node > self.root:
                    self.right_child = BinaryTree(new_node)
                else:
                    raise MyError('Данный узел нужно вставлять cлева')
            except TypeError:
                print('Введите число в качестве атрибута потомка')
            except MyError as mr:
                print(mr)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            try:
                if new_node > self.right_child.root:
                    tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
                else:
                    raise MyError('Данный узел нужно вставлять cлева')
            except TypeError:
                print('Введите число в качестве атрибута потомка')
            except MyError as mr:
                print(mr)

    # метод доступа к правому потомку
    def get_right_child(self):
        if self.right_child:
            return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        if self.left_child:
            return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        if self.root:
            self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


try:
    r = BinaryTree(8)
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left(4)
    r.insert_left(6)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right(30)
    r.insert_right(2)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(16)
    print(r.get_right_child().get_root_val())
except AttributeError:
    print('Ветвь не найдена')




