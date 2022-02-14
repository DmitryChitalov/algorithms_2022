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

"""Хаффман через коллекции"""
from collections import Counter, deque


def haffman_tree(word):
    sorted_elements = deque(sorted(Counter(word).items(), key=lambda a: a[1]))
    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            new_el = {0: sorted_elements.popleft()[0], 1: sorted_elements.popleft()[0]}
            for i, cnt in enumerate(sorted_elements):
                if weight > cnt[1]:
                    continue
                else:
                    sorted_elements.insert(i, (new_el, weight))
                    break
            else:
                sorted_elements.append((new_el, weight))
    else:
        weight = sorted_elements[0][1]
        new_elem = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((new_elem, weight))
    return sorted_elements[0][0]


code = {}


def haffman_code(tree, path=''):
    if isinstance(tree, str):
        code[tree] = path
        return
    haffman_code(tree[0], path=f'{path}0')
    haffman_code(tree[1], path=f'{path}1')


def encoding():
    result = (code[i] for i in word)
    return ' '.join(result)


word = input('Введите фразу, которую хотиде закодировать: ')

haffman_code(haffman_tree(word))

print(f'Фраза - {word} в кодировке - {encoding()}')
