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

from hashlib import sha256


def get_hash(s):
    return sha256(s.encode()).hexdigest()


def get_sub_strings(text):
    uniq_sub_str = set()
    for i in range(len(text)):
        for j in range(len(text), i, -1):
            sub_str = text[i:j]
            if text != sub_str:
                print(sub_str, end=' | ')
                uniq_sub_str.add(get_hash(sub_str))
    print()
    return uniq_sub_str


if __name__ == '__main__':
    text = 'python'
    sub_string = get_sub_strings(text)
    for i, sub_str in enumerate(sub_string):
        print(f'{i+1}. хеш: {sub_str}')
    print(f'Уникальных подстрок в строке "{text}": {len(sub_string)}')
