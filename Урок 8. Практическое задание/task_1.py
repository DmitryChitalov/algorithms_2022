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
user = input('Введите строку для кодирования: ')


def haffman_my(source):
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


code = {}


def haffman_ex(matrix, el=''):
    if not isinstance(matrix, dict):
        code[matrix] = el
    else:
        haffman_ex(matrix[0], el=f'{el}0')
        haffman_ex(matrix[1], el=f'{el}1')


haffman_ex(haffman_my(user))
for i in user:
    print(code[i], end=' ')
print()