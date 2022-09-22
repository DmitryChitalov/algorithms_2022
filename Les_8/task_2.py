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

"""
Добавила отлавливание ошибки вставки слева/справа
исправила баг с выдачей рута, если ветки нет
"""


class DirectionError(Exception):
    pass


class GetRootError(AttributeError):
    pass


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
            if new_node > self.root:
                raise DirectionError
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except DirectionError:
            print(f'{new_node} нельзя вставить слева')

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                raise DirectionError
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        except DirectionError:
            print(f'{new_node} нельзя вставить справа')

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


try:
    r = BinaryTree(8)
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left(40)
    print(r.get_left_child())
    r.insert_right(12)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(16)
    print(r.get_right_child().get_root_val())
    print(r.get_left_child().get_root_val())

except AttributeError:
    print('Ошибка считывания данных из дерева: нельзя вывести root, если ветка пуста')
