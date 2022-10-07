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


def haffman_coding(new_str):
    # Считаем уникальные символы.
    # Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
    count_elm = Counter(new_str)
    # Сортируем по возрастанию количества повторений.
    # deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
    # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
    sort_elm = deque(sorted(count_elm.items(), key=lambda item: item[1]))
    # Проверка, если строка состоит из одного повторяющего символа.
    if len(sort_elm) != 1:
        # Цикл для построения дерева
        while len(sort_elm) > 1:
            # далее цикл объединяет два крайних левых элемента
            # Вес объединенного элемента (накопленная частота)
            # веса - 2, 4, 4, 7, 8, 15
            weight = sort_elm[0][1] + sort_elm[1][1]
            # Словарь из 2 крайних левых элементов, попутно вырезаем их
            # из "sorted_elements" (из очереди).
            # comb - объединенный элемент
            '''
            {0: 'r', 1: '!'}
            {0: {0: 'r', 1: '!'}, 1: 'p'}
            {0: ' ', 1: 'o'}
            {0: 'b', 1: {0: ' ', 1: 'o'}}
            {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}
            {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
            '''
            comb = {0: sort_elm.popleft()[0],
                    1: sort_elm.popleft()[0]}

            # Ищем место для ставки объединенного элемента
            for i, amount in enumerate(sort_elm):
                if weight > amount[1]:
                    continue
                else:
                    # Вставляем объединенный элемент
                    # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
                    sort_elm.insert(i, (comb, weight))
                    break
            else:
                # Добавляем объединенный корневой элемент после
                # завершения работы цикла

                sort_elm.append((comb, weight))
            '''
            deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
            deque([(' ', 2), ('o', 2), ('b', 3), ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4)])
            deque([('b', 3), ({0: ' ', 1: 'o'}, 4), ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4)])
            deque([({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4), ({0: 'b', 1: {0: ' ', 1: 'o'}}, 7)])
            deque([({0: 'b', 1: {0: ' ', 1: 'o'}}, 7), ({0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}, 8)])
            deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
            '''
    else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        weight = sort_elm[0][1]
        comb = {0: sort_elm.popleft()[0], 1: None}
        sort_elm.append((comb, weight))
    # sorted_elements - deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
    # {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
    # словарь - дерево
    return sort_elm[0][0]


code_table = dict()

"""
tree - {
0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 
1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}
}
"""


def haffman_incode(tree, path=''):
    # Если элемент не словарь, значит мы достигли самого символа
    # и заносим его, а так же его код в словарь (кодовую таблицу).
    if not isinstance(tree, dict):
        code_table[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        haffman_incode(tree[0], path=f'{path}0')
        haffman_incode(tree[1], path=f'{path}1')


# строка для кодирования
my_str = "beep boop beer!"

# функция заполняет кодовую таблицу (символ-его код)
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
haffman_incode(haffman_coding(my_str))

# code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

# выводим коды для каждого символа
for i in my_str:
    print(code_table[i], end=' ')
print()
