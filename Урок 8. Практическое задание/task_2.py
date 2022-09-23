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

    # добавить правого потомка
    def insert_right(self, new_node):
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

    def insert_child(self, new_node):
        n = new_node if isinstance(new_node, int) else new_node.root
        if n < self.root:
            if self.left_child:
                a = self.left_child
                self.left_child = BinaryTree(new_node) if isinstance(new_node, int) else new_node
                self.left_child.insert_child(a)
            else:
                self.left_child = BinaryTree(new_node) if isinstance(new_node, int) else new_node

        else:
            if self.right_child:
                a = self.right_child
                self.right_child = BinaryTree(new_node) if isinstance(new_node, int) else new_node
                self.right_child.insert_child(a)

            else:
                self.right_child = BinaryTree(new_node) if isinstance(new_node, int) else new_node

    def __str__(self):
        return f"Root: {self.root}, \n" \
               f"left - {self.left_child.root if self.left_child else '-'}, " \
               f"right - {self.right_child.root if self.right_child else '-'}"


r = BinaryTree(8)
r.insert_child(40)
r.insert_child(12)
r.insert_child(3)
r.insert_child(5)
print(r)
print("****")
print(r.left_child)
print("****")
print(r.right_child)

"""
Вместо валидации значений я добавила функцию "insert_child", которая сама разбирается,
налево вставить потомка, или направо
И перегрузила метод __str__, чтобы результаты проще было увидеть
"""
