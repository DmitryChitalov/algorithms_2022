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


def huffman_tree(string):
    string_counter = Counter(string)
    sorted_elements = deque(sorted(string_counter.items(), key=lambda item: item[1]))
    if len(sorted_elements) != 1:
        for v in range(len(sorted_elements)-1):
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}
            for idx, letter_count in enumerate(sorted_elements):
                if weight > letter_count[1]:
                    continue
                else:
                    sorted_elements.insert(idx, (comb, weight))
                    break
            else:
                sorted_elements.append((comb, weight))
    else:
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    return huffman_code(sorted_elements[0][0], sorted_elements[0][0])


def huffman_code(main_dict, tree, path=''):
    if not isinstance(tree, dict):
        main_dict[tree] = path
    else:
        huffman_code(main_dict, tree[0], path=f'{path}0')
        huffman_code(main_dict, tree[1], path=f'{path}1')
    return main_dict


huff_string = "beep boop beer!"

for i in huff_string:
    print(huffman_tree(huff_string)[i], end=' ')

print('\n')

print('Эта тема дается мне немного тяжело, поэтому решил сделать опираясь на пример с урока, как и написано в одном\n'
      'из вариантов ТЗ. Я заменил имена нескольких переменных, убрал цикл while и поставил вместо него for на №\n'
      'строке, сделал вызов функции huffman_code сразу из huffman_tree, также убрал словарь и куда добавлялась\n'
      'закодированная строка и вместо него использовал словарь sorted_elements из функции huffman_tree, передав\n'
      'его 2 раза в качестве аргумента в huffman_code, в итоге получился максимально компактный, оптимизированный\n'
      'и читабельный код')
