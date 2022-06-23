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
"""
Доработки:
1) Генерация собственного исключения OwnError при добавлении потомка с "неверной логикой".
2) Генерация собственного исключения OwnError при получении несуществующего потомка.
3) Генерация собственного исключения OwnError при изменении корня на некорректное значение.
4) @property для определения методов в классе , которые действуют как атрибуты.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj  # корень
        self.left_child = None  # левый потомок
        self.right_child = None  # правый потомок

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if new_node >= self.root:
                raise OwnError(f'Ошибка! Левый потомок = {new_node} больше корня = {self.root}!')
        except OwnError as err:
            print(err)
        else:
            # если у узла нет левого потомка
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

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node <= self.root:
                raise OwnError(f'Ошибка! Правый потомок = {new_node} меньше корня = {self.root}!')
        except OwnError as err:
            print(err)
        else:
            # если у узла нет правого потомка
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

    # метод доступа к правому потомку
    @property
    def get_right_child(self):
        try:
            if self.right_child is None:
                raise OwnError('Потомка справа не существует!')
            return self.right_child
        except OwnError as err:
            print(err)
            return BinaryTree(None)

    # метод доступа к левому потомку
    @property
    def get_left_child(self):
        try:
            if self.left_child is None:
                raise OwnError('Потомка слева не существует!')
            return self.left_child
        except OwnError as err:
            print(err)
            return BinaryTree(None)



    # метод установки корня
    def set_root_val(self, obj):
        try:
            if self.get_left_child.get_root_val and self.get_left_child.get_root_val > obj \
            or self.get_right_child.get_root_val and self.get_right_child.get_root_val < obj:
                raise OwnError('Некорректное значение! Значение узла не изменилось!')
            self.root = obj
        except OwnError as err:
            print(err)

    # метод доступа к корню
    @property
    def get_root_val(self):
        return self.root



r = BinaryTree(8)
print(f'Значение корня: {r.get_root_val}')
print('---')

print(f'Несуществующий потомок слева = {r.get_left_child.get_root_val}')
print('---')

print('Неверное значение потомка слева :')
r.insert_left(12)
print('---')

print('Вставка потомка слева:')
r.insert_left(7)
print(f'Значение потомка слева: {r.get_left_child.get_root_val}')
print(f'Значение корня: {r.get_root_val}')
print('---')

print('Неверное значение потомка справа :')
r.insert_right(5)
print('---')

print('Вставка потомка справа:')
r.insert_right(10)
print(f'Значение потомка справа: {r.get_right_child.get_root_val}')
print(f'Значение корня: {r.get_root_val}')
print('---')

print('---> Попытка поменять значение корня:')
r.set_root_val(20)
print(r.get_root_val)