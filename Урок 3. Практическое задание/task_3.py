"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

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


string_ = 'papa'

combintations = []
hashes = set()
max_num_comb = len(string_)
for num_char_in_comb in range(1, len(string_)):
    for num_comb in range(max_num_comb):
        sub_string = string_[num_comb:num_comb+num_char_in_comb]
        hash_sub_string = hashlib.md5(sub_string.encode('utf-8')).hexdigest()
        len_before = len(hashes)
        hashes.add(hash_sub_string)
        if len_before < len(hashes):
            combintations.append(sub_string) 
    max_num_comb -= 1 

print(combintations)
