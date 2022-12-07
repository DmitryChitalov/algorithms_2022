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


def main():
    s = input('Введите строку для перебора: ')
    substrings_hashes = get_substrings_hashes(s)
    print(f"{s} - {len(substrings_hashes)} уникальных подстрок")


def get_substrings_hashes(s):
    result = set()
    for window_sz in range(1, len(s)):
        idx_1 = 0
        idx_2 = window_sz
        while idx_2 <= len(s):
            substring = s[idx_1: idx_2]
            hash_string = hashlib.sha256(substring.encode('utf-8')).hexdigest()
            result.add(hash_string)
            idx_1 += 1
            idx_2 += 1
    return result


if __name__ == '__main__':
    main()

