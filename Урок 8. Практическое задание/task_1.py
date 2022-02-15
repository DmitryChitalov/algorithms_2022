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

s = "beep boop beer!"
final_code = dict()


class BinaryTree:
    def __init__(self, left, right):
        # левый потомок
        self.left = left
        # правый потомок
        self.right = right


def haffman(s):
    count_str = Counter(s)          # частотный анализ
    sorted_str = deque(sorted(count_str.items(), key=lambda item: item[1]))     # сортируем дек по значеним
    #print(sorted_str)
    while len(sorted_str) > 1:          # пока в деке больше 1 элемена
        value = sorted_str[0][1] + sorted_str[1][1]             # соединяем значения двух наименьших элементов
        node = BinaryTree(left=sorted_str.popleft()[0], right=sorted_str.popleft()[0])    # создаем узел
        for i, elem in enumerate(sorted_str):                                             # и ищем куда его вставить
            if value > elem[1]:                 # если значение двух минимальных элементов больше третьего
                continue                         # идем дальше
            else:                                # пока не найдем элемент с бОльшим знчением, вставим узел перед ним
                sorted_str.insert(i, (node, value))
                break
        else:
            sorted_str.append((node, value))         # если сумма двух минимальных больше значения всех остальных то
                                                     # вставляем узел в конец дека
    print(sorted_str)
    print(sorted_str[0][0])
    return sorted_str[0][0]                     # Почему возвращаем значение нулевого элемента???


#print(haffman(s))

def haffman_code(tree, path=''):                            # Собираем результат
    if not isinstance(tree, BinaryTree):                    # Если элемент не имеет потомков(не является binary tree)
        final_code[tree] = path                             # то элемент - лист дерева, возвращем собранный до него путь
    else:                                                   # если имеет то рекурсивно продолжаем обход по поддеревьям
        haffman_code(tree.left, path=f'{path}0')            # Если идем налево то добавляем к пути 0
        haffman_code(tree.right, path=f'{path}1')           # Если идем направо то добавляем к пути 1


haffman_code(haffman(s))

print(final_code)

for i in s:
    print(final_code[i], end=' ')
