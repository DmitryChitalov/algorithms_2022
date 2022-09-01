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

from hashlib import sha1


def uniq_substring(input_str):
    result_set = set()
    for i in range(len(input_str)):
        for j in range(i, len(input_str) + 1):
            sliced_string = input_str[i:j]
            if sliced_string != '' and len(sliced_string) != len(input_str):
                result_set.add(sha1(sliced_string.encode()).hexdigest())
                result_set.add(sha1(sliced_string[::-1].encode()).hexdigest())
    return len(result_set)


if __name__ == '__main__':
    while True:
        input_data = input('Введите любую строку для подсчета уникальных подстрок:\n'
                           '1 - для выхода\n')
        if input_data == '1':
            break
        print(f'Количество уникальных подстрок: {uniq_substring(input_data)}')
