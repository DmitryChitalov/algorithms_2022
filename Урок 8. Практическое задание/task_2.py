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


class BinaryTreeError(Exception):
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
        try:
            if self.left_child is None and self.root > new_node:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            elif self.left_child is not None and self.root > new_node:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
            else:
                raise BinaryTreeError(f'Элемент "{new_node}" >= корня "{self.root}" - '
                                      f'вставка влево невозможна!')
        except BinaryTreeError as e:
            print(e)

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        try:
            if self.right_child is None and self.root <= new_node:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
            elif self.right_child is not None and self.root <= new_node:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
            else:
                raise BinaryTreeError(f'Элемент "{new_node}" < корня "{self.root}" - '
                                      f'вставка вправо невозможна!')
        except BinaryTreeError as err:
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


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())

r.insert_left(6)
r.insert_left(40)

print(r.get_left_child())

try:
    print(f'left > {r.get_left_child().get_root_val()}')
except AttributeError:
    print("No child on the left!")

r.insert_right(5)

print(r.get_right_child())

try:
    print(f'right > {r.get_right_child().get_root_val()}')
except AttributeError:
    print("No child on the right!")

r.insert_right(12)

print(f'right > {r.get_right_child().get_root_val()}')

r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

# 8
# None
# Элемент "40" >= корня "8" - вставка влево невозможна!
# <__main__.BinaryTree object at 0x000001B91EA88388>
# left > 6
# Элемент "5" < корня "8" - вставка вправо невозможна!
# None
# No child on the right!
# right > 12
# 16
