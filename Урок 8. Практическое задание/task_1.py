"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque


def build_tree(user_str):
    count_elem = Counter(user_str)
    sorted_elem = deque(sorted(count_elem.items(), key=lambda items: items[1]))
    while len(sorted_elem) > 1:
        weight = sorted_elem[0][1] + sorted_elem[1][1]
        node = {0: sorted_elem.popleft()[0], 1: sorted_elem.popleft()[0]}
        for j, item in enumerate(sorted_elem):
            if weight > item[1]:
                continue
            else:
                sorted_elem.insert(j, (node, weight))
                break
        else:
            sorted_elem.append((node, weight))
    return sorted_elem[0][0]


def build_code(tree, path=''):
    if type(tree) != dict:
        code_table[tree] = path
    else:
        build_code(tree[0], path=f'{path}0')
        build_code(tree[1], path=f'{path}1')


code_table = {}
user_string = input('Введите строку: ')
try:  # Проверка на пустую строку
    user_string == len(user_string) * user_string[0]
except IndexError:
    print('Вы ввели пустую строку.')
else:
    if user_string == len(user_string) * user_string[0]:
        print('Нельзя построить дерево из одного и того же элемента.')
    else:
        build_code(build_tree(user_string))
        print(f'Дерево: {build_tree(user_string)}')
        print(f'Таблица с кодами: {code_table}')
        print('Закодированная строка: ')
        for i in user_string:
            print(code_table[i], end=' ')
        print()
