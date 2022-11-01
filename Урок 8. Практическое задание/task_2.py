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
class ErrorBinTree(Exception):
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


    def __str__(self):
        return str(self.root)

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            # если у узла нет левого потомка
            if self.root >= new_node:
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
            else:
                raise ErrorBinTree('Значение левого потомка больше корня!')
        except ErrorBinTree as txt:
            print(txt)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root <= new_node:
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
            else:
                raise ErrorBinTree('Значение правого потомка меньше корня!')
        except ErrorBinTree as txt:
            print(txt)

    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            return self.right_child
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            return self.left_child
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')

    # метод установки корня
    def set_root_val(self, obj):
        try:
            self.root = obj
        except TypeError:
            print('Недопустимый атрибут корня!')


    # метод доступа к корню
    def get_root_val(self):
        try:
            return self.root
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')



r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
print(r.get_right_child())
r.insert_left(65)
r.insert_left(7)
r.insert_right(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print('--------------------------------------------------------------------------------------------------------------')
r.set_root_val(7)
print(r.get_root_val())
print(r.get_left_child())
print(r.get_right_child())
print('--------------------------------------------------------------------------------------------------------------')
r.insert_left(5)
r.insert_right(14)
print(r.get_left_child())
print(r.get_right_child())
r.insert_left(3)
r.insert_right(18)
print(r.get_left_child())
print(r.get_right_child())

print(type(r.get_right_child()))