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

"""
Предлагаемое решение декоратором, вроде как для расширения функционала, не меняя исходного решения, правда я завязался 
на имя функции, что на мой взгляд не очень хорошо, но зато получается один декоратор для всех функций.  
"""


def before_insert(func):
    def wrapper(node, newnode):
        if func.__name__ == 'insert_left' and node.root < newnode:
            raise ValueError(f'Значение должно быть меньше {node.root}')
        elif func.__name__ == 'insert_right' and node.root > newnode:
            raise ValueError(f'Значение должно быть больше {node.root}')
        else:
            pass

        return func(node, newnode)
    return wrapper


class BinaryTree:
    def __init__(self, root_obj, value=0):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        self.value = 0

    # добавить левого потомка
    @before_insert
    def insert_left(self, new_node):
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
        return self.left_child

    # добавить правого потомка
    @before_insert
    def insert_right(self, new_node):
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
        return self.right_child

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


if __name__ == '__main__':
    r = BinaryTree(8)
    # print(r.get_root_val())
    # print(r.get_left_child())
    r.insert_left(4)
    b1 = r.insert_left(2)
    b1.insert_right(3)
    r.insert_left(4)
    # print(r.get_left_child())
    # print(r.get_left_child().get_root_val())
    b2 = r.insert_right(12)
    b2.insert_left(4)
    # print(r.get_right_child())
    # print(r.get_right_child().get_root_val())
    # r.get_right_child().set_root_val(16)
    # print(r.get_right_child().get_root_val())
    print(r)