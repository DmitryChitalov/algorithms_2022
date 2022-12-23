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

    def insert_left(self, new_node):
        try:
            if self.root <= new_node:
                raise BinaryTreeError
        except BinaryTreeError:
            print('Левый потомок не может быть больше или равен родителю.')
        else:
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

    def insert_right(self, new_node):
        try:
            if self.root >= new_node:
                raise BinaryTreeError
        except BinaryTreeError:
            print('Правый потомок не может быть меньше или равен родителю.')
        else:
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

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_root_val(self):
        return self.root

    def del_root_val(self):
        try:
            if self.left_child is not None or self.right_child is not None:
                raise BinaryTreeError
        except BinaryTreeError:
            print('Невозможно удалить узел, т.к. он является родителем.')
        else:
            self.root = None


if __name__ == '__main__':

    root = BinaryTree(15)
    print(root.get_root_val())

    root.insert_left(8)
    print(root.get_left_child().get_root_val())

    root.insert_left(7)

    root.insert_left(9)
    print(root.get_left_child().get_root_val())
    print(root.get_left_child().get_left_child().get_root_val())

    root.insert_right(6)

    root.insert_right(20)
    print(root.get_right_child().get_root_val())

    root.get_left_child().insert_right(11)
    print(root.get_left_child().get_right_child().get_root_val())

    root.get_left_child().insert_left(7)

    root.get_left_child().get_right_child().del_root_val()
    print(root.get_left_child().get_right_child().get_root_val())

    root.get_left_child().del_root_val()

# Убрал метод установки корня (set_root_val), потому что могла нарушиться структура двоичного дерева,
# а как сделать проверку нового установленного корня при данной реализации бинарного дерева, я не придумал.
# Но всё равно может возникнуть ситуация, когда в дерево вставляется элемент, который либо уже есть в нём,
# либо всё равно нарушает его структуру. Тогда нужно как-то хранить все узлы дерева и сравнивать с новым узлом,
# который будет вставлен.

# Смог реализовать удаление узла, только если он "лист". Как удалять узел, если у него есть один или два потомка
# при данной реализации бинарного дерева, тоже не придумал.
