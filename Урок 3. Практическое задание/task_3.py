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

def uniqueSubstrings():

    strExample = 'pineapple'
    
    listStr = ['pineappl', 'ineapple', 'neapple', 'pineapp',
               'eapple', 'pineap', 'apple', 'pinea', 'pple',
               'pine', 'pin', 'eap', 'ple', 'pi', 'ne', 'ap',
               'pl', 'p', 'i', 'n', 'e', 'a', 'p', 'p', 'l', 'e']

    answerList = set()

    for elem in listStr:
        hesh = hashlib.sha256(elem.encode('utf8')).hexdigest()
        answerList.add(hesh)

    print 'Количество уникальных элементов: ' + str(len(answerList))


if name == 'main':
    uniqueSubstrings()

