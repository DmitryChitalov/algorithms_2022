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

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if new_node < self.root:
                # если у узла нет левого потомка
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
                raise Exception('Значение должно быть в правой ветви')
        except Exception as e:
            print(e)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node > self.root:
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
                raise Exception('Значение должно быть в левой ветви')
        except Exception as e:
            print(e)

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


r = BinaryTree(7)
print(r.get_root_val())  # 7
print(r.get_left_child())  # None
r.insert_left(17)  # Значение должно быть в правой ветви
print(r.get_left_child())  # None
r.insert_left(3)
print(r.get_left_child())  # <__main__.BinaryTree object at 0x0000025D777B5C10>
print(r.get_left_child().get_root_val())  # 3
r.insert_right(5)  # Значение должно быть в левой ветви
print(r.get_right_child())  # None
r.insert_right(13)
print(r.get_right_child())  # <__main__.BinaryTree object at 0x000001F69FEA5910>
print(r.get_right_child().get_root_val())  # 13
