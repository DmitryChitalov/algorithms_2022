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


class BinaryTreeError(Exception):
    def __init__(self):
        pass


class BinaryTree:

    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert(self, new_node):
        try:
            if self.root > new_node:
                if self.left_child is None:
                    self.left_child = BinaryTree(new_node)
                else:
                    try:
                        if self.left_child.root >= new_node:
                            raise BinaryTreeError
                    except BinaryTreeError:
                        print('Вставляемый слева новый узел не может быть меньше или равен узлу, который опустится ниже.')
                    else:
                        tree_obj = BinaryTree(new_node)
                        tree_obj.left_child = self.left_child
                        self.left_child = tree_obj
            elif self.root < new_node:
                if self.right_child is None:
                    self.right_child = BinaryTree(new_node)
                else:
                    try:
                        if self.right_child.root <= new_node:
                            raise BinaryTreeError
                    except BinaryTreeError:
                        print('Вставляемый справа новый узел не может быть больше или равен узлу, который опустится ниже.')
                    else:
                        tree_obj = BinaryTree(new_node)
                        tree_obj.right_child = self.right_child
                        self.right_child = tree_obj
            else:
                raise BinaryTreeError
        except BinaryTreeError:
            print('Новый потомок не может быть равен родителю.')

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_root_val(self):
        return self.root


if __name__ == '__main__':

    root = BinaryTree(15)
    print(root.get_root_val())

    root.insert(12)
    print(root.get_left_child().get_root_val())

    root.get_left_child().insert(12)

    root.insert(11)

    root.insert(25)
    print(root.get_right_child().get_root_val())

    root.insert(27)

    root.get_right_child().insert(20)
    print(root.get_right_child().get_left_child().get_root_val())

# Убрал метод установки корня (set_root_val), потому что могла нарушиться структура двоичного дерева,
# и вообще не уверен, что проверка нового установленного корня при данной реализации бинарного дерева возможна.
# Но всё равно при данной реализации может возникнуть ситуация, когда в дерево вставляется элемент, который либо уже есть в нём,
# либо всё равно нарушает его структуру.

# Методы вставки узла справа и слева заменил на общий метод вставки,
# в котором уже определяется, куда вставлять элемент: справа или слева.
