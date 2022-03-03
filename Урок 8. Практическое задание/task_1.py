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


class Tree():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def run(new_str):
    new_str = Counter(new_str)
    li = list(new_str.items())
    while len(li) > 1:
        li.sort(reverse=True, key=lambda k: k[1])
        val1, q1 = li.pop()
        val2, q2 = li.pop()
        summ = q1 + q2
        li.append((Tree(val1, val2), summ))
        
    return li[0][0]
   
code_di = dict()

def get_code(tree, path=''):
    if not isinstance(tree, Tree):
        code_di[tree] = path

    else:
        get_code(tree.left, path=f'{path}0')
        get_code(tree.right, path=f'{path}1')

source = 'test new str'
full = run(source)
res = get_code(full)

for i in source:
    print(code_di[i], end=' ')
print()
print(code_di)
'''
Получен словарь для кодирования этого вырашения
{'e': '00', 'n': '010', 'r': '0110', 'w': '0111', 't': '10', ' ': '110', 's': '111'}'''