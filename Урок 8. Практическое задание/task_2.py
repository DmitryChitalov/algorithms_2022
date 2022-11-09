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
# валидация try exept
'''
Бинарное поисковое дерево (BST) — где для каждого узла выполняется условие, чтобы все
узлы в левом поддереве были меньше этого узла, а все узлы в правом поддереве — больше.
Такое дерево еще называют упорядоченным.
'''


class InsertException(Exception):
    def __init__(self, txt):
        self.txt = txt


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if self.root <= new_node:
                raise InsertException(f"В левом узле значение ({new_node}) должно быть меньше корня ({self.root})")
        except InsertException as err:
            print(err)
            return
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
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root > new_node:
                raise InsertException(f"В правом узле значение ({new_node}) должно быть больше \
или равно корню ({self.root})")
        except InsertException as err:
            print(err)
            return
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


r = BinaryTree(8)
print(f'корень {r.get_root_val()}')
print(f'левый узел {r.get_left_child()}')
r.insert_left(40)
r.insert_left(6)
print(f'левый узел {r.get_left_child().get_root_val()}')
r.insert_right(7)
r.insert_right(12)
print(f'правый узел {r.get_right_child().get_root_val()}')

