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

    # добавить левого потомка
    def insert_left(self, new_node):
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

    # добавить правого потомка
    def insert_right(self, new_node):
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
        try:
            return self.root
        except Exception:
            return None

# Доработаем метод вставки согласно требованию:
#   - любое значение меньше значения узла становится левым ребенком или ребенком левого ребенка.
#   - любое значение больше или равное значению узла становится правым ребенком или ребенком правого ребенка.
    def insert_bin(self, new_node):
        if new_node < self.root:
            self.insert_left(new_node)
        else:
            self.insert_right(new_node)
            
# получить значение левого ребёнка            
    def get_left_val(self):
        try:
            return self.left_child.get_root_val()
        except Exception:
            return None
        
# получить значение правого ребёнка            
    def get_right_val(self):
        try:
            return self.right_child.get_root_val()
        except Exception:
            return None

r = BinaryTree(8)
r.insert_bin(7) # вставит влево
print('left_val', r.get_left_child().get_root_val())
print('right', r.get_right_child())
print('right_val', r.get_right_val())
r.insert_bin(7) # вставит влево
print('right', r.get_right_child())
print('right_val', r.get_right_val())
r.insert_bin(8) # вставит вправо
print('right', r.get_right_child())
print('right_val', r.get_right_val())
