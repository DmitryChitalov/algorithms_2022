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
        if new_node < self.root:
            # если у узла нет левого потомка
            if self.left_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.insert_left(self.left_child.root)
                self.left_child = tree_obj
        elif new_node > self.root:
            self.insert_right(new_node)
            print('Новый потомок больше корня, и будет добавлен вправо!')
        else:
            print('Невозможно добавить потомка, со значением равным корню!')

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node > self.root:
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
                tree_obj.insert_right(self.right_child.root)
                self.right_child = tree_obj
        elif new_node < self.root:
            self.insert_left(new_node)
            print('Новый потомок меньше корня, и будет добавлен влево!')
        else:
            print('Невозможно добавить потомка, со значением равным корню!')

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
r.insert_left(12)  # пытаемся добавить больший элемент влево
print(r.right_child.get_root_val())  # получаем предупреждение, и видим, что больший элемент добавился в право
r.insert_left(6)
print(r.left_child.get_root_val())  # добавление элемента удовлетворяющего валидацию прошло корректно
r.insert_left(8)  # проверили случай с равным корню значением
r.insert_left(5)  # вставили нового потомка
print(r.left_child.get_root_val())  # проверили этого нового потомка
print(r.left_child.right_child.get_root_val())  # проверили, то что спущенный потомок, занял верное место
# 6 больше 5, и поэтому потомок ушел в право
