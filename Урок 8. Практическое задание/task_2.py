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
from random import randint


# Валидацию объединил с автоматизацией вставки. В правую ветку - значения больше корневого, в левую - меньше.
# При попытке вставить уже существующие узлы дерева вызывается исключение (заменил на сообщение об ошибке).
# Класс еще можно развить функционально (удаление, замена узла, перестройка дерева до сбалансированного...), но такого
# задания вроде не было.
class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj  # корень
        self.left_child = None  # левый потомок
        self.right_child = None  # правый потомок

    def insert_node(self, value):  # вставляем узел, рекурсивно обходя дерево, пока не найдем нужное место
        def _add(node, val):
            if val < node.root:
                if node.left_child is not None:
                    _add(node.left_child, val)
                else:
                    node.left_child = BinaryTree(val)
            elif val > node.root:
                if node.right_child is not None:
                    _add(node.right_child, val)
                else:
                    node.right_child = BinaryTree(val)
            else:  # val == node.root
                # raise Exception(f"Узел '{val}' уже существует в дереве")
                print(f"Узел '{val}' уже существует в дереве")

        _add(self, value)

    def sorted_list(self):  # обходим дерево и возвращаем сортированный список значений
        def _sorted_list(node, lst):
            if node is not None:
                _sorted_list(node.left_child, lst)
                lst.append(node.root)
                _sorted_list(node.right_child, lst)

        if self.root is not None:
            _sorted_list(self, list_ := [])
            return list_

    def print_tree(self):  # печать дерева: корень крайний слева.
        def _print_tree(node, level=0):
            if node is not None:
                _print_tree(node.right_child, level + 1)
                print(f"{' ' * 4 * level}--| {node.root}")
                _print_tree(node.left_child, level + 1)

        if self.root is not None:
            print('---- Tree: -------------')
            _print_tree(self)
            print('------------------------')


# проверяем на тестовом массиве, печатаем дерево, получаем упорядоченный массив, обходя дерево
bt = BinaryTree(8)
[bt.insert_node(i) for i in [2, 5, 3, 6, 12, 9, 10, 15]]
bt.print_tree()
print(bt.sorted_list())

# Проверяем на случайных значениях.
# Сортируем уникальные значения входного массива и сравниваем со значениями, полученными обходом дерева
list_len = 100
test_len = 50
for i in range(test_len):
    li = [randint(-list_len, list_len) for _ in range(list_len)]
    li.append(0)  # добавляем 0, если не выпал случайно
    bt = BinaryTree(0)
    [bt.insert_node(i) for i in li]
    print(sorted(set(li)))
    print(bt.sorted_list())
    assert bt.sorted_list() == sorted(set(li))
print(f"{test_len} тестов на {list_len} значениях завершились успешно!")
