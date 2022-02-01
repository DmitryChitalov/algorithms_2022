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

word = input('Введите слово: ')
new_word = word
# print(len(s))
hash_list = []

for i in range(1, len(word) + 1):
    hash_word = hashlib.sha256(new_word.encode()).hexdigest()

    if not (hash_word in hash_list) and new_word != word:
        hash_list.append(hash_word)
        print(new_word)

    for n in range(1, len(new_word)):
        temp_word = new_word[:len(new_word) - n]
        hash_word = hashlib.sha256(temp_word.encode()).hexdigest()

        if not (hash_word in hash_list):
            print(temp_word)
            hash_list.append(hash_word)

    new_word = word[i:len(word)]

print(f'{word} - {len(hash_list)} уникальных подстрок')
