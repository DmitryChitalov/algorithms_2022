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

from accessify import protected


class BinaryTree:
    def __init__(self, root_obj, path='root'):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        # путь
        self.path = path

    # добавить потомка
    def insert_child(self, root_obj, path='root'):
        # разделяем от корня на левую или правую ветки
        if root_obj >= self.root:
            self.insert_right(root_obj, path)
        else:
            self.insert_left(root_obj, path)

    # добавить левого потомка
    @protected
    def insert_left(self, new_node, path):
        # если у узла нет левого потомка
        path = f'{path}-l'
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node, path=path)
        # если у узла есть левый потомок
        else:
            old_node = self.get_left_child()
            # большие или равные идут направо
            if new_node >= old_node.root:
                old_node.insert_right(new_node, path)
            else:  # остальные налево
                old_node.insert_left(new_node, path)

    # добавить правого потомка
    @protected
    def insert_right(self, new_node, path):
        path = f'{path}-r'
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node, path=path)
        # если у узла есть правый потомок
        else:
            old_node = self.get_right_child()
            # большие или равные идут направо
            if new_node >= old_node.root:
                old_node.insert_right(new_node, path)
            else:  # остальные налево
                old_node.insert_left(new_node, path)

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

    def __str__(self):
        return f'{self.path}: {self.root}'

    # поиск элемента по значению
    def find_el(self, node):
        try:
            if node == self.root:
                print(self)
            elif node >= self.root:
                new_self = self.get_right_child()
                new_self.find_el(node)
            else:
                new_self = self.get_left_child()
                new_self.find_el(node)
        except AttributeError:
            print(f'Значение {node} отсутствует')


r = BinaryTree(10)
print(r.get_root_val())
print(r.get_left_child())
r.insert_child(40)
print(f'{r.get_right_child()}')
r.insert_child(3)
print(f'{r.get_left_child()}')
r.insert_child(5)
print(f'{r.get_left_child().get_right_child()}')
r.insert_child(15)
print(f'{r.get_right_child().get_left_child()}')
r.insert_child(45)
print(f'{r.get_right_child().get_right_child()}')
r.insert_child(12)
r.insert_child(30)
print(f'{r.get_right_child().get_left_child().get_right_child()}')
print(f'{r.get_right_child().get_left_child().get_left_child()}')
r.insert_child(41)
print(f'{r.get_right_child().get_right_child().get_left_child()}')
r.insert_child(31)
print(f'{r.get_right_child().get_left_child().get_right_child().get_right_child()}')
r.find_el(12)
r.find_el(7)

# Вывод:
#  Методы insert_right и insert_left - оптимизация. Пользователю предоставляем
#  для добавления узлов метод insert_child, который принимает на вход значение узла,
#  определяет основную ветвь и далее вызывает методы insert_right и insert_left, которые рекурсивно
#  вызывают друг друга в процессе определения места в дереве в зависимости от значения
#  нового узла и уже ранее добавленных узлов дерева.
#  Для проверки корректности построения дерева добавила атрибут path, куда пишется путь
#  размещения узла.
