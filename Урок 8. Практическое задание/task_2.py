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


class BranchErr(Exception):
    def __init__(self, x, y, child):
        self.x = x
        self.y = y
        self.child = child

    def __str__(self):
        if self.x > self.y:
            return f'неверное значение для метода {self.child.__name__}: ' \
                   f'"{self.x}" введите число меньше корня {self.y}'
        elif self.x < self.y:
            return f'неверное значение для метода {self.child.__name__}: ' \
                   f'"{self.x}" введите число больше корня {self.y}'


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
        # если у узла нет левого потомка
        try:
            if self.left_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                if new_node > self.root:
                    raise BranchErr(new_node, self.root, self.insert_left)
                self.left_child = BinaryTree(new_node)
                # если у узла есть левый потомок
            else:
                if new_node > self.left_child.get_root_val():
                    raise BranchErr(new_node, self.left_child.root, self.insert_left)
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except BranchErr as er:
            print(er)


    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        try:
            if self.right_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                if new_node < self.root:
                    raise BranchErr(new_node, self.root, self.insert_right)
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
            else:
                # тогда вставляем новый узел
                if new_node < self.right_child.get_root_val():
                    raise BranchErr(new_node, self.right_child.root, self.insert_right)
                tree_obj = BinaryTree(new_node)
                self.right_child = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        except BranchErr as er:
            print(er)


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


r = BinaryTree(8)
print('right')
print(r.get_root_val())
print(r.get_right_child())
r.insert_right(12)
#print(r.get_right_child())
#print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print(r.get_right_child())
print(r.get_right_child().get_right_child())
r.insert_right(15)
print(r.get_right_child().get_root_val())
print(r.get_right_child())
print(r.get_right_child().get_right_child())
r.insert_right(18)
print(r.get_right_child().get_root_val())
print(r.get_right_child())
print(r.get_right_child().get_right_child())
r.insert_right(19)
print(r.get_right_child().get_root_val())
print(r.get_right_child())
print(r.get_right_child().get_right_child())

print('left')
print(r.get_left_child())
r.insert_left(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_left(8)
print(r.get_left_child().get_root_val())
print(r.get_left_child())
print(r.get_left_child().get_left_child())
r.insert_left(5)
print(r.get_left_child().get_root_val())
print(r.get_left_child())
print(r.get_left_child().get_left_child())
r.insert_left(4)
print(r.get_left_child().get_root_val())
print(r.get_left_child())
print(r.get_left_child().get_left_child())
#print(r.get_right_child().get_right_child())
#root2 = r.get_right_child().get_root_val()
#r2 = BinaryTree(root2)
#r2.insert_left(18)
#print(r2.get_left_child().get_root_val())