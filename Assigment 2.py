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

class MyOwnError(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        if self.reason == 'more':
            return "Left child's value can not be more than root's"
        else:
            return "Right child's value can not be less than root's"


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        try:
            if new_node > self.root:
                raise MyOwnError('more')
            else:
                if self.left_child is None:
                    self.left_child = BinaryTree(new_node)
                else:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
        except MyOwnError:
            print(MyOwnError('more'))

    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                raise MyOwnError('less')
            else:
                if self.right_child is None:
                    self.right_child = BinaryTree(new_node)
                else:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
        except MyOwnError:
            print(MyOwnError('less'))

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


if __name__ == '__main__':
    try:
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
        r.insert_left(60)
        r.insert_right(1)