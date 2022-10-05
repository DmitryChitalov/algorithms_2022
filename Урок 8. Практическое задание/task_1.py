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

from collections import Counter, deque, namedtuple


class MyTree(namedtuple('Tree', 'right left')):
    pass


def haffman_tree(my_str):
    count_symbol = Counter(my_str)

    sorted_dict = deque(sorted(count_symbol.items(), key=lambda symbol: symbol[1]))

    while len(sorted_dict) > 1:

        weight = sorted_dict[0][1] + sorted_dict[1][1]
        node = MyTree(left=sorted_dict.popleft()[0], right=sorted_dict.popleft()[0])

        for i, item in enumerate(sorted_dict):
            if weight > item[1]:
                continue
            else:
                sorted_dict.insert(i, (node, weight))
                break
        else:
            sorted_dict.append((node, weight))

    return sorted_dict[0][0]



code_dict = {}


def haffman_code(tree, path=''):
    if not isinstance(tree, MyTree):
        code_dict[tree] = path

    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


# строка для кодирования
s = "beep boop beer!"

# функция заполняет кодовую таблицу (символ-его код)
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
haffman_code(haffman_tree(s))

# code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

# выводим коды для каждого символа
for i in s:
    print(code_dict[i], end=' ')
print()


