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


class WrongValue(Exception):
    def __init__(self, text):
        self.text = text


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int):
        """ вставка """
        try:
            if not str(value).isdigit():
                raise WrongValue(f'Вы ввели "{value}", так не надо.'
                                 f'\nСледует использовать цифры.\n{"*" * 50}')
        except WrongValue as message:
            print(message)
        else:
            if value < self.value:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)

    def inorder_tree(self):
        """ вывести в сортированном виде """
        if self.left:
            self.left.inorder_tree()
        print(self.value)
        if self.right:
            self.right.inorder_tree()
        return f'{"-" * 30}'

    def get_right_child(self):
        """ правый потомок """
        return self.right

    def get_left_child(self):
        """ правый потомок """
        return self.left

    def set_root_val(self, obj):
        """ установка корня """
        self.value = obj

    def get_root_val(self):
        """ доступ к корню """
        return self.value


r = BinaryTree(8)
r.insert(40)
r.insert(12)
r.insert(5)
r.insert(2)
r.insert(16)
r.insert(1)
r.insert(51)
r.insert(11)
r.insert(3)
r.insert(39)
r.insert(6)
r.insert('А и Б')

print('Все элементы дерева в отсортированном виде')
print(r.inorder_tree())

print('Корни отдельных веток:')
print(f'root: {r.value}')  # root 8
print(f'left root: {r.left.get_root_val()}')  # 5
print(f'right root: {r.right.get_root_val()}')  # 40
print(f'left left root: {r.left.left.get_root_val()}')  # 2
print(f'left right root: {r.left.right.get_root_val()}')  # 6
print(f'right left root: {r.right.left.get_root_val()}')  # 12

"""
здесь https://bit.ly/3y1gL4Q удобства представлена схема 
текущего бинарного дерева с данными, использованными в задании 
"""
