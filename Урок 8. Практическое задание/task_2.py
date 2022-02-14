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

    def __init__(self, text):
        self.text = text



class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    # отобразить дерево в понятном виде
    def __str__(self):
        left = self.left_child.root if self.left_child is not None else None
        right = self.right_child.root if self.right_child is not None else None
        return f'Узел {self.root} - левый потомок - {left} правый потомок - {right}'

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if new_node > self.root:
                raise MyErr('Вставляемое значение не может быть больше корня!')
            if self.left_child == None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except MyErr as err:
            print(err)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                raise MyErr('Вставляемое значение не может быть меньше корня!')
            if self.right_child == None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
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


tree = BinaryTree(30)
tree.insert_right(23)
tree.insert_right(10)
tree.insert_left(54)
tree.insert_right(45)
tree.insert_left(12)
print(tree)
