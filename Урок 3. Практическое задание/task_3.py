"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib

my_str = 'papa'
sub_str_set = set()
for i in range(len(my_str)):
    if i == 0:
        str_slice = my_str[i+1:-1]
    else:
        str_slice = my_str[(i+1):]
    sub_str = my_str[i]
    sub_str_set.add(hashlib.md5(sub_str.encode()).hexdigest())
    for n in range(len(str_slice)):
        sub_str += str_slice[n]
        sub_str_set.add(hashlib.md5(sub_str.encode()).hexdigest())
print(len(sub_str_set))
