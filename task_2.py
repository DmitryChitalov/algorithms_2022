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

##############################################################################
"""
Доработки:
1) использовал слоты, чтобы уменьшить потребляемое количество памяти;
2) использовал декоратор @property, чтобы не писать пустые скобки использовании
методов получения элементов;
3) добавил генерацию исключения MyError при валидации значений узлов;
4) добавил генерацию исключения MyError при попытке получить несуществующего
потомка;
5) добавил генерацию исключения MyError при попытке установить значение узла,
которе меньше значения левого потомка или больше значения правого потомка.
"""

class MyError(Exception):

    def __init__(self, message):
        self.message = message


class BinaryTree():
    __slots__ = ['root', 'left_child', 'right_child', 'parent']

    def __init__(self, root_obj):
        self.root = root_obj  # корень
        self.left_child = None  # левый потомок
        self.right_child = None  # правый потомок

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if new_node > self.root:
                raise MyError(f'Значение потомка слева должно быть не больше {self.root}!')
            elif self.left_child == None:
                self.left_child = BinaryTree(new_node)
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except MyError as err:
            print(err)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                raise MyError(f'Значение потомка справа должно быть не меньше {self.root}!')
            elif self.right_child == None:
                self.right_child = BinaryTree(new_node)
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        except MyError as err:
            print(err)

    # метод доступа к правому потомку
    @property
    def get_right_child(self):
        try:
            if not self.right_child:
                raise MyError('Потомка справа не существует! Возвращается пустой узел!')
            return self.right_child
        except MyError as err:
            print(err)
            return BinaryTree(None)

    # метод доступа к левому потомку
    @property
    def get_left_child(self):
        try:
            if not self.left_child:
                raise MyError('Потомка слева не существует! Возвращается пустой узел!')
            return self.left_child
        except MyError as err:
            print(err)
            return BinaryTree(None)

    # метод установки корня
    def set_root_val(self, obj):
        try:
            if self.get_left_child.get_root_val and self.get_left_child.get_root_val > obj \
            or self.get_right_child.get_root_val and self.get_right_child.get_root_val < obj:
                raise MyError('Некорректное значение! Значение узла не изменилось!')
            self.root = obj
        except MyError as err:
            print(err)

    # метод доступа к корню
    @property
    def get_root_val(self):
        return self.root


# Тестирование
r = BinaryTree(8)
print('---> Значение корня:')
print(r.get_root_val)
print()

print('---> Попытка обратиться к несуществующему потомку слева:')
print(r.get_left_child)
print()

print('---> Попытка привязать потомка слева с некорретным значением:')
r.insert_left(10)
print()

r.insert_left(5)
print('---> Попытка обратиться к существующему потомку слева:')
print(r.get_left_child)
print()

print('---> Значение потомка слева:')
print(r.get_left_child.get_root_val)
print()

print('---> Попытка обратиться к несуществующему потомку справа:')
print(r.get_right_child)
print()

print('---> Попытка привязать потомка справа с некорретным значением:')
r.insert_right(5)
print()

r.insert_right(10)
print('---> Попытка обратиться к существующему потомку справа:')
print(r.get_right_child)
print()

print('---> Значение потомка справа:')
print(r.get_right_child.get_root_val)
print()

print('---> Попытка поменять значение потомка справа:')
r.get_right_child.set_root_val(16)
print(r.get_right_child.get_root_val)
print()

print('---> Попытка поменять значение корня:')
r.set_root_val(20)
print(r.get_root_val)