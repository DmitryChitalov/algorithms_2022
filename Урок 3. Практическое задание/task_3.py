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

def hash_function(input_string):
    hash_obj = hashlib.md5(input_string.encode())
    return hash_obj.hexdigest()


if __name__ == '__main__':
    # print(dir(hashlib))
    print('')
    result_set = set()
    input_string = input('Please enter string for checking:  ').lower()
    print('')
    length_string = len(input_string)
    for i in range(0, length_string+1):
        # print(f'i= {i}')
        for j in range(i+1, length_string+1):
            # print(f'j= {j}')
            check_string = input_string[i:j]
            if not check_string == "" and check_string != input_string:
                result_set.add(hash_function(check_string))
                print(f'checking:  {check_string}   > Unique Substrings : {len(result_set)} ')
    print(f'\n There are {len(result_set)} uniq substring in word {input_string} ')


# Script listing:
#
# Please enter string for checking:  papa
#
# checking:  p   > Unique Substrings : 1
# checking:  pa   > Unique Substrings : 2
# checking:  pap   > Unique Substrings : 3
# checking:  a   > Unique Substrings : 4
# checking:  ap   > Unique Substrings : 5
# checking:  apa   > Unique Substrings : 6
# checking:  p   > Unique Substrings : 6
# checking:  pa   > Unique Substrings : 6
# checking:  a   > Unique Substrings : 6
#
#  There are 6 uniq substring in word papa
#
# Process finished with exit code 0


