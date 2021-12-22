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


def parts(word):
    result = list()
    hash_collect = set()
    for x in range(1, len(word)):
        start = 0
        end = x
        part = word[start: end]
        word_hash = hashlib.sha3_256(part.encode()).hexdigest()
        if word_hash in hash_collect:
            pass
        else:
            hash_collect.add(word_hash)
            result.append(part)
        for y in range(len(word) - x):
            start += 1
            end += 1
            part = word[start: end]
            word_hash = hashlib.sha3_256(part.encode()).hexdigest()
            if word_hash in hash_collect:
                pass
            else:
                hash_collect.add(word_hash)
                result.append(part)
    return f'{word} - {len(hash_collect)} уникальных подстрок \n{result}'


print(parts('geekbrains'))
