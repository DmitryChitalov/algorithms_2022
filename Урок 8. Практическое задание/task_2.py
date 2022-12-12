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

from sys import exit


# Добавлено исключение
class RootValueError(Exception):

    def __init__(self, message=None):
        if message:
            self.message = message


class BinaryTree:
    def __init__(self, root_obj, parent_val=None, is_left=None):
        """Добавлены атрибуты parent_val и is_left,
        Используются для проверки корректности значения узла-потомка"""
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        self.parent_val = parent_val
        self.is_left = is_left

    # добавить левого потомка
    def insert_left(self, new_node):
        if not new_node < self.root:  # Проверка и генерация исключения
            raise RootValueError(f'Некоректное значение узла: {new_node}.')
        else:
            # если у узла нет левого потомка
            if self.left_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node, parent_val=self.root, is_left=True)
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                if new_node < self.left_child.get_root_val():  # Проверка и генерация исключения
                    raise RootValueError(f'Некоректное значение узла: {new_node}.')
                else:
                    tree_obj = BinaryTree(new_node, parent_val=self.root, is_left=True)
                    # и спускаем имеющегося потомка на один уровень ниже
                    self.left_child.parent_val = new_node  # Перенос значения узла-родителя в узел-потомок
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:  # Проверка и генерация исключения
            raise RootValueError(f'Некоректное значение узла: {new_node}.')
        else:
            # если у узла нет правого потомка
            if self.right_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node, parent_val=self.root, is_left=False)
            # если у узла есть правый потомок
            else:
                if not new_node < self.right_child.get_root_val():  # Проверка и генерация исключения
                    raise RootValueError(f'Некоректное значение узла: {new_node}.')
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node, parent_val=self.root, is_left=False)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child.parent_val = new_node  # Перенос значения узла-родителя в узел-потомок
                    self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        if self.is_left:
            if not obj < self.parent_val:  # Проверка и генерация исключения
                raise RootValueError(f'Некоректное значение узла: {obj}.')
        else:
            if obj < self.parent_val:  # Проверка и генерация исключения
                raise RootValueError(f'Некоректное значение узла: {obj}.')
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


"""
r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
"""

# Мой клиентский код
tree = BinaryTree(100)
print(f'Корень дерева: {tree.get_root_val()}')
tree.insert_left(90)
print(f'Создан левый потомок: {tree.left_child.get_root_val()}')
tree.insert_right(110)
print(f'Создан правый потомок: {tree.right_child.get_root_val()}')
tree.insert_right(105)
print(f'Вставка узла между корнем и правым потомком: {tree.right_child.get_root_val()}')
print(f'Правый потомок от корня: {tree.right_child.get_root_val()}')
print(f'Правый потомок правого потомка: {tree.right_child.right_child.get_root_val()}')
tree.right_child.right_child.set_root_val(150)
print(f'Изменение значения узла правого потомка правого потомка: {tree.right_child.right_child.get_root_val()}')
print('Вставка левого потомка правого потомка правого потомка с генерацией исключения: ')
tree.right_child.right_child.insert_left(200)
