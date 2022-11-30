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


def create_hash(a: str):
    '''
    Функция принмает данные и возвращает хеш
    :param a: str
    :return: str
    '''
    import hashlib
    hash_obj = hashlib.sha224(a.encode('utf-8'))
    result = hash_obj.hexdigest()

    return result


def substring_search(line: str):
    '''
    Функция принимает строку находит все подстроки создает из них хеш
     и возвращает множество уникальных хеш-значений
    :param line:str
    :return:set
    '''

    result = set()
    k = 0
    while k < len(s) - 1:
        i = 0
        k += 1
        while i + k < len(s) + 1:
            el = s[i:i + k]
            # print(el)
            result.add(create_hash(el))
            i += 1
    return result


def program_3_3(line: str):
    '''
    Программа принимает строку и выводит на экран количество уникальных подстрок в ней
    :param line: str
    :return:
    '''
    substring_set = substring_search(line)
    result = len(substring_set)
    print(f'Строка "{line}" содержит {result} уникальных подстрок')


s = 'рара'
program_3_3(s)
