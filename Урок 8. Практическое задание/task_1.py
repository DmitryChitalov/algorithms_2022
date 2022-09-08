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

from collections import Counter


class HoffTree:

    def __init__(self, val, l_v=None, r_v=None):
        self.r_val = r_v
        self.l_val = l_v
        self.val = val


def fill_tree(new_str):
    str_cnt = Counter(new_str)

    if len(str_cnt) <= 1:
        unit = HoffTree(None)

        if len(str_cnt) == 1:
            unit.l_val = HoffTree([key for key in str_cnt][0])
            unit.r_val = HoffTree(None)

        str_cnt = {unit: 1}

    while len(str_cnt) != 1:
        unit = HoffTree(None)
        spam = str_cnt.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            unit.l_val = HoffTree(spam[0][0])

        else:
            unit.l_val = spam[0][0]

        if isinstance(spam[1][0], str):
            unit.r_val = HoffTree(spam[1][0])

        else:
            unit.r_val = spam[1][0]

        del str_cnt[spam[0][0]]
        del str_cnt[spam[1][0]]
        str_cnt[unit] = spam[0][1] + spam[1][1]

    return [key for key in str_cnt][0]


def tree_code(root, bin_code1=None, new_code=''):
    if bin_code1 is None:
        bin_code1 = dict()
    if root is None:
        return

    if isinstance(root.val, str):
        bin_code1[root.val] = new_code
        return bin_code1

    tree_code(root.l_val, bin_code1, new_code + '0')
    tree_code(root.r_val, bin_code1, new_code + '1')

    return bin_code1


def coding(str_to_code, bin_code2):
    fin_code = ''

    for dig in str_to_code:
        fin_code += bin_code2[dig]

    return fin_code


new_string_to_coding = input('Введите строку, которую нужно зашифровать: ')
tree = fill_tree(new_string_to_coding)
bin_code = tree_code(tree)
print(f'Коды символов: {bin_code}')

coding_str = coding(new_string_to_coding, bin_code)
print('Код строки: ', coding_str)
