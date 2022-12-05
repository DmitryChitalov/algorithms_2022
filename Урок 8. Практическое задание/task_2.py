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
    # Добавим exeption
    def insert_left(self, new_node):
        try:
            # если у узла нет левого потомка
            if self.root >= new_node:
                if self.left_child is None:
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
            else:
                raise Exception('Некорректое действие!\nИспользуйте другого потомка.')
        except Exception as e:
            print(e)

    # добавить правого потомка
    # Добавим exeption (аналогично левому потомку)
    def insert_right(self, new_node):
        try:
            # если у узла нет правого потомка
            if self.root <= new_node:
                if self.right_child is None:
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
            else:
                raise Exception('Некорректое действие!\nИспользуйте другого потомка.')
        except Exception as e:
            print(e)

    # метод доступа к правому потомку
    # Появлялась ошибка AttributeError 'NoneType' object has no attribute 'get_root_val')
    # try-except поймать не получится, поскольку возвращаемое значение None считается адекватным
    # Чтобы не выдавало ошибки (адекватно работал метод get_root_val()), будем возвращать бинарное дерево от None
    def get_right_child(self):
        if self.right_child is not None:
            return self.right_child
        else:
            return BinaryTree(None)

    # метод доступа к левому потомку
    # Аналогично для левого потомка
    def get_left_child(self):
        if self.left_child is not None:
            return self.left_child
        else:
            return BinaryTree(None)

    # метод установки корня
    # Доработаем, чтобы нельзя было изменить дерево неправильно
    def set_root_val(self, obj):
        # Если равен, то по сути оставляем неизменным
        if obj == self.root:
            self.root = obj
        else:
            # Если меньше, то добавляем в качестве левого потомка
            if obj < self.root:
                # Если потомка нет, то создаем его
                if self.left_child is None:
                    self.left_child = BinaryTree(obj)
                else:
                    # Если есть, то меняем рекурсией
                    self.left_child.set_root_val(obj)
            # Если больше, то добавляем в качестве правого потомка
            elif obj > self.root:
                # Если потомка нет, то создаем его
                if self.right_child is None:
                    self.right_child = BinaryTree(obj)
                else:
                    # Если есть, то меняем рекурсией
                    self.right_child.set_root_val(obj)

    # метод доступа к корню
    # Если потомка нет (приходит BinaryTree(None)), будем об этом сообщать
    def get_root_val(self):
        if self.root is not None:
            return f'Значение - {self.root}'
        else:
            return 'Ошибка доступа к значению, потомка нет!'

    # При попытке вывода несуществующего объекта также будем об этом сообщать
    def __str__(self):
        if self.root is None:
            return 'Потомка нет!'
        return f'{type(self)}, значение - {self.root}'


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
print()

r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
print()

r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
print()

r.right_child.insert_right(13)
print(r.right_child.get_right_child())
print(r.right_child.get_right_child().get_root_val())
print()

r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print()


print(r.get_root_val())
print(r.right_child.get_root_val())
print(r.right_child.right_child.get_root_val())
print()
"""
Изначально выводилось:
Значение - 8
Значение - 16
Значение - 13

Это неверно, поскольку не соблюдается порядок для значений потомков.
Это можно решить доработав метод set_root_val()
"""
"""
После доработки set_root_val():
Значение - 8
Значение - 16
Значение - 13

Значение же 16, которое мы пытались добавить, теперь является еще одним потомком
"""

print(r.get_root_val())
print(r.right_child.get_root_val())
print(r.right_child.right_child.get_root_val())
print(r.right_child.right_child.right_child.get_root_val())

"""
Получим:
Значение - 8
Значение - 12
Значение - 13
Значение - 16

В итоге смысл методов следующий:
1) Методы Insert_right и insert_left существуют для пользователей, которые понимают бинарные деревья. 
    Если они совершают ошибку, выводится сообщение о ней.
2) Метод set_root_val для условно "автоматического" добавления значения. 
    Если семантически значение не подходит для места, куда его хочет установить пользователь,
    создаются поддеревья, дерево смещается и значение устанавливается в подходящее место.
"""