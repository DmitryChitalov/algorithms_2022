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

from task_2 import password_hash_sha


def unique_substr():
    print('Пожалуйста, введите Вашу строку: ', end='')
    user_string = input()
    # user_list = list()  # Чтобы вывести сами подстроки (для проверки)
    user_set = set()
    for i in range(0, len(user_string)):
        for k in range(0, len(user_string) - i):
            if i != 0 or k != 0:
                if k == 0:
                    # user_list.append(user_string[i:])  # Чтобы вывести сами подстроки (для проверки)
                    user_hash = password_hash_sha(user_string[i:])
                    user_set.add(user_hash)
                else:
                    # user_list.append(user_string[i:][:-k])  # Чтобы вывести сами подстроки (для проверки)
                    user_hash = password_hash_sha(user_string[i:][:-k])
                user_set.add(user_hash)
    # print(user_list)  # Чтобы вывести сами подстроки (для проверки)
    print(f'Количество уникальных подстрок: {len(user_set)}')


if __name__ == '__main__':
    unique_substr()
