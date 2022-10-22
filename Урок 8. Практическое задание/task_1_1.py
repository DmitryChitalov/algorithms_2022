class HaffmanElement():
    def __init__(self, simbol : str, count : int):
        self.simbol = simbol
        self.count = count
        self.bit = ''

        self.parent = None
        # левый потомок
        self.left_child : HaffmanElement = None
        # правый потомок
        self.right_child : HaffmanElement = None

    def __str__(self):
        return str(f'({self.simbol}, {self.count}, bit={self.bit})')

    def get_value(self):
        return self.simbol, self.count

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # добавить левого потомка
    def insert_left(self, child):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = child
            self.left_child.parent = self
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = child
            tree_obj.parent = self
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, child):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = child
            self.right_child.parent = self
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = child
            tree_obj.parent = self
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj