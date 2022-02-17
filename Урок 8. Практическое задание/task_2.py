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


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить потомка автоматически
    def insert(self, data):
        if data < self.root:
            if self.left_child is None:
                self.left_child = BinaryTree(data)
            else:
                self.left_child.insert(data)
        elif data > self.root:
            if self.right_child is None:
                self.right_child = BinaryTree(data)
            else:
                self.right_child.insert(data)
        
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

    # Вывод дерева
    def p_print(self, level=0):
        print('  ' * (level + 1) + '|' + '_' + repr(self.get_root_val()))
        for child in (self.left_child, self.right_child):
            if child is not None:
                child.p_print(level+1)


r = BinaryTree(8)
r.insert(10)
r.insert(6)
r.get_right_child().insert(5)
r.get_right_child().insert(11)
r.p_print()

"""
Добавлен метод автоматической вставки, выбор вставить влево или право определяется по значению.

Добавлен простой метод вывода древа.

"""