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

    def get_right_child(self, move=False):
        if isinstance(self.right_child, BinaryTree):
            if move:
                return self.right_child
            else:
                return self.right_child.get_root()
        else:
            return self.right_child

    def get_left_child(self, move=False):
        if isinstance(self.left_child, BinaryTree):
            if move:
                return self.left_child
            else:
                return self.left_child.get_root()
        else:
            return self.left_child

    def get_root(self):
        return self.root


def check_insert(func):
    def wrap(cls, new):
        try:
            # print(cls,new)
            if not isinstance(cls, BinaryTree):
                raise NameError(f'неверно передан {cls} он должен быть BinaryTree')
            elif not isinstance(new, int):
                raise MyError(f'неверно передан {new} он должен быть тип int')
            else:
                func(cls, new)
        except (MyError, NameError) as e:
            print(e)
    return wrap

@check_insert
def insert(Bt_class, new_node):
    # print(f'bt class {type(Bt_class)} root {Bt_class.root}')
    if Bt_class.root > new_node:
        print(f'{new_node} в лево от {Bt_class.root}')
        if Bt_class.left_child == None:
            Bt_class.left_child = new_node
        else:
            
            new_tree = BinaryTree(Bt_class.left_child)
            print(f'создание нового узла с корнем {Bt_class.left_child}')
            insert(new_tree, new_node)
            Bt_class.left_child = new_tree

    elif Bt_class.root < new_node:
        print(f'{new_node} в право от {Bt_class.root}')
        if Bt_class.right_child == None:
            Bt_class.right_child = new_node
        else:
            
            new_tree = BinaryTree(Bt_class.right_child)
            print(f'создание нового узла с корнем {Bt_class.right_child}')
            insert(new_tree, new_node)
            Bt_class.right_child = new_tree
    else:
        print(f'новое значение равно root {new_node}')

def find(cls, num):
    if num == cls.get_right_child():
        return f'найдено {num} в правой ветке {cls.get_root()}'
    elif num == cls.get_left_child():
        return f'найдено {num} в левой ветке {cls.get_root()}'
    elif num < cls.root:
        if cls.get_left_child():
            return find(cls.get_left_child(True), num)
        else:
            return 'нет такого значения'
    elif num > cls.root:
        if cls.get_right_child():
            return find(cls.get_right_child(True), num)
        else:
            return 'нет такого значения'

class MyError(Exception):
    def __init__(self, message="ошибка моего типа"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
        
Bt = BinaryTree(8)

insert(Bt, 20)
insert(Bt, 'df')
insert(Bt, 10)
insert(Bt, 4)
print(Bt.get_left_child())
insert(Bt, 2)
print(Bt.get_right_child())
print(find(Bt, 5))

'''Кроме __init__ переписаны функции и классы
добавлены: 
    ошибка типа MyError 
    поиск по дереву
    print по ходу помещения новых значений в дерево для показа перемещений
    проверка с помощью декоратора значений принимаемых деревом
    
изменены:
    get_right_child
    get_left_child

пример выполнения:
    20 в право от 8
    неверно передан df он должен быть тип int
    10 в право от 8
    создание нового узла с корнем 20
    10 в лево от 20
    4 в лево от 8
    4
    2 в лево от 8
    создание нового узла с корнем 4
    2 в лево от 4
    20
    нет такого значения

'''