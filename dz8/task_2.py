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


# Создал свое исключение
class MyErrorInsert(Exception):

    def __init__(self, message='Вставка не может быть выполнена, так как потомок не соответсвует вставке.'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, num):
        # Вызываю собственное исключение, если потомок больше корня
        if num >= self.root:
            raise MyErrorInsert
        if self.left_child is None:
            self.left_child = BinaryTree(num)
        else:
            tree_obj = BinaryTree(num)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    def insert_right(self, num):
        # Вызываю собственное исключение, если потомок меньше корня
        if num <= self.root:
            raise MyErrorInsert
        if self.right_child is None:
            self.right_child = BinaryTree(num)
        else:
            tree_obj = BinaryTree(num)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

'''
Создал собственное исключение MyErrorInsert,
и вызываю это исключение при попытке вставки правого потомка меньше корня, 
или левого потомка больше корня.
'''