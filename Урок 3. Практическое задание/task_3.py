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


def uniq(word):
    word_set = set()
    word_dict = {}
    for i in range(len(word)):
        for j in range(len(word)- 1 if i == 0 else len(word), i, -1):
            word_set.add(hash(word[i:j]))
            print(word[i:j])
            word_dict[word[i:j]] = hash(word[i:j])
    print('Уникальных строк:', len(word_set))



word = input('Введите слово: ')
uniq(word)