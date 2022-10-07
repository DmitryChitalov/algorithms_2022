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
                raise ValueError("Число больше корня и должно находиться в правой ветви.")
        except ValueError as err:
            print(err)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root <= new_node:
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
            else:
                raise ValueError("Число меньше корня и должно находиться в левой ветви.")
        except ValueError as err:
            print(err)



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


root = BinaryTree(8)
print(root.get_root_val())
print(root.get_left_child())
root.insert_left(29)
print(root.get_left_child())
root.insert_left(5)
print(root.get_left_child().get_root_val())
root.insert_right(6)
print(root.get_right_child())
root.insert_right(10)
print(root.get_right_child().get_root_val())
root.get_right_child().set_root_val(16)
print(root.get_right_child().get_root_val())
