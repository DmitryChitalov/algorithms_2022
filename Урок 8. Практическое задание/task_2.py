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
        # если у узла нет левого потомка
        try:
            if self.root >= new_node:
                if self.left_child == None:
                    self.left_child = BinaryTree(new_node)
                # если у узла есть левый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            else:
                raise Exception('Ошибка! Значение должно быть меньше корневого значения!')
        except Exception as exc:
            print(exc)

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        try:
            if self.root <= new_node:
                if self.right_child == None:
                    self.right_child = BinaryTree(new_node)
                # если у узла есть правый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
            else:
                raise Exception('Ошибка! Значение должно быть больше корневого значения!')
        except Exception as exc:
            print(exc)

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


tree = BinaryTree(8)
print(tree.get_root_val())  # 8
print(tree.get_left_child())  # None
tree.insert_left(40)  # Ошибка! Значение должно быть меньше корневого значения!
tree.insert_right(40)
print(tree.get_left_child())  # None
print(tree.get_right_child())  # До перегрузки __str__: <__main__.BinaryTree object at 0x000001C226763DF0>
                                    # После - 40
print(tree.get_right_child().get_root_val())  # 40
tree.insert_left(7)
print(tree.get_left_child())  # До перегрузки __str__: <__main__.BinaryTree object at 0x000002CE7D7D3D90>
                                   # После - 7
print(tree.get_right_child().get_root_val())  # 40
