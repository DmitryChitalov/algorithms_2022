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


class AddTreeWrongSideException(Exception):
    pass


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # если совсем лениво
    def insert_child(self, new_node):
        if self.root < new_node:
            self.insert_right(new_node)
        else:
            self.insert_left(new_node)

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            # если нужно добавить с другой стороны
            if self.root < new_node:
                raise AddTreeWrongSideException
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
        except AddTreeWrongSideException:
            print(f'Добавление не в ту сторону, корень не должен быть меньше')

    # добавить правого потомка
    def insert_right(self, new_node):
        # если нужно добавить с другой стороны
        try:
            if self.root > new_node:
                raise AddTreeWrongSideException
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
        except AddTreeWrongSideException:
            print(f'Добавление не в ту сторону, корень не должен быть больше')

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
    r = BinaryTree(10)
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left(1)
    print(r.get_left_child())
    r.insert_right(30)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(15)
    print(r.get_right_child().get_root_val())
