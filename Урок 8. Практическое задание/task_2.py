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
import operator


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
        if new_node >= self.root:
            raise "Incorrect value left"
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
            if self.left_child.root < new_node:
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
            else:
                self.left_child.insert_left(new_node)

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node <= self.root:
            raise "Incorrect value right"
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
            if self.right_child.root > new_node:
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
            else:
                self.right_child.insert_right(new_node)

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        flag = True
        if self.left_child is not None:
            if self.left_child.root >= obj:
                flag = False
        if self.right_child is not None:
            if self.right_child.root <= obj:
                flag = False
        if flag is False:
            raise 'Incorrect root value'
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


def try_test(tree, method, value):
    try:
        operator.attrgetter(method)(tree)(value)
        return True
    except TypeError:
        return False


# Тестирование дерева:
# Проверка добавление левой ветки
test_case = [22, 21, 6, 21, 10, 5, 4]
r = BinaryTree(10)
test_methods = ['insert_left', 'insert_right', 'set_root_val']
for method in test_methods:
    for value in test_case:
        print(f'{method} {value} result: {try_test(tree=r, method=method, value=value)}')
    test_case.reverse()

for value in test_case:
    print(
        f'get_right_child().set_root_val {value} result: {try_test(tree=r.get_right_child(), method="set_root_val", value=value)}')
for value in test_case:
    print(
        f'get_left_child().set_root_val {value} result: {try_test(tree=r.get_left_child(), method="set_root_val", value=value)}')
