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
import hashlib


# саму строку тоже считает уникальной подстрокой, поэтому на 1 больше.

def unique_substrings(inp_str='papa'):
    dip = (set([inp_str[i:j + i + 1] for i in range(len(inp_str)) for j in range(len(inp_str) + 1)]))
    return f'{inp_str} - {len(dip)} уникальных подстрок включая саму строку.'


def from_the_end():
    my_set = set()
    my_dict = {}
    inp_str = str(input("Введите строку S: "))  # не считает саму подстроку за уникальную.
    for i in range(len(inp_str)):
        for j in range(len(inp_str) - 1 if i == 0 else len(inp_str), i, -1):
            my_dict[hash(inp_str[i:j])] = inp_str[i:j]
            my_set.add(hash(inp_str[i:j]))
    print(f'{inp_str} - {len(my_set)} уникальных подстрок. Сама строка не считается уникальной.')
    for key in my_dict.keys():
        if key in my_set:
            print(my_dict[key])


def from_the_beginning():
    inp_str = str(input("Введите строку S: "))  # не считает саму подстроку за уникальную.
    my_set = set()
    my_dict = {}
    for i in range(len(inp_str)):
        for j in range(i + 1, len(inp_str) if i == 0 else len(inp_str) + 1):
            hash_obj = hashlib.md5((inp_str[i:j]).encode('utf-8'))
            hex_dig_res = hash_obj.hexdigest()
            my_dict[hex_dig_res] = inp_str[i:j]
            my_set.add(hex_dig_res)
    print(f'{inp_str} - {len(my_set)} уникальных подстрок. Сама строка не считается уникальной.')
    for key in my_dict.keys():
        if key in my_set:
            print(my_dict[key])


if __name__ == '__main__':
    print(unique_substrings())
    print(unique_substrings('mam'))
    from_the_end()
    from_the_beginning()

    inp_str = str(input("Введите строку S: "))  # не считает саму подстроку за уникальную.
    my_dict = {}
    for i in range(len(inp_str)):
        for j in range(i + 1, len(inp_str) if i == 0 else len(inp_str) + 1):
            hash_obj = hashlib.md5((inp_str[i:j]).encode('utf-8'))
            hex_dig_res = hash_obj.hexdigest()
            my_dict[hex_dig_res] = inp_str[i:j]
    print(f'{inp_str} - {len(my_dict)} уникальных подстрок. Сама строка не считается уникальной.')
    for key in my_dict.keys():
        print(my_dict[key])
