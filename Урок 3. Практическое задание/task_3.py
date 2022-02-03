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
from itertools import combinations
from hashlib import sha256


def get_unique_substrings(s):  # множество хешей
    return {sha256(bytes(s[i:j], 'UTF-8')).hexdigest()
            for i, j in combinations(range(len(s) + 1), 2) if (i, j) != (0, len(s))}


def calculate_hash_for_unique_substrings(s):  # Словарь тоже отсекает одинаковые ключи, но и ассоциирует с подстроками
    return {sha256(bytes(s[i:j], 'UTF-8')).hexdigest(): s[i:j]
            for i, j in combinations(range(len(s) + 1), 2) if (i, j) != (0, len(s))}


def print_substrings_and_hash(dict_):  # для красивой печати
    print(f'Количество уникальных подстрок: {len(dict_)}')
    for i, item in enumerate(dict_.items()):
        print(f'{i + 1}. {item[0]}: {item[1]}')


print("Строка 'папа'")
print_substrings_and_hash((calculate_hash_for_unique_substrings('papa')))
print("Строка 'rococo'")
print_substrings_and_hash((calculate_hash_for_unique_substrings('rococo')))
