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


from collections import Counter, deque

code_table = dict()


def to_sort_list(s: str):
    elements = list(Counter(s).items())
    sorted_elements = sorted(elements, key=lambda element: element[1], reverse=True)
    return sorted_elements


class Trees:

    def __init__(self, sorted_list: list):
        self.sorted_list = sorted_list
        self.tree_rep = tuple()

    def haffman_tree(self):
        el_2 = self.sorted_list.pop()
        el_1 = self.sorted_list.pop()
        w = el_1[1] + el_2[1]
        obj = (('1', el_1[0]), ('0', el_2[0]))
        new_el = (obj, w)
        length = len(self.sorted_list)
        help_list = self.sorted_list
        if length == 0 or self.sorted_list[length - 1][1] >= w:
            self.sorted_list.append(new_el)
        elif self.sorted_list[0][1] <= w:
            self.sorted_list.insert(0, new_el)
        else:
            for i in range(length):
                if self.sorted_list[i][1] >= w:
                    self.sorted_list.insert(i + 1, new_el)
                    break
        return Trees(self.sorted_list)

    def structure(self):
        for _ in range(len(self.sorted_list) - 1):
            self.tree_rep = self.haffman_tree().sorted_list
        return self.tree_rep[0][0]


def create_table(tree_obj: tuple, path=''):
    if not isinstance(tree_obj[0], str):
        create_table(tree_obj[0], path=path)
        create_table(tree_obj[1], path=path)
    elif not isinstance(tree_obj[1], tuple):
        path = path + tree_obj[0]
        code_table[tree_obj[1]] = path
    else:
        path = path + tree_obj[0]
        create_table(tree_obj[1], path)


# Сделал реализацию через ООП и кортежи
output_str = str()
my_str = 'beep boop beer!'
print(f'\nИсходная строка: {my_str}')
my_list = to_sort_list(my_str)
my_tree = Trees(my_list)
my_structure = my_tree.structure()
print(f'Дерево Хаффмана: {my_structure}')
create_table(my_structure)
print(f'Словарь: {code_table}')
for char in my_str:
    output_str = f'{output_str}{code_table[char]}'
print(f'Закодированная строка: {output_str}\n')
my_str_1 = 'Cat climbs into Christmas tree to play with ornaments'
print(f'Исходная строка: {my_str_1}')
my_list = to_sort_list(my_str_1)
my_tree = Trees(my_list)
my_structure = my_tree.structure()
print(f'Дерево Хаффмана: {my_structure}')
create_table(my_structure)
print(f'Словарь: {code_table}')
output_str = str()
for char in my_str_1:
    output_str = f'{output_str}{code_table[char]}'
print(f'Закодированная строка: {output_str}\n')
my_str_2 = 'Пробки в Казани снова достигли 9 баллов'
print(f'Исходная строка: {my_str_2}')
my_list = to_sort_list(my_str_2)
my_tree = Trees(my_list)
my_structure = my_tree.structure()
print(f'Дерево Хаффмана: {my_structure}')
create_table(my_structure)
print(f'Словарь: {code_table}')
output_str = str()
for char in my_str_2:
    output_str = f'{output_str}{code_table[char]}'
print(f'Закодированная строка: {output_str}')
