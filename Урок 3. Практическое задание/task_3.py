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

# Напишем функцию определяющую количество уникальных хэш в строке из латинских букв.
def unique_str(string):
    for i in range(len(string)):
        for j in range(i, len(string)):
            if not string[i:j + 1] == string:
                uni_str.add(hashlib.sha256(string[i:j + 1].encode()).hexdigest())
    return f'{string} - {len(uni_str)} уникальных подстрок.'


uni_str = set() # Создаём пустое множество.

# Проверим работу функции.
string = 'papa'
print(unique_str(string))
print(uni_str)

string = 'tetra'
print(unique_str(string))
print(uni_str)

string = 'system'
print(unique_str(string))
print(uni_str)
