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


def make_new_substring(string, set_to_add=set()):
    a1 = set_to_add
    letters = list(string)
    if len(string) == 0:
        return a1
    else:
        for i in range(len(letters)):
            let_to_join = letters[:(len(letters) - i)]
            word = "".join(let_to_join)
            word_hash = hashlib.sha256(word.encode()).hexdigest()
            a1.add(word_hash)
        return make_new_substring(letters[1:], a1)


str1 = input('Введите строку из строчных латинских букв   ')
set1 = make_new_substring(str1)
str1_hash = hashlib.sha256(str1.encode()).hexdigest()
set1.discard(str1_hash)
print(set1)
print(f'{str1} - уникальных подстрок: {len(set1)}')
