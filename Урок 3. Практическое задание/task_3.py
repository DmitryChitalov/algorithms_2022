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
from hashlib import md5

memory = set()
test = 'Hello'  # h, e, l, o, he, el, ll, lo, hel, ell, llo,


def find_substrings(string: str):
    length = len(string)
    for i in range(length):
        for j in range(i + 1, length + 1):
            if string[i:j] != string:
                memory.add(md5(string[i:j].encode()).hexdigest())
                print(string[i:j])
    print(memory, f'Количество элементов:  {len(memory)}')

            


if __name__ == '__main__':
    find_substrings('Hello')
