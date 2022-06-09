"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
import copy
from collections import Counter, deque

"""
Хаффман через ООП
Кажеться, у меня получилась весьма жуткая, после пары дней упорного допиливания - абсолютно работающая структура))

"""


class BinaryTree:
    code_table = {}

    def __init__(self, root_obj):
        """
        При инициализаци экземпляра класса у нас есть два сценария:
        Когда экземпляр создаеться заново - ему передаеться кортеж из 2-х элементов, где первый элемент - символ из
        строки, второй - ее "вес" (частота, с какой этот символ встречаеться в строке)
        И второй вариант - когда пеердаеться экземпляр такого же класса (Звучит бредово и непонятно на данном этапе
        но ниже есть объяснение) тогда просто копируем параметры этого экземпляра во вновь созданные
        :param root_obj:
        """
        if isinstance(root_obj, tuple):
            # корень
            self.root = root_obj
            # значение корня
            self.root_element = root_obj[0]
            # вес элемента
            self.weight = root_obj[1]
            # левый потомок
            self.left_child = None
            # правый потомок
            self.right_child = None
            self.deque_el = None
        else:
            self.root = root_obj.root
            self.root_element = root_obj.root_element
            # вес элемента
            self.weight = root_obj.weight
            # левый потомок
            self.left_child = root_obj.left_child
            # правый потомок
            self.right_child = root_obj.right_child
            self.deque_el = root_obj.deque_el

    def haffman_deque(self, user_string):
        """
        Формируем дек из строки для кодировки, плюс получаем множество из элементов данной строки
        :param user_string: строка, которуую нужно закодировать
        :return: дек с элементами и из частотами повторения
        """
        # Строка пользователя
        self.user_string = user_string
        self.user_string_set = {el for el in self.user_string}
        # дэк из отсортированных элементов
        count = Counter(self.user_string)
        # Сортируем по возрастанию количества повторений.
        sorted_el = deque(sorted(count.items(), key=lambda item: item[1]))
        temp_deque = [BinaryTree(el) for el in sorted_el]
        self.deque_el = deque(temp_deque)

    """
    Методы insert_left и  insert_right оставляем из оригинального задания 2, хотя из них можно смело удалить половину 
    кода...
    """

    # добавить левого потомка
    def insert_left(self, new_node):
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

    @property
    def make_haff_tree(self):
        """
        Метод, который создает бинарное дерево из элементов дека сформированного методом haffman_deque
        Многочисленные "принты" писал для себя, что бы удостовериться в правильности работы метода, и решил не удалять
        в финальной версии.
        """
        if len(self.deque_el) != 0:
            while len(self.deque_el) > 1:
                # Берем 2 крайних элемента из начала дека и вычисляем вес
                temp_weight = self.deque_el[0].weight_root + self.deque_el[1].weight_root
                # Создаем новый узел с вычесленным весом
                new_node = ('', temp_weight)
                # Создаем новый элемент бинарного дерева и вычесленным весом
                temp_obj = BinaryTree(new_node)
                # В "лево" передаем 0-й элемент очереди, в "право" 1-й, удаляя эти элементы из дека
                temp_obj.insert_left(self.deque_el.popleft())
                temp_obj.insert_right(self.deque_el.popleft())
                # Ищем место для ставки объединенного элемента
                for i, el in enumerate(self.deque_el):
                    if temp_obj.weight_root > el.weight_root:
                        continue
                    else:
                        print("До вставки", [n.get_root_val() for n in self.deque_el])
                        print(f'Позиция {i}, заменяемый - {el}, вставляемый - {temp_obj},'
                              f' вставляемый левый {temp_obj.get_left_child()},'
                              f'вставляемый правый {temp_obj.get_right_child()}')
                        self.deque_el.insert(i, temp_obj)
                        print("После вставки", [n.get_root_val() for n in self.deque_el])
                        print(f'Длинна sorted_elements {len(self.deque_el)}')
                        print(self.deque_el)
                        break
                else:
                    print("До вставки", [n.get_root_val() for n in self.deque_el])
                    print(f'В конец списка вставляемый - {temp_obj.get_root_val()},'
                          f' вставляемый левый {temp_obj.get_left_child()},'
                          f'вставляемый правый {temp_obj.get_right_child()}')
                    self.deque_el.append(temp_obj)
                    print("После вставки", [n.get_root_val() for n in self.deque_el])
                    print(self.deque_el)
            if len(self.deque_el) == 1:
                self.haffman_binary_tree = self.deque_el[0]

    @property
    def haffman_tree_scaner(self):
        """
        Метод передающий поэлементно уникальные элементы кодируемой строки в метод haffman_deep_scan,
        и состовляющий словарь с кодировками
        """
        print(self.user_string_set)
        print(f"Binary tree {self.haffman_binary_tree}")
        for el in self.user_string_set:
            temp_string = ''
            find_el = self.haffman_deep_scan(self.haffman_binary_tree, el, temp_string)
            if find_el[0]:
                print(f'Элемент {el} найден!')
                self.code_table[el] = find_el[1]
            else:
                print(f'Элемент {el} не найден в бинарном дереве')

    def haffman_deep_scan(self, obj, el, code_string):
        """
        Метод - обходчик бинарного дерева. Метод рекурсивно обходит все бинарное дерево, начиная с корня, левого
        потомка, правого потомка.
        :param obj: Бинарное дерево
        :param el: Элемент, который нужно найти в корне или потомках бинарного дерева
        :param code_string: Строка содержащая кодировку искомого элемента
        :return: кортеж, в котором первый элемент - флаг False/True - итог найден ли был элемент по результату работы
        метода, и второй элемент - code_string - строка-кодировка искомого элемента
        """
        if obj == None:
            return False, code_string
        else:
            if obj.root_element == el:
                return True, code_string
            else:
                left_obj = self.haffman_deep_scan(obj.get_left_child(), el, code_string)
                if left_obj[0]:
                    return True, f'0{left_obj[1]}'
                else:
                    right_obj = self.haffman_deep_scan(obj.get_right_child(), el, code_string)
                    if right_obj[0]:
                        return True, f'1{right_obj[1]}'
                    else:
                        return False, code_string

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    # метод показа "веса" корня
    @property
    def weight_root(self):
        return self.weight

    # метод вывода элементов и их кодов
    @property
    def show_code_table(self):
        print(self.code_table)


# строка для кодирования
s = "beep boop beer!"
a = BinaryTree((1, 1))
print(a)
a.haffman_deque(s)
a.make_haff_tree
print(a.haffman_binary_tree)
print(a.get_root_val())
a.haffman_tree_scaner
a.show_code_table
