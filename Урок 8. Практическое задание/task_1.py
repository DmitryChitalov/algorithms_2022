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
        # проверка на соотвествие значения правилу бинарного дерева
        if self.root <= new_node:
            return print(f"Число {new_node} больше или равно значению корня, введите его в функцию добавления правого потомка.")
        # если у узла нет левого потомка
        elif self.left_child == None:
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
        if self.root > new_node:
            return print(f"Число {new_node} меньше значения корня, введите его в функцию добавления левого потомка.")
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

    # методы обхода значений дерева
def in_order(root):
    if root:
        in_order(root.left_child)
        print(root.root)
        in_order(root.right_child)


def pre_order(root):
    if root:
        print(root.root)
        pre_order(root.left_child)
        pre_order(root.right_child)



r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
r.insert_left(6)
r.insert_left(8)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
r.insert_right(7)
r.insert_right(8)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
pre_order(r)
in_order(r)



"""
 Cам не придумывал, врать не буду, но нашел и разобрал еще такую реализацию. Показалась тоже интересной.
 Тут отдельной функцией вставка сразу делается к правым или левым потомкам.
 Ну, и обходы представлены.
"""

# class Node:
#     def __init__(self, val):
#         self.l_child = None
#         self.r_child = None
#         self.data = val
#
# def binary_insert(root, node):
#     if root is None:
#         root = node
#     else:
#         if root.data > node.data:
#             if root.l_child is None:
#                 root.l_child = node
#             else:
#                 binary_insert(root.l_child, node)
#         else:
#             if root.r_child is None:
#                 root.r_child = node
#             else:
#                 binary_insert(root.r_child, node)
#
# def in_order_print(root):
#     if not root:
#         return
#     in_order_print(root.l_child)
#     print(root.data)
#     in_order_print(root.r_child)
#
# def pre_order_print(root):
#     if not root:
#         return
#     print(root.data)
#     pre_order_print(root.l_child)
#     pre_order_print(root.r_child)
#
# r = Node(3)
# binary_insert(r, Node(7))
# binary_insert(r, Node(1))
# binary_insert(r, Node(5))
#
# print("in order:")
# in_order_print(r)
# print("pre-order:")
# pre_order_print(r)
