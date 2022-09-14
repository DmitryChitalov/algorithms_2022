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
source_in = input('Введите строку для кодирования: ')


def haffman_in(source):
    sl = deque(sorted(Counter(source).most_common(), key=lambda x: x[1]))
    while len(sl) > 1:
        k0 = sl[0][1]
        el_0 = sl.popleft()[0]
        k1 = sl[0][1]
        el_1 = sl.popleft()[0]
        k = k0 + k1
        sl1 = {0: el_0, 1: el_1}
        for i, w in enumerate(sl):
            if k > w[1]:
                continue
            else:
                sl.insert(i, (sl1, k))
                break
        else:
            sl.append((sl1, k))
    return sl[0][0]


our_code = {}


def haffman_out(matrix, el=''):
    if not isinstance(matrix, dict):
        our_code[matrix] = el
    else:
        haffman_out(matrix[0], el=f'{el}0')
        haffman_out(matrix[1], el=f'{el}1')


haffman_out(haffman_in(source_in))
for i in source_in:
    print(our_code[i], end=' ')
print()
