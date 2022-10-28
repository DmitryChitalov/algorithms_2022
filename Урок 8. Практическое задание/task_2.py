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


class ValidInsert(Exception):
    def __init__(self, text):
        self.text = text


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
            if self.root > new_node:
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
            # добавляем исключения
            elif self.root < new_node:
                raise ValidInsert(f'Добавляемый узел {new_node} '
                                f'больше корня {self.root} дерева!')
            else:
                raise ValidInsert(f'Добавляемый узел {new_node} '
                                f'равен корню {self.root} дерева!')
        except Exception as exp:
            print(exp)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root < new_node:
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
            # добавляем исключения
            elif self.root > new_node:
                raise ValidInsert(f'Добавляемый узел {new_node} '
                                f'меньше корня {self.root} дерева!')
            else:
                raise ValidInsert(f'Добавляемый узел {new_node} '
                                f'равен корню {self.root} дерева!')
        except Exception as exp:
            print(exp)

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

    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left(6)
    r.insert_left(30)
    r.insert_left(8)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val(), '\n')

    r.insert_right(30)
    r.insert_right(6)
    r.insert_right(8)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val(), '\n')

"""
8
None
Добавляемый узел 30 больше корня 8 дерева!
Добавляемый узел 8 равен корню 8 дерева!
<__main__.BinaryTree object at 0x0000019CD5A53D00>
6 

Добавляемый узел 6 меньше корня 8 дерева!
Добавляемый узел 8 равен корню 8 дерева!
<__main__.BinaryTree object at 0x0000019CD5A53C70>
30 
"""
