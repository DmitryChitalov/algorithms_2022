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
import re
import ast
import json


def dict_tree(my_tree):
    while len(my_tree) > 1:
        my_tree = dict(sorted(dict(my_tree).items(), key=lambda x: -x[1]))
        m_0 = my_tree.popitem()
        m_1 = my_tree.popitem()
        my_tree[f"{{0: {m_0[0]}, 1: {m_1[0]}}}"] = m_0[1] + m_1[1]
    my_tree = my_tree.popitem()[0]
    my_tree = re.sub(':(\s+[^,{}]*),|:\s\w+}|:\s+}', get_repl, my_tree)
    my_tree = json.loads(json.dumps(ast.literal_eval(my_tree)))
    return my_tree


def get_repl(obj):
    my_str = obj.group(0)
    fn = obj.group(0).replace(':', '').replace(' ', '').replace(',', '').replace('}', '')
    if fn == '':
        return f"{my_str[0]} ' '{my_str[3]}"
    else:
        return f"{my_str[0]} '{fn}'{my_str[3]}"


def make_tree(s, k_tmp=()):
    while len(s) > 0:
        kn = k_tmp
        n = dict.popitem(s)
        if len(kn) == 0:
            kn = n[0]
        else:
            kn += n[0]
        if type(n[1]) is dict:
            make_tree(n[1], kn)
        if len(n[1]) > 0:
            key_code[n[1]] = kn
    return


def make_code_list(key_tmp, my_str):
    str_code = ''
    for i in my_str:
        str_code += key_tmp[i]
    return str_code


my_str = 'beep boop beer!'
print(f'Исходный текст: {my_str}')

my_dict = dict(sorted(dict(Counter(list(my_str))).items(), key=lambda x: -x[1]))
print(f'Частота символов: {my_dict}')

my_dict = dict_tree(my_dict)
print(f'Дерево в виде словаря: {my_dict}')

key_code = {}
make_tree(my_dict)
print(f'Кодировка символов: {key_code}')

str_code = make_code_list(key_code, my_str)
print(f'Закодированная строка: {str_code}')


