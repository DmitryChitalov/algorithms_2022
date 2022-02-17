"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""
from functools import reduce
from collections import defaultdict

def_dict = defaultdict(list)

# Думал в этом же направлении, но смущало двойная работа: сначала перевести в формат хранения - [‘A’, ‘2’],
# а потом джоинить чтобы сделать 'A2'
for i in range(1, 3):
    def_dict[f"num_{i}"] = (list(input(f'Введите num_{i}: ')))

# делал бы так. Получилось громоздко, но выводит как по заданию
sum_num = list(k for k in hex(sum([int("".join(j), 16) for j in def_dict.values()])).upper() if k != "0" and k != "X")
print(f'Сумма элементов равна {sum_num}')

multi_num = hex(reduce(lambda x, y: x * y, [int("".join(l), 16) for l in def_dict.values()])).upper()
print(f'{list(s for s in multi_num if s != "0" and s != "X")}')

# Такой вывод лаконичнее (из примера разбора дз)
# не знал что так можно
print("Сумма: ", list('%X' % sum([int("".join(j), 16) for j in def_dict.values()])))