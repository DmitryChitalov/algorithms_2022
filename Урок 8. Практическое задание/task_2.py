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

    def __str__(self):
        return "[%s, %s, %s]" % (self.left_child, str(self.root), self.right_child)

    def is_empty(self):
        return self.left_child == self.right_child == self.root == None

    def insert(self, val):
        if self.is_empty():
            self.val = val
        elif val < self.root:
            if self.left_child is None:
                self.left_child = BinaryTree(val)
            else:
                self.left_child.insert(val)
        else:
            if self.right_child is None:
                self.right_child = BinaryTree(val)
            else:
                self.right_child.insert(val)

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


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert(65)
print(r.get_right_child())
r.insert(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.insert(2)
r.insert(53)
print(r.get_right_child())
print(r.get_left_child())
