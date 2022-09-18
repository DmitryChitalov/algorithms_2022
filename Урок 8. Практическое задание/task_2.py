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


class MyErr(Exception):
    pass


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def __str__(self):
        return str(self.root)

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            new_node = int(new_node)
        except ValueError:
            print('Вы ввели не число')
        else:
            try:
                # если у узла нет левого потомка
                if self.root >= new_node:
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
                else:
                    raise MyErr('Введенное число не для левой части дерева')
            except MyErr as err:
                print(err)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            new_node = int(new_node)
        except ValueError:
            print('Вы ввели не число')
        else:
            try:
                if self.root <= new_node:
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
                else:
                    raise MyErr('Введенное число не для правой части дерева')
            except MyErr as err:
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


if __name__ == '__main__':
    r = BinaryTree(8)
    print(r.get_root_val())
    print(r.get_left_child())
    print(r.get_right_child())
    r.insert_left(65)
    r.insert_left(7)
    r.insert_left('a')
    r.insert_left('b')
    print(r.get_left_child())
    r.insert_right(6)
    r.insert_right(65)
    print(r.get_right_child())
    print(r.get_left_child().get_root_val())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(17)
    print(r.get_right_child().get_root_val())
    print(r.get_left_child())
    print(r.get_right_child())
