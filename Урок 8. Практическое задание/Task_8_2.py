"""
Задание 2.**
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)
Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def __str__(self):  # добавлено строкове представление
        left = self.left_child.root if self.left_child is not None else None
        right = self.right_child.root if self.right_child is not None else None
        return f'<Узел {self.root}, дети: {left}, {right}>'

    def insert_left(self, new_node):  # добавлена валидация нового узла по отношению к родительскому

        if not self.validate(new_node):
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:  # добавлено автоматическое смещение прежнего узла в сторону правого или левого потомка нового узла
                tree_obj = BinaryTree(new_node)
                if tree_obj.validate(self.left_child.root):
                    tree_obj.right_child = self.left_child
                    self.left_child = tree_obj
                else:
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
        else:
            raise ValueError('Значение узла больше или равно корню!')

    def insert_right(self, new_node):

        if self.validate(new_node):  # добавлена валидация нового узла по отношению к родительскому
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:  # добавлено автоматическое смещение прежнего узла в сторону правого или левого потомка нового узла
                tree_obj = BinaryTree(new_node)
                if tree_obj.validate(self.right_child.root):
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
                else:
                    tree_obj.left_child = self.right_child
                    self.right_child = tree_obj
        else:
            raise ValueError('Значение нового узла меньше корня!')

    def validate(self, value):
        if value >= self.root:
            return True
        else:
            return False

    def set_root_val(self, obj):
        self.root = obj


if __name__ == '__main__':
    tree = BinaryTree(20)
    tree.insert_left(19)
    tree.insert_right(30)
    print(tree.left_child)
    print(tree.right_child)
    tree.insert_left(15)
    tree.insert_right(30)
    print(tree.left_child)
    print(tree.right_child)
    print(tree.left_child.right_child)
    print(tree.right_child.right_child)

"""
    tree = BinaryTree(20)
    tree.insert_left(19)
    tree.insert_right(30)
    print(tree.left_child)
    print(tree.right_child)
    tree.insert_left(15)
    tree.insert_right(30)
    print(tree.left_child)
    print(tree.right_child)
    print(tree.left_child.right_child)
    print(tree.right_child.right_child)
"""

"""
  Traceback (most recent call last):
  
    tree.insert_right(19)
  
    raise ValueError('Значение нового узла меньше корня!')
ValueError: Значение нового узла меньше корня!

"""


