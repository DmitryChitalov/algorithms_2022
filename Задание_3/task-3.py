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

S = input('Введите строку ')
N = len(S)
set_ss = set()

for p1 in range(N + 1):
    for p2 in range(p1 + 1, N + 1):
        if p1 == 0 and p2 == N:  # вся строка не нужна
            continue
        ss = S[p1:p2]
        ss_bytes = ss.encode(encoding='utf-8')
        ss_hash = hashlib.md5(ss_bytes).hexdigest()
        set_ss.add((ss, ss_hash))

for item in set_ss:
    print(item[0])
