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


def haffman_tree(my_str):
    # Считаем уникальные символы.
    # Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
    # Counter({'a': 5, 'b': 2, 'r': 2, ' ': 1, 'c': 1, 'd': 1})
    # Counter(my_str) Counter({'a': 9})
    # Counter()
    count = Counter(my_str)
    # Сортируем по возрастанию количества повторений.
    # deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
    # deque([(' ', 1), ('c', 1), ('d', 1), ('b', 2), ('r', 2), ('a', 5)])
    # deque([('a', 9)])
    # deque([])
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    # Проверка, если строка состоит из одного повторяющего символа.
    if len(sorted_elements) > 1:
        # Цикл для построения дерева
        while len(sorted_elements) > 1:
            # далее цикл объединяет два крайних левых элемента
            # Вес объединенного элемента (накопленная частота)
            # веса - 2, 4, 4, 7, 8, 15
            # веса - 2, 3, 4, 7, 12
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            # Словарь из 2 крайних левых элементов, попутно вырезаем их
            # из "sorted_elements" (из очереди).
            # comb - объединенный элемент

            # {0: 'r', 1: '!'}
            # {0: 'p', 1: ' '}
            # {0: 'o', 1: {0: 'r', 1: '!'}}
            # {0: 'b', 1: 'e'}
            # {0: {0: 'p', 1: ' '}, 1: {0: 'o', 1: {0: 'r', 1: '!'}}}
            # {0: {0: 'b', 1: 'e'}, 1: {0: {0: 'p', 1: ' '}, 1: {0: 'o', 1: {0: 'r', 1: '!'}}}}

            # {0: ' ', 1: 'c'}
            # {0: 'd', 1: 'b'}
            # {0: 'r', 1: {0: ' ', 1: 'c'}}
            # {0: {0: 'd', 1: 'b'}, 1: {0: 'r', 1: {0: ' ', 1: 'c'}}}
            # {0: 'a', 1: {0: {0: 'd', 1: 'b'}, 1: {0: 'r', 1: {0: ' ', 1: 'c'}}}}

            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}
            # Ищем место для ставки объединенного элемента
            for elem, _count in enumerate(sorted_elements):
                if weight >= _count[1]:  # Если добавить "=", код совпадет с полученным в task_1.py,
                    # вставка будет производиться в конец одинаковых элементов.
                    continue
                # Вставляем объединенный элемент
                # deque([('p', 2), (' ', 2), ('o', 2), ({0: 'r', 1: '!'}, 2), ('b', 3), ('e', 4)])
                sorted_elements.insert(elem, (comb, weight))
                break
            else:
                # Добавляем объединенный корневой элемент после
                # завершения работы цикла

                sorted_elements.append((comb, weight))

            # deque([('o', 2), ({0: 'r', 1: '!'}, 2), ('b', 3), ('e', 4), ({0: 'p', 1: ' '}, 4)])
            # deque([('b', 3), ('e', 4), ({0: 'p', 1: ' '}, 4), ({0: 'o', 1: {0: 'r', 1: '!'}}, 4)])
            # deque([({0: 'p', 1: ' '}, 4), ({0: 'o', 1: {0: 'r', 1: '!'}}, 4), ({0: 'b', 1: 'e'}, 7)])
            # deque([({0: 'b', 1: 'e'}, 7), ({0: {0: 'p', 1: ' '}, 1: {0: 'o', 1: {0: 'r', 1: '!'}}}, 8)])
            # deque([({0: {0: 'b', 1: 'e'}, 1: {0: {0: 'p', 1: ' '}, 1: {0: 'o', 1: {0: 'r', 1: '!'}}}}, 15)])
            # deque([({0: 'a', 1: {0: {0: 'd', 1: 'b'}, 1: {0: 'r', 1: {0: ' ', 1: 'c'}}}}, 12)])
            # sorted_elements deque([({0: 'a', 1: None}, 9)])
            # sorted_elements deque([])

    elif len(sorted_elements) == 1:
        # приравниваем значение 0 к одному повторяющемуся символу
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
        # deque([({0: 'a', 1: None}, 9)])
    # sorted_elements - deque([({0: {0: 'b', 1: 'e'}, 1: {0: {0: 'p', 1: ' '}, 1: {0: 'o', 1: {0: 'r', 1: '!'}}}}, 15)])
    # {0: {0: 'b', 1: 'e'}, 1: {0: {0: 'p', 1: ' '}, 1: {0: 'o', 1: {0: 'r', 1: '!'}}}}
    # словарь - дерево
    # sorted_elements - deque([({0: 'a', 1: {0: {0: 'd', 1: 'b'}, 1: {0: 'r', 1: {0: ' ', 1: 'c'}}}}, 12)])
    # {0: 'a', 1: {0: {0: 'd', 1: 'b'}, 1: {0: 'r', 1: {0: ' ', 1: 'c'}}}}
    # словарь - дерево
    # sorted_elements - deque([({0: 'a', 1: None}, 9)])
    # {0: 'a', 1: None}
    # словарь - дерево
    # deque([])

    if sorted_elements:  # Для повторяющейся пустой строки.
        return_el = sorted_elements[0][0]
    else:
        return_el = ascii('')
    return return_el


code_table = {}


# tree - {
# 0: {0: 'b', 1: 'e'},
# 1: {0: {0: 'p', 1: ' '}, 1: {0: 'o', 1: {0: 'r', 1: '!'}}}
# }

# tree - {
# 0: 'a',
# 1: {0: {0: 'd', 1: 'b'}, 1: {0: 'r', 1: {0: ' ', 1: 'c'}}}
# }


def haffman_code(tree, path=''):
    # Если элемент не словарь, значит мы достигли самого символа
    # и заносим его, а так же его код в словарь (кодовую таблицу).
    if not isinstance(tree, dict):
        code_table[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')
    # print(" code_table ", code_table)


# строка для кодирования
code_table = {}
s = "beep boop beer!"

# функция заполняет кодовую таблицу (символ-его код)
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
haffman_code(haffman_tree(s))

# code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

# выводим коды для каждого символа
for i in s:
    print(code_table[i], end=' ')
print()

code_table = {}
MY_STRIING = "abra cadabra"
haffman_code(haffman_tree(MY_STRIING))
# code_table - {'a': '0', 'd': '100', 'b': '101', 'r': '110', ' ': '1110', 'c': '1111'}

# выводим коды для каждого символа
for i in MY_STRIING:
    print(code_table[i], end=' ')
print()

code_table = {}
MY_STRIING = "aaaaaaaaa"
haffman_code(haffman_tree(MY_STRIING))
# code_table - {'a': '0'}

# выводим коды для каждого символа
for i in MY_STRIING:
    print(code_table[i], end=' ')
print()

code_table = {}
MY_STRIING = ""
haffman_code(haffman_tree(MY_STRIING))
# code_table - {None: ''}
MY_STRIING = ""
haffman_code(haffman_tree(MY_STRIING))
# code_table - {None: ''}
