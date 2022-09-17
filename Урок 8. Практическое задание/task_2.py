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


class SideError(Exception):
    """Базовый класс для других исключений"""
    pass


class RightValueTooSmallError(SideError):
    """Вызывается, когда правое входное значение мало"""
    pass


class LeftValueTooLargeError(SideError):
    """Вызывается, когда левое входное значение велико"""
    pass


class BinaryTree:
    __slots__ = ['root', 'left_child', 'right_child']

    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # def __str__(self):
    #     return f"{self.root}"

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if self.root < new_node:
                raise LeftValueTooLargeError
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
            print(f"Левый потомок {new_node} успешно добавлен.")
        except LeftValueTooLargeError:
            print(f'Левый потомок должен быть меньше корня {self.root}. Добавляется {new_node}.')

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root > new_node:
                raise RightValueTooSmallError
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
            print(f"Правый потомок {new_node} успешно добавлен.")
        except RightValueTooSmallError:
            print(f'Правый потомок должен быть больше корня {self.root}. Добавляется {new_node}.')

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
print(f'Корень: {r.get_root_val()}.')
print(f'Левый потомок: {r.get_left_child()}.')
r.insert_left(40)
r.insert_left(4)
print(f'Левый потомок (объект): {r.get_left_child()}.')
print(f'Значение объекта "Левый потомок": {r.get_left_child().get_root_val()}.')
r.insert_right(1)
r.insert_right(20)
print(f'Прай потомок (объект): {r.get_right_child()}.')
print(f'Значение объекта "Правый потомок": {r.get_right_child().get_root_val()}.')
r.get_right_child().set_root_val(16)  # Заменили значение правого потомка.
print(f'Новое значение объекта "Правый потомок": {r.get_right_child().get_root_val()}.')
