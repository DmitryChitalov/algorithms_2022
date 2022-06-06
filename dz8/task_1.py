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


def hafman_func(st):
    count = Counter(st)
    dec = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(dec) != 1:
        while len(dec) > 1:
            sum_w = dec[0][1] + dec[1][1]
            res = {0: dec.popleft()[0],
                   1: dec.popleft()[0]}
            for i, el_c in enumerate(dec):
                if sum_w > el_c[1]:
                    continue
                else:
                    dec.insert(i, (res, sum_w))
                    break
            else:
                dec.append((res, sum_w))
    else:
        sum_w = dec[0][1]
        res = {0: dec.popleft()[0], 1: None}
        dec.append((res, sum_w))
    return dec[0][0]


result_tbl = dict()


def hafman_cod(tree, res=''):
    if not isinstance(tree, dict):
        result_tbl[tree] = res
    else:
        hafman_cod(tree[0], res=f'{res}0')
        hafman_cod(tree[1], res=f'{res}1')


def string_cod(user_str):
    res = ''
    for j in user_str:
        res += result_tbl[j]
    return res


def decoding(cod_str):
    res = ''
    i = 0
    while i < len(cod_str):
        for cod in result_tbl:
            if cod_str[i:].find(result_tbl[cod]) == 0:
                res += cod
                i += len(result_tbl[cod])
    return res


s = 'beep boop beer!'
(hafman_cod(hafman_func(s)))

print(f"Дерево: {hafman_func(s)}")
print(f"Таблица с кодировкой символа: {result_tbl}")
print(f"Закодированноя строка: {string_cod(s)}")
print(f"Декодированноя строка: {decoding(string_cod(s))}")
