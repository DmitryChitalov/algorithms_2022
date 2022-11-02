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

# Создадим класс для создания бинарного дерева.
class NodeHaffmanTree:
    """ Класс для создания ноды бинарного дерева алгоритма Хаффмана. """

    def __init__(self, left_el=None, right_el=None):
        self.left_el = left_el
        self.right_el = right_el


def haffman_tree(string_code):
    """ Функция для создания бинарного дерева для алгоритма Хаффмана. """

    # Создадим коллекцию в виде словаря для подсчета частоты повторений символов в кодируемой строке.
    count_string_code = Counter(string_code)

    # Отсортируем словарь по возрастанию частоты появления элементов и создадим дек в виде списка кортежей
    # (символ, частота).
    sort_list = deque(sorted(count_string_code.items(), key=lambda item: item[1]))
    # Пока длина списка больше 1 будем записывать символы в бинарное дерево.
    while len(sort_list) > 1:
        # Подсчитываем веса элеметов и создаём правого и левого потомка дерева.
        weight = sort_list[0][1] + sort_list[1][1]
        node = NodeHaffmanTree(left_el=sort_list.popleft()[0], right_el=sort_list.popleft()[0])
        # Проверяем веса элементов в списке, если он меньше подсчитанного соседних элементов, вставляем ноду в список
        # или если его не нашлось в конец списка.
        for i, item in enumerate(sort_list):
            if weight > item[1]:
                continue
            else:
                sort_list.insert(i, (node, weight))
                break
        else:
            sort_list.append((node, weight))

    return sort_list[0][0]


dict_code = dict()


def haffman_code(haffman_code_tree, path=''):
    """ Функция создания кодов элементов в алгоритме Хаффмана. """
    # Обходим дерево и если оно принадлежит классу NodeHaffmanTree, то добавляем код элемента в словарь, иначе
    # добавляем к коду '0' и '1' к правому и левому потомку, запускаем рекурсивно функцию и продолжаем обход бинарного
    # дерева построенного по алгоритму Хафффмана.
    if not isinstance(haffman_code_tree, NodeHaffmanTree):
        dict_code[haffman_code_tree] = path

    else:
        haffman_code(haffman_code_tree.left_el, path=f'{path}0')
        haffman_code(haffman_code_tree.right_el, path=f'{path}1')


def haffman_decode(list_decode, dict_code):
    """ Функция декодирования строки алгоритма Хаффмана. """
    string_decode = ''
    for _ in list_decode:
        for k, v in dict_code.items():
            if _ == v:
                string_decode += k

    return string_decode



string_code = "I like programming on Python!!!"

haffman_code(haffman_tree(string_code))

# Выводим полученный код на экран.
print(f'Код строки: "{string_code}", по алгоритму Хаффмана:\n')
list_decode = []
for i in string_code:
    print(dict_code[i], end=' ')
    list_decode.append(dict_code[i])

print('\n')

# Выведем таблицу кодов символов для декодирования строки.
print(f'Таблица кодов символов алгоритма Хаффмана для строки: "{string_code}"')
for k, v in dict_code.items():
    print(f'{k} : {v}')

print('\n')
# Для проверки написанного кода, декодируем строку.
print(f'Декодированная строка: "{haffman_decode(list_decode, dict_code)}"')
