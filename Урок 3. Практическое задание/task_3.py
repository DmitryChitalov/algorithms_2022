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


def test(text):
    hash_tabl = {}
    for n in range(len(text)):
        for i in range(len(text)):
            if text[i:n + 1:] != '' and text[i:n + 1:] != text:  # Можно убрать второе условие если нужна строка
                hash_tabl.setdefault(hashlib.sha256(text[i:n + 1:].encode()).hexdigest(), text[i:n + 1:])
    return hash_tabl.values()


for el in test(input('Введите строку: ')):
    print(el)
