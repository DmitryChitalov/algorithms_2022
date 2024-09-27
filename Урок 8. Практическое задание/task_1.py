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

user_string = "beep boop beer! Shubin Ostap"


# 1- Создаем Класс, на вход принимает объект
class Wood(object):
    def __init__(self, left='', right=''):
            self.left = left
            self.right = right

    # функция возвращает левый и правый корень
    def root(self):
        return self.left, self.right


# 2- функция сортировки и подсчета символов в строке
def sort_string(user_string):
    # Подсчет символов
    symbol_count = Counter(user_string)
    # print(symbol_count)
    # Создаем список пар и сортируем
    result = sorted(dict(symbol_count).items(), key=lambda x: x[1])
# result = sorted(dict(count).items(), key=lambda x: x[1], reverse=True)
    # print(result[2:])
    return result

# print(sort_string(user_string))


# 3 - Функция создает очередь и считает веса(повторы элемента в строке), суммируя веса получаем корень

def create_queue(sort_string):
    # Создаем рекурсию
    if len(sort_string) == 1:
        return sort_string[0][0]
    # Создаем переменные для символа и веса для 1 и 2 элемента в очереди
    (symbol_1, weight_1) = sort_string[0]
    (symbol_2, weight_2) = sort_string[1]
    # Убераем первые два элемента из списка
    # print(sort_string)
    sort_string = sort_string[2:]
    # Создаем корень
    root = Wood(symbol_1, symbol_2)
    # Добавляем корень в наш исходный список, суммируем их вес
    sort_string.append((root, weight_1 + weight_2))
    # Создаем список пар и сортируем
    sort_string = sorted(sort_string, key=lambda x: x[1])
    # Возвращаем список для рекурсии
    return create_queue(sort_string)

# create_queue(sort_string(user_string))


# 4- Функция кодировки Хаффмана

def huffman_code(wood, code_number='', result={}):  # в функцию передаем наше "дерево" - объект класса Tree,
    # созданный функцией make_tree, а результат будет словарь - ключ-буква, значение - код, состоящий из нулей и единиц
    if type(wood) is not Wood:  # наше дерево состоит из звеньев (объект Tree) и листьев (буквы, символы)
        return {wood: code_number}  # если мы добираемся до символа, то записываем словарь {буква: код}
    left, right = wood.root()  # двигаемся по дереву используя функцию из класса Tree - next_leaf, возвращая
    # left и right
    result.update(huffman_code(left, code_number + '0', result))  # используем рекурсии, чтобы двигаться по дереву
    result.update(huffman_code(right, code_number + '1', result))  # и наполнять итоговый словарь-кодовую таблицу
    return result


# 1 функция сортировки и подсчета символов в строке
obj_sort_string = sort_string(user_string)
print(obj_sort_string)
# 2 Функция создает очередь и считает веса(повторы элемента в строке), суммируя веса получаем корень
obj_root = create_queue(obj_sort_string)
print(obj_root)
# 3 Функция кодировки Хаффмана
obj_encoded = huffman_code(obj_root)
print(obj_encoded)







